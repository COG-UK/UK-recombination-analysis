from Bio import SeqIO
import argparse
import sys


def parse_mask(mask_list):
    l = []
    for x in mask_list:
        temp = x.split("-")
        if len(temp) == 1:
            l.append((int(temp[0]) - 1, int(temp[0])))
        else:
            l.append((int(temp[0]) - 1, int(temp[1])))

    return l


def mask(infile, mask_list):
    mask = parse_mask(mask_list)

    with open(infile, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            start = 0
            seq = str(record.seq)
            new_seq = ""
            for maskblock in mask:
                new_seq = new_seq + seq[start:maskblock[0]] + ("N" * (maskblock[1] - maskblock[0]))
                start = maskblock[1]

            if start < len(seq):
                new_seq = new_seq + seq[start:]

            print(">" + record.id)
            print(new_seq)

    pass


def parse_args():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--infile', "-i", help="infile")
    parser.add_argument('--mask', "-m", nargs='+')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    mask(infile = args.infile, mask_list = args.mask)
