import sys

lines = list(map(int, sys.stdin.readlines()))


def count_increasing(depths):
    return sum([1 for x, y in zip(depths, depths[1:]) if y > x])


print("Part 1: ", count_increasing(lines))

windows = list(map(sum, zip(lines, lines[1:], lines[2:])))
print("Part 2: ", count_increasing(windows))
