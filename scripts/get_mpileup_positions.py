import sys
import pysam

bamfile = sys.argv[1]
snpfile = sys.argv[2]
outfile = sys.argv[3]

snplist = []
with open(snpfile, "r") as f:
    for line in f:
        l = line.rstrip()
        ref = l[0]
        alt = l[-1]
        pos = int(l[1:-1])
        t = (pos, ref, alt)
        snplist.append(t)

snplist.sort(key = lambda x: x[0])

bam = pysam.AlignmentFile(bamfile, 'r')
ref = bam.header['SQ'][0]['SN']

with open(outfile, "w") as f:
    for t in snplist:
        f.write(ref + "\t" + str(t[0]) + "\n")
