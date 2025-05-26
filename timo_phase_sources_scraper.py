import csv
from collections import Counter

# 1) Export each search result from PoP as “pop_export.csv” with a “Source” column.
# 2) Merge all three exports into one file or process one at a time.

counter = Counter()
with open('pop_export.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        src = row.get('Source', '').strip()
        if src:
            counter[src] += 1

# Print journals/reports sorted by frequency
for src, count in counter.most_common():
    print(f"{count:3d} – {src}")
