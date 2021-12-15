import sys

line = sys.stdin.read().strip()

print("Part 1:", sum([1 if l == "(" else -1 for l in line]))

floor = 0
for i, l in enumerate(line):
    if l == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print("Part 2:", i + 1)
        exit()
