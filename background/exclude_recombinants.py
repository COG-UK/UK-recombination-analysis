from Bio import SeqIO

excluded = set(["England/CAMC-CBA018/2020",
                "Wales/ALDP-11CF93B/2021",
                "Wales/ALDP-125C4D7/2021",
                "Wales/LIVE-DFCFFE/2021",
                "England/CAMC-CB7AB3/2020",
                "England/QEUH-CCCB30/2020",
                "England/QEUH-CD0F1F/2020",
                "England/MILK-1166F52/2021",
                "England/MILK-11C95A6/2021",
                "England/QEUH-109B25C/2021",
                "England/MILK-126FE1F/2021",
                "England/RAND-12671E1/2021",
                "England/RAND-128FA33/2021",
                "England/CAMC-CB7AB3/2020",
                "England/MILK-103C712/2021",
                "Scotland/QEUH-1067DEF/2021",
                "Wales/ALDP-130BB95/2021"])

with open("cog_2021-03-07_all_alignment.fa", "r") as fin, open("cog_2021-03-07_all_alignment_norecomb.fa", "w") as fout:
    for record in SeqIO.parse(fin, "fasta"):
        if record.id in excluded:
            continue
        fout.write(">" + record.id + "\n")
        fout.write(str(record.seq) + "\n")
