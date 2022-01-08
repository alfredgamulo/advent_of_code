import sys
from itertools import combinations
from collections import defaultdict

containers = list(map(int, sys.stdin.readlines()))

combos = defaultdict(int)
for r in range(len(containers)):
    for combo in combinations(containers, r):
        if sum(combo) == 150:
            combos[len(combo)] += 1

print("Part 1:", sum(combos.values()))
print("Part 2:", combos[min(combos)])
