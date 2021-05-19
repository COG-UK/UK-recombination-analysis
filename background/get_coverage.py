import sys
from Bio import SeqIO

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

input = sys.argv[1]

def strip_amb(s):
    s = s.replace("N", "")
    # s = s.replace("R", "")
    # s = s.replace("Y", "")
    # s = s.replace("S", "")
    # s = s.replace("W", "")
    # s = s.replace("K", "")
    # s = s.replace("M", "")
    # s = s.replace("B", "")
    # s = s.replace("D", "")
    # s = s.replace("H", "")
    # s = s.replace("V", "")

    return s

print("sequence_name\tcoverage")
with open(input, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        coverage = len(strip_amb(str(record.seq))) / len(record.seq)
        print(record.id + "\t" + str(round(coverage, 4)))
