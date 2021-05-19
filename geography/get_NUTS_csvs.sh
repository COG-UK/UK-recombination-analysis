mkdir -p groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF

for FOL in groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF
do
  python3 get_NUTS.py ../mask_2/${FOL}/queries ../background/cog_global_2021-03-07.csv ${FOL}/metadata.csv ${FOL}/startdate.txt
done
