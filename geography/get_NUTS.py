import csv
import sys
import datetime

queries_in = sys.argv[1]
csv_in = sys.argv[2]
csv_out = sys.argv[3]


queries = set()
with open(queries_in, "r") as f:
    for line in f:
        queries.add(line.rstrip())

dates = []
with open(csv_in, 'r', newline = '') as f:
    reader = csv.DictReader(f, delimiter=",", quotechar='\"', dialect = "unix")
    for row in reader:
        if row["sequence_name"] in queries:
            dates.append(row["sample_date"])

min_date = datetime.datetime.strptime(min(dates), '%Y-%m-%d').date()
earliest_date = min_date - datetime.timedelta(28 + 3)
latest_date = min_date + datetime.timedelta(3)

print(dates)
print(min_date)
print(earliest_date)
print(latest_date)

with open(sys.argv[4], "w") as f:
    f.write(str(min_date - datetime.timedelta(28)) + "\n")

NUTS = set()
with open(csv_in, 'r', newline = '') as f:
    reader = csv.DictReader(f, delimiter=",", quotechar='\"', dialect = "unix")
    for row in reader:
        if row["sequence_name"] in queries:
            NUTS.add(row["NUTS1"])

print(NUTS)

with open(csv_in, 'r', newline = '') as f_in, \
    open(csv_out, 'w', newline = '') as f_out:

    reader = csv.DictReader(f_in, delimiter=",", quotechar='\"', dialect = "unix")
    writer = csv.DictWriter(f_out, fieldnames = reader.fieldnames, delimiter=",", quotechar='\"', quoting=csv.QUOTE_MINIMAL, dialect = "unix")
    writer.writeheader()

    for row in reader:
        date = datetime.datetime.strptime(row["sample_date"], '%Y-%m-%d').date()
        if date > latest_date:
            continue
        if date < earliest_date:
            continue
        if row["NUTS1"] in NUTS:
            writer.writerow(row)
