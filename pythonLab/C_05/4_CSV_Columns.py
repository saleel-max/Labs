import csv

filename = input("Enter CSV file name: ")
cols = input("Enter column numbers to read (comma-separated, starting from 0): ")

cols = [int(c.strip()) for c in cols.split(",")]

with open(filename, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        selected = [row[i] for i in cols]
        print(selected)
