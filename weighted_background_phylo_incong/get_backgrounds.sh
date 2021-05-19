
cat ../background/MN908947.fa ../recombinant_genomes/groupA.2.fasta ../weighted_background/sample.2000.fasta > groupA.temp.fasta
python3 ../scripts/mask.py -i groupA.temp.fasta -m 21256-29903 > groupA.L.fasta
python3 ../scripts/mask.py -i groupA.temp.fasta -m 1-21764 > groupA.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/groupB.fasta ../weighted_background/sample.2000.fasta > groupB.temp.fasta
python3 ../scripts/mask.py -i groupB.temp.fasta -m 6529-29903 > groupB.L.fasta
python3 ../scripts/mask.py -i groupB.temp.fasta -m 1-6953 > groupB.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/groupC.fasta ../weighted_background/sample.2000.fasta > groupC.temp.fasta
python3 ../scripts/mask.py -i groupC.temp.fasta -m 24915-29903 > groupC.L.fasta
python3 ../scripts/mask.py -i groupC.temp.fasta -m 1-28650 > groupC.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/groupD.fasta ../weighted_background/sample.2000.fasta > groupD.temp.fasta
python3 ../scripts/mask.py -i groupD.temp.fasta -m 21576-29903 > groupD.L.fasta
python3 ../scripts/mask.py -i groupD.temp.fasta -m 1-23062 > groupD.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/CAMC-CBA018.fasta ../weighted_background/sample.2000.fasta > CAMC-CBA018.temp.fasta
python3 ../scripts/mask.py -i CAMC-CBA018.temp.fasta -m 11397-29903 > CAMC-CBA018.L.fasta
python3 ../scripts/mask.py -i CAMC-CBA018.temp.fasta -m 1-21764 > CAMC-CBA018.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/CAMC-CB7AB3.fasta ../weighted_background/sample.2000.fasta > CAMC-CB7AB3.temp.fasta
python3 ../scripts/mask.py -i CAMC-CB7AB3.temp.fasta -m 1-6285 12535-29903 > CAMC-CB7AB3.L.fasta
python3 ../scripts/mask.py -i CAMC-CB7AB3.temp.fasta -m 3268-21764 > CAMC-CB7AB3.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/MILK-103C712.fasta ../weighted_background/sample.2000.fasta > MILK-103C712.temp.fasta
python3 ../scripts/mask.py -i MILK-103C712.temp.fasta -m 26802-29903 > MILK-103C712.L.fasta
python3 ../scripts/mask.py -i MILK-103C712.temp.fasta -m 1-27971 > MILK-103C712.R.fasta

cat ../background/MN908947.fa ../recombinant_genomes/QEUH-1067DEF.fasta ../weighted_background/sample.2000.fasta > QEUH-1067DEF.temp.fasta
python3 ../scripts/mask.py -i QEUH-1067DEF.temp.fasta -m 6955-29903 > QEUH-1067DEF.L.fasta
python3 ../scripts/mask.py -i QEUH-1067DEF.temp.fasta -m 1-10869 > QEUH-1067DEF.R.fasta

rm *temp*
