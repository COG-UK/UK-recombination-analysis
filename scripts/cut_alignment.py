from Bio import SeqIO
import sys

al = sys.argv[1]
start = int(sys.argv[2])
stop = int(sys.argv[3])

with open(al, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        print(">" + record.id)
        print(str(record.seq)[(start - 1):(stop)])
