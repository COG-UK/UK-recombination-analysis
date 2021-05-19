import csv

neighbours = set()
recombs = set()

with open("neighbours.ids.txt", "r") as f:
    for line in f:
        l = line.strip()
        neighbours.add(l)

with open("recombs.ids.txt", "r") as f:
    for line in f:
        l = line.strip()
        recombs.add(l)

with open("../background/date_filtered.csv", 'r', newline = '') as csv_in, \
    open("neighbours.dates.csv", 'w', newline = '') as csv_out:

    reader = csv.DictReader(csv_in, delimiter=",", quotechar='\"', dialect = "unix")
    writer = csv.DictWriter(csv_out, fieldnames = ["sequence_name", "sample_date", "epi_week"], delimiter=",", quotechar='\"', quoting=csv.QUOTE_MINIMAL, dialect = "unix")
    writer.writeheader()

    for row in reader:
        if row["sequence_name"] in neighbours:
            writer.writerow({x: row[x] for x in writer.fieldnames})
