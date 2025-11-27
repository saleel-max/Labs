import csv

data = [
    {"Name": "Alice", "Age": 23, "City": "London"},
    {"Name": "Bob", "Age": 30, "City": "New York"},
    {"Name": "Charlie", "Age": 29, "City": "Sydney"},
    {"Name": "Diana", "Age": 25, "City": "Toronto"}
]

filename = "output.csv"

with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

with open(filename, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
