source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f1, open(destination, "w") as f2:
    for i, line in enumerate(f1, start=1):
        if i % 2 == 1:
            f2.write(line)
