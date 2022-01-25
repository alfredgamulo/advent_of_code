import sys
from itertools import combinations
from math import prod

packages = list(map(int, sys.stdin.readlines()))


def balance(groups):
    weight = sum(packages) // groups
    for s in range(2, len(packages) - 1):
        for c in combinations(packages, s):
            if sum(c) == weight:
                return prod(c)


print("Part 1:", balance(3))
print("Part 2:", balance(4))
