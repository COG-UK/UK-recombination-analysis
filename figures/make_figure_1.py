import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import pandas as pd
import datetime
import sys

import colorsys
import pickle

# df = pd.read_csv("../background/cog_2021-03-07.csv")
#
# parentlins = []
# for i,row in df.iterrows():
#     x = row['lineage']
#     if x[0:8] == "B.1.177.":
#         parentlins.append("B.1.177")
#     elif x[0:7] == "B.1.36.":
#         parentlins.append("B.1.36")
#     else:
#         parentlins.append(x)
#
# df['parentlins'] = parentlins
# toplin_idx = df['parentlins'].value_counts()[0:4].index
# toplins = []
# for tl in toplin_idx:
#     toplins.append(tl)
# toplins.append("other")
#
# # print(toplins)
#
# date_list = []
# start_date = datetime.datetime.strptime("2020-12-01", '%Y-%m-%d').date()
# for day in range(90):
#     a_date = (start_date + datetime.timedelta(days = day))
#     date_list.append(a_date)
#
# # print(date_list)
#
# def get_toplin_counts(linvec, toplins):
#     d = {x: 0 for x in toplins}
#     for v in linvec:
#         if v in d:
#             d[v] += 1
#         else:
#             d["other"] += 1
#
#     return(d)
#
# freqs = []
# for date in date_list:
#     window_start = (date - datetime.timedelta(days = 3)).isoformat()
#     window_end = (date + datetime.timedelta(days = 3)).isoformat()
#
#     temp = df[(df['sample_date'] >= window_start) & (df['sample_date'] < window_end)]
#
#     d = get_toplin_counts(temp["parentlins"], toplins)
#     freqs.append(d)
#
# with open('lin_freqs.obj', 'wb') as f_lin_freqs:
#     pickle.dump(freqs, f_lin_freqs)
#
# with open('date_list.obj', 'wb') as f_date_list:
#     pickle.dump(date_list, f_date_list)
#
# with open('top_lins.obj', 'wb') as f_top_lins:
#     pickle.dump(toplins, f_top_lins)

with open('lin_freqs.obj', 'rb') as f_lin_freqs:
    freqs = pickle.load(f_lin_freqs)

with open('date_list.obj', 'rb') as f_date_list:
    date_list = pickle.load(f_date_list)

with open('top_lins.obj', 'rb') as f_top_lins:
    toplins = pickle.load(f_top_lins)

# the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 2.5), dpi=250)

# no axes
plt.axis('off')
plt.xlim([-0.05, 1.1])
plt.ylim([-0.2, 1.3])

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
cols = ["#a6611a", "#dfc27d", "#f5f5f5", "#80cdc1", "#018571"]
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
    rec = patches.Rectangle((j, -0.03), 0.002, 0.01, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = j, y = -0.1, s = date_list[i], size = 5.5, color = "black", family = 'monospace', ha = "center", transform=ax.transData)

plt.figtext(x = 0.5, y = -0.3, s = "date", size = 10, color = "black", family = 'monospace', ha = "center", transform=ax.transData)

# Y axis
rec = patches.Rectangle((-0.004, 0), 0.002, 1, facecolor = "black", fill = True, linewidth = 0, transform=ax.transData)
ax.add_patch(rec)
for i in range(0, 11, 1):
    rec = patches.Rectangle((-0.004, i / 10), -0.002, 0.0075, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = -0.01, y = i / 10, s = str(i / 10), size = 6, color = "black", family = 'monospace', ha = "right", va = "center", transform=ax.transData)

plt.figtext(x = -0.075, y = 0.5, s = "cumulative frequency", rotation = "vertical", size = 10, color = "black", family = 'monospace', ha = "left", va = "center", transform=ax.transData)

# add a key
for i in range(len(toplins)):
    rec = patches.Rectangle((1.02, 0.9 - (i * 0.1)), 0.025, 0.1, facecolor = cols[i], fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = 1.05, y = 0.95 - (i * 0.1), s = toplins[i], size = 7, color = "black", family = 'monospace', ha = "left", va = "center", transform=ax.transData)

# add dates
grp_recombinant_dates = {"Group A": ("2021-01-30", "2021-02-14"),
                     "Group B": ("2020-12-23", "2020-12-24"),
                     "Group C": ("2021-01-18", "2021-01-30"),
                     "Group D": ("2021-02-02", "2021-02-07")}

grp_heights = [1.05, 1.05, 1.05, 1.20]

sin_recombinant_dates = {"CAMC-CBA018": "2020-12-18",
                     "CAMC-CB7AB3": "2020-12-18",
                     "MILK-103C712": "2021-01-12",
                     "QEUH-1067DEF": "2021-01-17"}

sin_heights = [1.15, 1.25, 1.125, 1.25]

counter = 0
for key,value in grp_recombinant_dates.items():
    valdate1 = datetime.datetime.strptime(value[0], '%Y-%m-%d').date()
    xpos1 = [i for i,x in enumerate(date_list) if x == valdate1][0] / len(date_list)
    # valdate2 = datetime.datetime.strptime(value[1], '%Y-%m-%d').date()
    # xpos2 = [i for i,x in enumerate(date_list) if x == valdate2][0] / len(date_list)

    # center = xpos1 + (xpos2 - xpos1) / 2

    rec = patches.Rectangle((xpos1 + 0.01, grp_heights[counter]), 0.03, 0.01, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    x = [xpos1, xpos1 + 0.01, xpos1 + 0.01]
    y = [grp_heights[counter] + 0.005, grp_heights[counter] + 0.02 + 0.015, grp_heights[counter] - (0.02 + 0.005)]
    coords = list(zip(x, y))
    poly = patches.Polygon(coords, closed = True, fill = True, facecolor = "black", linewidth = 0)
    ax.add_patch(poly)

    plt.figtext(x = xpos1 + 0.01, y = grp_heights[counter] + 0.02, s = key, size = 7, color = "black", family = 'monospace', ha = "left", va = "bottom", transform=ax.transData)

    counter += 1

counter = 0
for key,value in sin_recombinant_dates.items():
    valdate1 = datetime.datetime.strptime(value, '%Y-%m-%d').date()
    xpos1 = [i for i,x in enumerate(date_list) if x == valdate1][0] / len(date_list)

    if counter != 1:
        rec = patches.Rectangle((xpos1 + 0.01, sin_heights[counter]), 0.03, 0.01, facecolor = "black", fill = True, linewidth = 0)
        ax.add_patch(rec)
        x = [xpos1, xpos1 + 0.01, xpos1 + 0.01]
        y = [sin_heights[counter] + 0.005, sin_heights[counter] + 0.02 + 0.015, sin_heights[counter] - (0.02 + 0.005)]
        coords = list(zip(x, y))
        poly = patches.Polygon(coords, closed = True, fill = True, facecolor = "black", linewidth = 0)
        ax.add_patch(poly)

    plt.figtext(x = xpos1 + 0.01, y = sin_heights[counter] + 0.02, s = key, size = 7, color = "black", family = 'monospace', ha = "left", va = "bottom", transform=ax.transData)

    counter += 1


plt.savefig("figure_1.png", bbox_inches='tight')
















#
