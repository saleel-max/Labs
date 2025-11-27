filename = input("Enter file name: ")

lines = []
with open(filename, "r") as f:
	for line in f:
		lines.append(line.rstrip("\n"))

print(lines)
