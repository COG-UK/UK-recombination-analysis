for FOL in groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF
do
  python3 lineage_freq_plots.py ${FOL}/metadata.csv ${FOL}/startdate.txt ${FOL}/plot.pdf ${FOL}
done
