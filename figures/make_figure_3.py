import sys
import collections
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import lines as mplines

sys.path.append('/Users/ben/programs/baltic/baltic')
import baltic as bt

myTree = bt.loadNewick("../weighted_background/2000.sample.masked.treefile", absoluteTime=False)
myTree.traverse_tree()
myTree.sortBranches()

# figure, axes
fig, ax = plt.subplots(figsize=(5,10), facecolor='w', dpi = 300)

# what to plot on the x-axis. in this case it's branch length
x_attr=lambda k: k.height

# plot the tree with thin branches
myTree.plotTree(ax, x_attr=x_attr, colour='black', width=0.1) ## tree
# myTree.plotPoints(ax, x_attr=x_attr, size=20, colour='w', zorder=100) ## tips
ax.plot()

ax.set_ylim(-1, myTree.ySpan + 1)
ax.set_xlim(0, 0.0018)

ax.set_yticks([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_xticklabels([])
# [ax.spines[loc].set_visible(False) for loc in ax.spines if loc not in ['bottom']]
[ax.spines[loc].set_visible(False) for loc in ax.spines]
# ax.spines['bottom'].set_position(("outward", 20))

col_pal = sns.color_palette()

col_dict = {"Wales/ALDP-11CF93B/2021": col_pal[0],
            "Wales/ALDP-125C4D7/2021": col_pal[0],
            "Wales/LIVE-DFCFFE/2021": col_pal[0],
            "Wales/ALDP-130BB95/2021": col_pal[0],
            "England/QEUH-CCCB30/2020": col_pal[1],
            "England/QEUH-CD0F1F/2020": col_pal[1],
            "England/MILK-1166F52/2021": col_pal[2],
            "England/MILK-11C95A6/2021": col_pal[2],
            "England/QEUH-109B25C/2021": col_pal[2],
            "England/MILK-126FE1F/2021": col_pal[3],
            "England/RAND-12671E1/2021": col_pal[3],
            "England/RAND-128FA33/2021": col_pal[3],
            "England/CAMC-CBA018/2020": col_pal[4],
            "England/CAMC-CB7AB3/2020": col_pal[5],
            "England/MILK-103C712/2021": col_pal[6],
            "Scotland/QEUH-1067DEF/2021": col_pal[7]}

def get_tip_colour(tipname, d):

    if tipname.split("|")[0] in d:
        col = d[tipname.split("|")[0]]
    else:
        col = "black"

    return col

def get_tip_size(tipname):
    r = set(["England/CAMC-CBA018/2020",
                "Wales/ALDP-11CF93B/2021",
                "Wales/ALDP-125C4D7/2021",
                "Wales/LIVE-DFCFFE/2021",
                "England/CAMC-CBA018/2020",
                "England/QEUH-CCCB30/2020",
                "England/QEUH-CD0F1F/2020",
                "England/MILK-1166F52/2021",
                "England/MILK-11C95A6/2021",
                "England/QEUH-109B25C/2021",
                "England/MILK-126FE1F/2021",
                "England/RAND-12671E1/2021",
                "England/RAND-128FA33/2021",
                "England/CAMC-CB7AB3/2020",
                "England/MILK-103C712/2021",
                "Scotland/QEUH-1067DEF/2021",
                "Wales/ALDP-130BB95/2021"])

    if tipname.split("|")[0] in r:
        size = 40
    else:
        size = 0

    return size

point_dict = {"Wales/ALDP-11CF93B/2021|L": "o",
            "Wales/ALDP-125C4D7/2021|L": "o",
            "Wales/LIVE-DFCFFE/2021|L": "o",
            "Wales/ALDP-130BB95/2021|L": "o",
            "England/QEUH-CCCB30/2020|L": "o",
            "England/QEUH-CD0F1F/2020|L": "o",
            "England/MILK-1166F52/2021|L": "^",
            "England/MILK-11C95A6/2021|L": "^",
            "England/QEUH-109B25C/2021|L": "^",
            "England/MILK-126FE1F/2021|L": "o",
            "England/RAND-12671E1/2021|L": "o",
            "England/RAND-128FA33/2021|L": "o",
            "England/CAMC-CBA018/2020|L": "o",
            "England/CAMC-CB7AB3/2020|L": "o",
            "England/MILK-103C712/2021|L": "o",
            "Scotland/QEUH-1067DEF/2021|L": "^",
            "Wales/ALDP-11CF93B/2021|R": "^",
            "Wales/ALDP-125C4D7/2021|R": "^",
            "Wales/LIVE-DFCFFE/2021|R": "^",
            "Wales/ALDP-130BB95/2021|R": "^",
            "England/QEUH-CCCB30/2020|R": "^",
            "England/QEUH-CD0F1F/2020|R": "^",
            "England/MILK-1166F52/2021|R": "o",
            "England/MILK-11C95A6/2021|R": "o",
            "England/QEUH-109B25C/2021|R": "o",
            "England/MILK-126FE1F/2021|R": "^",
            "England/RAND-12671E1/2021|R": "^",
            "England/RAND-128FA33/2021|R": "^",
            "England/CAMC-CBA018/2020|R": "^",
            "England/CAMC-CB7AB3/2020|R": "^",
            "England/MILK-103C712/2021|R": "^",
            "Scotland/QEUH-1067DEF/2021|R": "o"}

# colour the recombinant tips
c_func = lambda k: get_tip_colour(k.name, col_dict) ## colour according to which recombinant it is
s_func = lambda k: get_tip_size(k.name)
myTree.plotDifferentPoints(ax, point_dict=point_dict, x_attr=x_attr, size=s_func, colour=c_func, zorder=100, outline_size=0) ## tips

group_dict = collections.OrderedDict([("QEUH-1067DEF", col_pal[7]),
                                        ("MILK-103C712", col_pal[6]),
                                        ("CAMC-CB7AB3", col_pal[5]),
                                        ("CAMC-CBA018", col_pal[4]),
                                        ("Group D", col_pal[3]),
                                        ("Group C", col_pal[2]),
                                        ("Group B", col_pal[1]),
                                        ("Group A", col_pal[0])])

# make a legend
ylims = ax.get_ylim()
xlims = ax.get_xlim()

xs = []
ys = []
ms = []
cs = []
ts = []
for i,item in enumerate(group_dict.items()):
    x = xlims[0] + ((xlims[1] - xlims[0]) / 10)
    y = ylims[0] + ((ylims[1] - ylims[0]) / 12)
    xs.append(x)
    ys.append(y + ((ylims[1] - ylims[0]) / 70) * i)
    ms.append("^")
    cs.append([item[1]])
    xs.append(x + ((xlims[1] - xlims[0]) / 25))
    ys.append(y + ((ylims[1] - ylims[0]) / 70) * i)
    ms.append("o")
    cs.append([item[1]])

    ts.append((item[0], x + 2 * ((xlims[1] - xlims[0]) / 25), y + ((ylims[1] - ylims[0]) / 70) * i))

for i,j,m,c in zip(xs,ys,ms,cs):
    plt.scatter(i,j,marker=m,c=c)

for i,t in enumerate(ts):
    plt.text(s = t[0], x = t[1], y = t[2], fontsize = 6, verticalalignment = "center")

plt.text(s = "B.1.1.7", x = xlims[0] + ((xlims[1] - xlims[0]) / 10), y = ylims[0] + ((ylims[1] - ylims[0]) / 12) + (((ylims[1] - ylims[0]) / 70) * 8), fontsize = 6, rotation = 90.0, ha = "center", va = "bottom")
plt.text(s = "other", x = xlims[0] + ((xlims[1] - xlims[0]) / 10) + ((xlims[1] - xlims[0]) / 25), y = ylims[0] + ((ylims[1] - ylims[0]) / 12) + (((ylims[1] - ylims[0]) / 70) * 8), fontsize = 6, rotation = 90.0, ha = "center", va = "bottom")

plt.savefig("figure_BACKGROUNDTREE.svg", bbox_inches='tight', transparent=True)
plt.savefig("figure_BACKGROUNDTREE.png", bbox_inches='tight')






















#
