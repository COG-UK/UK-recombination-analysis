import sys

pileupfile = sys.argv[1]

def get_allele_counts(string):
    """
    parse the pileup basecalls column to get naive (!) allele counts

    returns d: a dict of ACGT allele counts
    """
    d = {"A": 0, "C": 0, "G": 0, "T": 0}

    for s in string:
        s = s.upper()
        if s in d.keys():
            d[s] += 1

    return d

print("pos\tA\tT\tG\tC")

with open(pileupfile, "r") as f:
    for line in f:
        l = line.rstrip().split("\t")
        AC_dict = get_allele_counts(l[4])
        print("\t".join([l[1], str(AC_dict["A"]), str(AC_dict["T"]), str(AC_dict["G"]), str(AC_dict["C"])]))
