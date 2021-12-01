import sys

input = sys.argv[1]

with open(input) as f:
    lines = list(map(int, f.read().splitlines()))

print("Part 1: ", sum([1 for x, y in zip(lines, lines[1:]) if y > x]))

windows = list(map(sum, zip(lines, lines[1:], lines[2:])))
print("Part 2: ", sum([1 for x, y in zip(windows, windows[1:]) if y > x]))
