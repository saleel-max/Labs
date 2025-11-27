import csv

filename = input("Enter CSV file name: ")

with open(filename, newline="") as f:
    reader = csv.reader(f)
        for row in reader:
            print(row)
