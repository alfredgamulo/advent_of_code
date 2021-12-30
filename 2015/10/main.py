import sys
from itertools import groupby

line = sys.stdin.read().strip()


def solve(iters, line):
    s = line
    for i in range(iters):
        s = "".join(str(len(list(v))) + k for k, v in groupby(s))
    return s


part1 = solve(40, line)
print("Part 1:", len(part1), flush=True)

part2 = solve(50, line)
print("Part 2:", len(part2))
