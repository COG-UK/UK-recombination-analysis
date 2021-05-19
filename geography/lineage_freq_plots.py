import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import pandas as pd
import datetime
import sys

import colorsys
import pickle

import seaborn as sns

Ntoplins = 9
cols = sns.color_palette(None, Ntoplins + 1)

df = pd.read_csv(sys.argv[1])

parentlins = []
for i,row in df.iterrows():
    x = row['lineage']
    if x[0:8] == "B.1.177.":
        parentlins.append("B.1.177")
    elif x[0:7] == "B.1.36.":
        parentlins.append("B.1.36")
    else:
        parentlins.append(x)

    # parentlins.append(x)


df['parentlins'] = parentlins
toplin_idx = df['parentlins'].value_counts()[0:Ntoplins].index
toplins = []
for tl in toplin_idx:
    toplins.append(tl)
toplins.append("other")

# print(toplins)

with open(sys.argv[2], "r") as f:
    date = [line.rstrip() for line in f][0]

print(date)

date_list = []
start_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
for day in range(28):
    a_date = (start_date + datetime.timedelta(days = day))
    date_list.append(a_date)

# print(date_list)

def get_toplin_counts(linvec, toplins):
    d = {x: 0 for x in toplins}
    for v in linvec:
        if v in d:
            d[v] += 1
        else:
            d["other"] += 1

    return(d)

freqs = []
for date in date_list:
    window_start = (date - datetime.timedelta(days = 3)).isoformat()
    window_end = (date + datetime.timedelta(days = 3)).isoformat()

    temp = df[(df['sample_date'] >= window_start) & (df['sample_date'] < window_end)]

    d = get_toplin_counts(temp["parentlins"], toplins)
    freqs.append(d)

# with open('lin_freqs.obj', 'wb') as f_lin_freqs:
#     pickle.dump(freqs, f_lin_freqs)
#
# with open('date_list.obj', 'wb') as f_date_list:
#     pickle.dump(date_list, f_date_list)
#
# with open('top_lins.obj', 'wb') as f_top_lins:
#     pickle.dump(toplins, f_top_lins)
#
# with open('lin_freqs.obj', 'rb') as f_lin_freqs:
#     freqs = pickle.load(f_lin_freqs)
#
# with open('date_list.obj', 'rb') as f_date_list:
#     date_list = pickle.load(f_date_list)
#
# with open('top_lins.obj', 'rb') as f_top_lins:
#     toplins = pickle.load(f_top_lins)

# the plot
fig, ax = plt.subplots(1, 1, figsize=(4, 2.5), dpi=250)

# no axes
plt.axis('off')
plt.xlim([-0.05, 1.1])
plt.ylim([-0.2, 1.2])

# get the polygons - one for each in toplins
y_coords_list = []
for d in freqs:
    y_coords = []
    total = sum(d.values())
    lower = 0
    upper = 0
    for l in toplins:
        upper = upper + d[l]
        y_coords.append((lower / total, upper / total))
        lower = upper

    y_coords_list.append(y_coords)

# for y in y_coords_list:
#     print(y)

# the frequencies:
for i,lin in enumerate(toplins):
    x = [x / len(freqs) for x in range(0, len(freqs))] + [x / len(freqs) for x in range(len(freqs) - 1, -1, -1)]
    y = []
    for y_coords in y_coords_list:
        y.append(y_coords[i][0])
    for j in range(len(y_coords_list) - 1, -1, -1):
        y.append(y_coords_list[j][i][1])

    coords = list(zip(x, y))
    poly = patches.Polygon(coords, closed = True, fill = True, facecolor = cols[i], linewidth = 0)
    ax.add_patch(poly)

# X axis
rec = patches.Rectangle((0, -0.02), 1 - 1 / len(date_list), 0.01, facecolor = "black", fill = True, linewidth = 0, transform=ax.transData)
ax.add_patch(rec)
for i in range(0, len(date_list), 7):
    j = i / len(date_list)
    rec = patches.Rectangle((j, -0.03), 0.001, 0.01, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = j, y = -0.1, s = date_list[i], size = 5, color = "black", family = 'monospace', ha = "center", transform=ax.transData)

plt.figtext(x = 0.5, y = -0.2, s = "date", size = 8, color = "black", family = 'monospace', ha = "center", transform=ax.transData)

# Y axis
rec = patches.Rectangle((-0.004, 0), 0.002, 1, facecolor = "black", fill = True, linewidth = 0, transform=ax.transData)
ax.add_patch(rec)
for i in range(0, 11, 1):
    rec = patches.Rectangle((-0.004, i / 10), -0.002, 0.005, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = -0.01, y = i / 10, s = str(i / 10), size = 5, color = "black", family = 'monospace', ha = "right", va = "center", transform=ax.transData)

plt.figtext(x = -0.1, y = 0.5, s = "cumulative frequency", rotation = "vertical", size = 8, color = "black", family = 'monospace', ha = "left", va = "center", transform=ax.transData)

plt.figtext(x = 0.5, y = 1.2, s = sys.argv[4], size = 8, color = "black", family = 'monospace', ha = "center", va = "center", transform=ax.transData)

# add a key
for i in range(len(toplins)):
    rec = patches.Rectangle((1.02, 0.9 - (i * 0.1)), 0.05, 0.1, facecolor = cols[i], fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = 1.1, y = 0.95 - (i * 0.1), s = toplins[i], size = 5, color = "black", family = 'monospace', ha = "left", va = "center", transform=ax.transData)



plt.savefig(sys.argv[3], bbox_inches='tight')
















#
