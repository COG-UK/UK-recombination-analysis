import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Bio import SeqIO

# get the gene positions
with open("../background/MN908947.gb", "r") as f:
    gb = SeqIO.read(f, "genbank")

genes = {}
for feat in gb.features:
    if feat.type == "gene":
        name = feat.qualifiers['gene'][0].lower()
        start = int(feat.location.start)
        length = int(feat.location.end) - int(feat.location.start)
        genes[name] = (start, length)

fig, ax = plt.subplots(1, 1, figsize=(10, 2.5), dpi=250)

# no axes
plt.axis('off')
plt.xlim([-0.1, 1.05])
plt.ylim([-0.8, 1])

# whole genome as a black line
r = patches.Rectangle((0, 0.745), 1, 0.01, facecolor = "black", fill = True, edgecolor = 'none')
ax.add_patch(r)

# genes as grey rectangles
for n,g in genes.items():
    bp_trim = 50
    gstart = (g[0] / 29903 ) + (bp_trim / 29903)
    glen = (g[1] / 29903) - (bp_trim / 29903)
    grec = patches.Rectangle((gstart, 0.7), glen, 0.1, facecolor = "lightgrey", fill = True, linewidth = 0)
    ax.add_patch(grec)

gene_label_pos = [10935.0, 23498.0, 25831.0 - 800, 26383.0 - 600, 26881.5 - 700, 27319.0 - 450, 27601.0 + 400, 28101.0 + 1000, 28928.0 + 900, 29640.5 + 1000]

# gene names
i = 0
for n,g in genes.items():
    xcoord = gene_label_pos[i] / 29903
    plt.figtext(x = xcoord, y = 0.94, s = n.upper(), size = 6, family = 'monospace', ha = "center", transform=ax.transData)
    i += 1

# gene name -> gene rectangle mapping polygons
i = 0
for n,g in genes.items():
    bp_trim = 50
    gstart = (g[0] / 29903 ) + (bp_trim / 29903)
    glen = (g[1] / 29903) - (bp_trim / 29903)
    gend = gstart + glen

    xcoord = gene_label_pos[i] / 29903

    x = [gstart, gend, xcoord, xcoord]
    y = [0.8, 0.8, 0.92, 0.92]
    coords = list(zip(x, y))

    poly = patches.Polygon(coords, closed = True, alpha = 0.3, fill = True, edgecolor = 'none', facecolor = "lightgrey")
    ax.add_patch(poly)
    i += 1

# orf1a only:
xcoord = ((13468 - 266) / 29903 )/ 2
plt.figtext(x = xcoord, y = 0.94, s = "ORF1A", size = 6, family = 'monospace', ha = "center", transform=ax.transData)

x = [266 / 29903, 13468 / 29903, xcoord, xcoord]
y = [0.8, 0.8, 0.92, 0.92]
coords = list(zip(x, y))
poly = patches.Polygon(coords, closed = True, alpha = 0.3, fill = True, edgecolor = 'none', facecolor = "lightgrey")
ax.add_patch(poly)


# the groups
groups = ["Group A", "Group B", "Group C", "Group D", "CAMC-CBA018", "CAMC-CB7AB3", "MILK-103C712", "QEUH-1067DEF"]
for i in range(0, 8):
    ycoord = 1 - ((i * 5/32) + 0.5)
    plt.figtext(x = -0.01, y = ycoord + 0.01, s = groups[i], size = 6, family = 'monospace', ha = "right", va = "bottom", transform=ax.transData)

# breakpoints = [21764, 6952, 27971, 21994, 21764, None, 27975, 6956]
# cols = [("#cfc084","#a5aed9"),("#cfc084","#a5aed9"),("#a5aed9","#cfc084"),("#cfc084","#a5aed9"),("#cfc084","#a5aed9"),None,("#cfc084","#a5aed9"),("#a5aed9","#cfc084")]
# lins = [("B.1.177","B.1.1.7"),("B.1.36.28","B.1.1.7"),("B.1.1.7","B.1.221.1"),("B.1.36.17","B.1.1.7"),("B.1.177","B.1.1.7"),None,("B.1.177.16","B.1.1.7"),("B.1.1.7","B.1.177.9")]
# for i in range(0, 8):
#     if i == 5:
#         continue
#     ycoord = 1 - ((i * 5/32) + 0.5)
#
#     lstart = 0
#     lend = (lstart + breakpoints[i]) / 29903
#     llen = lend - lstart
#     rec_left = patches.Rectangle((lstart, ycoord), llen, 0.1, facecolor = cols[i][0], fill = True, linewidth = 0)
#     plt.figtext(x = lstart + llen / 2, y = ycoord + 0.022, s = lins[i][0], size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)
#
#     rstart = breakpoints[i] / 29903
#     rend = 1
#     rlen = rend - rstart
#     rec_right = patches.Rectangle((rstart, ycoord), rlen, 0.1, facecolor = cols[i][1], fill = True, linewidth = 0)
#     plt.figtext(x = rstart + rlen / 2, y = ycoord + 0.022, s = lins[i][1], size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)
#
#     ax.add_patch(rec_left)
#     ax.add_patch(rec_right)

