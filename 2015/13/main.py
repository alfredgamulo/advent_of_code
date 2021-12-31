import sys
from itertools import permutations
from collections import defaultdict


lines = sys.stdin.readlines()
names = set()
refer = defaultdict(int)
for line in lines:
    first, _, gol, cost, *_, second = line.split()
    happiness = int(cost)
    if gol == "lose":
        happiness *= -1
    names.add(first)
    second = second.strip(".")
    names.add(second)
    refer[(first, second)] = happiness


def find_happinesss(names):
    happiest = -1
    for p in permutations(names):
        (lp := (list(p))).append(p[0])
        happiness = 0
        for left, right in zip(lp, lp[1:]):
            happiness += refer[(left, right)] + refer[(right, left)]
        happiest = max(happiness, happiest)
    return happiest


print("Part 1:", find_happinesss(names))
names.add("me")
print("Part 2:", find_happinesss(names))
