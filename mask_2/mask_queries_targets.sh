mkdir -p groupA groupB groupC groupD CAMC-CBA018 CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF

python3 ../scripts/mask.py -i ../recombinant_genomes/groupA.2.fasta -m 21256-29903 > groupA/groupA.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 21256-29903 > groupA/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupA.2.fasta -m 1-21764 > groupA/groupA.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-21764 > groupA/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupB.fasta -m 6529-29903 > groupB/groupB.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 6529-29903 > groupB/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupB.fasta -m 1-6953 > groupB/groupB.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-6953 > groupB/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupC.fasta -m 24915-29903 > groupC/groupC.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 24915-29903 > groupC/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupC.fasta -m 1-28650 > groupC/groupC.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-28650 > groupC/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupD.fasta -m 21576-29903 > groupD/groupD.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 21576-29903 > groupD/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupD.fasta -m 1-23062 > groupD/groupD.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-23062 > groupD/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CBA018.fasta -m 11397-29903 > CAMC-CBA018/CAMC-CBA018.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 11397-29903 > CAMC-CBA018/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CBA018.fasta -m 1-21764 > CAMC-CBA018/CAMC-CBA018.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-21764 > CAMC-CBA018/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CB7AB3.fasta -m 1-6285 12535-29903 > CAMC-CB7AB3/CAMC-CB7AB3.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-6285 12535-29903 > CAMC-CB7AB3/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CB7AB3.fasta -m 3268-21764 > CAMC-CB7AB3/CAMC-CB7AB3.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 3268-21764 > CAMC-CB7AB3/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/MILK-103C712.fasta -m 26802-29903 > MILK-103C712/MILK-103C712.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 26802-29903 > MILK-103C712/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/MILK-103C712.fasta -m 1-27971 > MILK-103C712/MILK-103C712.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-27971 > MILK-103C712/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/QEUH-1067DEF.fasta -m 6955-29903 > QEUH-1067DEF/QEUH-1067DEF.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 6955-29903 > QEUH-1067DEF/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/QEUH-1067DEF.fasta -m 1-10869 > QEUH-1067DEF/QEUH-1067DEF.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-10869 > QEUH-1067DEF/background.R.fasta