breakpoints = [(21255, 21765), (6528, 6954), (24914, 28651), (21575, 23063), (11396, 21991), None, (26801, 27972), (6954, 10870)]
cols = [("#cfc084","#a5aed9"),("#cfc084","#a5aed9"),("#a5aed9","#cfc084"),("#cfc084","#a5aed9"),("#cfc084","#a5aed9"),None,("#cfc084","#a5aed9"),("#a5aed9","#cfc084")]
lins = [("B.1.177","B.1.1.7"),("B.1.36.28","B.1.1.7"),("B.1.1.7","B.1.221.1"),("B.1.36.17","B.1.1.7"),("B.1.177","B.1.1.7"),None,("B.1.177.16","B.1.1.7"),("B.1.1.7","B.1.177.9")]
for i in range(0, 8):
    if i == 5:
        continue
    ycoord = 1 - ((i * 5/32) + 0.5)

    lstart = 0
    lend = (lstart + breakpoints[i][0]) / 29903
    llen = lend - lstart
    rec_left = patches.Rectangle((lstart, ycoord), llen, 0.1, facecolor = cols[i][0], fill = True, linewidth = 0)
    plt.figtext(x = lstart + llen / 2, y = ycoord + 0.022, s = lins[i][0], size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)

    rstart = breakpoints[i][1] / 29903
    rend = 1
    rlen = rend - rstart
    rec_right = patches.Rectangle((rstart, ycoord), rlen, 0.1, facecolor = cols[i][1], fill = True, linewidth = 0)
    plt.figtext(x = rstart + rlen / 2, y = ycoord + 0.022, s = lins[i][1], size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)

    ax.add_patch(rec_left)
    ax.add_patch(rec_right)

for i in [5]:
    cols = ("#a5aed9","#cfc084","#a5aed9")
    ycoord = 1 - ((i * 5/32) + 0.5)
    rec_1 = patches.Rectangle((0, ycoord), 3267 / 29903, 0.1, facecolor = cols[0], fill = True, linewidth = 0)
    rec_2 = patches.Rectangle((5388 / 29903, ycoord), (12534 - 5388) / 29903, 0.1, facecolor = cols[1], fill = True, linewidth = 0)
    rec_3 = patches.Rectangle((21765 / 29903, ycoord), (29903 - 21765) / 29903, 0.1, facecolor = cols[2], fill = True, linewidth = 0)
    ax.add_patch(rec_1)
    ax.add_patch(rec_2)
    ax.add_patch(rec_3)

    plt.figtext(x = 0 + ((3267 / 29903 )/ 2), y = ycoord + 0.022, s = "B.1.1.7", size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)
    plt.figtext(x = (6286 / 29903) + (((12534 - 6286) / 29903) / 2), y = ycoord + 0.022, s = "B.1.177", size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)
    plt.figtext(x = (21765 / 29903) + (((29903 - 21765) / 29903) / 2), y = ycoord + 0.022, s = "B.1.1.7", size = 6, color = "white", family = 'monospace', ha = "center", transform=ax.transData)

rec = patches.Rectangle((0, -0.67), 1, 0.005, facecolor = "black", fill = True, linewidth = 0)
ax.add_patch(rec)
for i in range(0, 29000, 4000):
    rec = patches.Rectangle((i / 29903, -0.68), 0.001, 0.01, facecolor = "black", fill = True, linewidth = 0)
    ax.add_patch(rec)
    plt.figtext(x = i / 29903, y = -0.75, s = str(i), size = 6, color = "black", family = 'monospace', ha = "center", transform=ax.transData)

plt.figtext(x = 0.5, y = -0.9, s = "position (base)", size = 7, color = "black", family = 'monospace', ha = "center", transform=ax.transData)


plt.savefig("figure_4.png", bbox_inches='tight')














#
