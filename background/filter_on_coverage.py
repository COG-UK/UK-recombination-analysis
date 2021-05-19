from Bio import SeqIO
import csv
import sys

al_f = sys.argv[1]
cov_f = sys.argv[2]

al_in = SeqIO.index(al_f, "fasta")

with open(cov_f, 'r', newline = '') as csv_in:

    reader = csv.DictReader(csv_in, delimiter="\t", quotechar='\"', dialect = "unix")

    for row in reader:
        if float(row["coverage"]) < 0.9835:
            continue
        seq_rec = al_in[row["sequence_name"]]
        print(">" + seq_rec.id)
        print(str(seq_rec.seq))
