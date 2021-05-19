cp groupA_PlusTransmission.fasta tree.fasta

tail -n+2 ../mask_2/groupA/L.closest.csv | cut -d"," -f2 | cut -d";" -f 1-20 | tr ";" "\n" | sort | uniq > L.IDs.txt
tail -n+2 ../mask_2/groupA/R.closest.csv | cut -d"," -f2 | cut -d";" -f 1-20 | tr ";" "\n" | sort | uniq > R.IDs.txt

python3 ../scripts/get_fasta_from_IDs.py ../background/date_filtered.cov_filtered.fasta L.IDs.txt >> tree.fasta
python3 ../scripts/get_fasta_from_IDs.py ../background/date_filtered.cov_filtered.fasta R.IDs.txt >> tree.fasta

cat ../background/MN908947.fa >> tree.fasta
