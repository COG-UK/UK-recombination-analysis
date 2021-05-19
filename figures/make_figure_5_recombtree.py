import sys
import csv
# import collections
import seaborn as sns
# import matplotlib as mpl
from matplotlib import pyplot as plt
# from matplotlib import lines as mplines

sys.path.append('/Users/ben/programs/baltic/baltic')
import baltic as bt

recombsTree = bt.loadNewick("../groupA_neighbours_tree/recombs.treefile", absoluteTime=False)
recombsTree.traverse_tree()
recombsTree.sortBranches()

# a map from tip to epiweek
tip_2_epiweek = {}
with open("../recombinant_genomes/recombs.dates.csv", 'r', newline = '') as csv_in:
    reader = csv.DictReader(csv_in, delimiter=",", quotechar='\"', dialect = "unix")
    for row in reader:
        tip_2_epiweek[row["sequence_name"]] = int(row["epi_week"])

# fudge the reference
tip_2_epiweek["MN908947.3"] = 0

collist = [x for x in range(49, 67, 1)]

# a diverging colour palette:
numcols = len(collist)
div_col_pal = sns.diverging_palette(240, 10, n=numcols)

# make a map from all the levels of epi week (except the reference seq) to a colour
col_map = {}
for week, col in zip(collist, div_col_pal):
    col_map[week] = col

# fudge the reference's epiweek
col_map[0] = (1, 1, 1)

# a function literal to assign tip colour by epiweek
tip_col = lambda k: col_map[tip_2_epiweek[k.name]]

# figure, axis
fig, ax = plt.subplots(figsize=(5,5), dpi = 300)

# what to plot on the x-axis. in this case it's branch length
x_attr = lambda k: k.height
x_attr_text = lambda k: k.height + 0.00003

# tipname lambda
tip_name = lambda k: k.name.split("/")[0] if k.name[0:2] == "MN" else k.name.split("/")[1]

# plot the first tree with thin branches
recombsTree.plotTree(ax, x_attr = x_attr, colour = 'black', width = 0.5) ## tree
recombsTree.addText(ax, x_attr = x_attr_text, text = tip_name, color = "gray", size = 6, va = "center") ## tips labelled with epiweek
recombsTree.plotPoints(ax, x_attr = x_attr, size = 20, colour = tip_col, zorder = 100, outline = False) ## tips
ax.plot()

ax.set_ylim(-1, recombsTree.ySpan + 1)
ax.set_xlim(0, 0.0015)

ax.set_yticks([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_xticklabels([])
[ax.spines[loc].set_visible(False) for loc in ax.spines]

plt.savefig("figure_GROUPA_recombstree.svg", bbox_inches = 'tight', transparent = True)
plt.savefig("figure_GROUPA_recombstree.png", bbox_inches = 'tight')

# a legend?
sns.palplot(div_col_pal)

plt.savefig("figure_GROUPA_key.svg", bbox_inches = 'tight', transparent = True)
plt.savefig("figure_GROUPA_key.png", bbox_inches = 'tight')








#
