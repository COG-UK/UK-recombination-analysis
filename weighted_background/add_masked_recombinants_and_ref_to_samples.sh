cat ../background/MN908947.fa sample.2000.fasta > sample.2000.ref.maskedrecombs.fasta

for FILE in ../mask_2/*/*.L.fasta
do
 cp $FILE temp
 sed -e '/^>/s/$/|L/g' temp > temp2
 cat temp2 >> sample.2000.ref.maskedrecombs.fasta
done

for FILE in ../mask_2/*/*.R.fasta
do
 cp $FILE temp
 sed -e '/^>/s/$/|R/g' temp > temp2
 cat temp2 >> sample.2000.ref.maskedrecombs.fasta
done

rm temp temp2
