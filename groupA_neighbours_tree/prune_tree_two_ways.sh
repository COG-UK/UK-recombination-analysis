sed -i.bak "s/'//g" HKY.treefile

echo "taxon" > neighbours.ids.txt
cat R.ids.txt L.ids.txt >> neighbours.ids.txt

echo "taxon" > recombs.ids.txt
grep "^>" ../groupA_transmission/groupA_PlusTransmission.fasta | cut -d">" -f2 >> recombs.ids.txt

jclusterfunk prune \
  -i HKY.treefile \
  -f newick \
  -o recombs.treefile \
  --taxon-file neighbours.ids.txt

jclusterfunk prune \
  -i HKY.treefile \
  -f newick \
  -o neighbours.treefile \
  --taxon-file recombs.ids.txt
