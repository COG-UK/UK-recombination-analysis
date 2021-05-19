mkdir -p groupA groupB groupC groupD CAMC-CB7AB3 MILK-103C712 QEUH-1067DEF

python3 ../scripts/mask.py -i ../recombinant_genomes/groupA.fasta -m 21765-29903 > groupA/groupA.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 21765-29903 > groupA/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupA.fasta -m 1-21764 > groupA/groupA.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-21764 > groupA/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupB.fasta -m 6953-29903 > groupB/groupB.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 6953-29903 > groupB/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupB.fasta -m 1-6952 > groupB/groupB.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-6952 > groupB/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupC.fasta -m 24917-29903 > groupC/groupC.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 24917-29903 > groupC/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupC.fasta -m 1-24916 > groupC/groupC.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-24916 > groupC/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/groupD.fasta -m 23066-29903 > groupD/groupD.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 23066-29903 > groupD/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/groupD.fasta -m 1-23065 > groupD/groupD.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-23065 > groupD/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CB7AB3.fasta -m 1-3268 21765-29903 > CAMC-CB7AB3/CAMC-CB7AB3.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-3268 21765-29903 > CAMC-CB7AB3/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/CAMC-CB7AB3.fasta -m 3269-21764 > CAMC-CB7AB3/CAMC-CB7AB3.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 3269-21764 > CAMC-CB7AB3/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/MILK-103C712.fasta -m 27972-29903 > MILK-103C712/MILK-103C712.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 27972-29903 > MILK-103C712/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/MILK-103C712.fasta -m 1-27971 > MILK-103C712/MILK-103C712.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-27971 > MILK-103C712/background.R.fasta

python3 ../scripts/mask.py -i ../recombinant_genomes/QEUH-1067DEF.fasta -m 6956-29903 > QEUH-1067DEF/QEUH-1067DEF.L.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 6956-29903 > QEUH-1067DEF/background.L.fasta
python3 ../scripts/mask.py -i ../recombinant_genomes/QEUH-1067DEF.fasta -m 1-6955 > QEUH-1067DEF/QEUH-1067DEF.R.fasta
python3 ../scripts/mask.py -i ../background/date_filtered.cov_filtered.fasta -m 1-6955 > QEUH-1067DEF/background.R.fasta
