import sys
from collections import defaultdict

lines = map(str.strip, sys.stdin.read().split("\n\n"))
templ = next(lines)
arrow = " -> "
rules = {r.split(arrow)[0]: r.split(arrow)[1] for r in next(lines).split("\n")}

polymer = templ
for _ in range(40):
    new_poly = polymer[0]
    for a, b in zip(polymer, polymer[1:]):
        new_poly += rules[a + b] + b
    polymer = new_poly

counter = defaultdict(int)
for p in polymer:
    counter[p] += 1

print("Part 1:", max(counter.values()) - min(counter.values()))
