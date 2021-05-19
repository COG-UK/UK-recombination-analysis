from Bio import SeqIO
import sys

al = sys.argv[1]
snps = sys.argv[2]

snpset = set()
with open(snps, "r") as f:
    for line in f:
        l = line.strip()
        snpset.add(int(l[1:len(l) - 1]))

with open(al, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        printrec = True
        for snppos in snpset:
            if record.seq[snppos - 1] not in ["A", "T", "G", "C"]:
                printrec = False
                break

        if printrec:
            print(">" + record.id)
            print(str(record.seq))
