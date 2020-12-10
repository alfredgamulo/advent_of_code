#! /usr/local/bin/python3

from collections import Counter
from itertools import combinations
import time
start_time = time.time()

joltages = [0]
with open("input") as f:
    joltages.extend(sorted(map(int, f.readlines())))

c = Counter(y-x for x, y in zip(joltages, joltages[1:]))
print("Part 1:", c[1]*(c[3]+1))

d = {}
for x, y in combinations(joltages, 2):
    if y - x <= 3:
        d.setdefault(x, []).append(y)

branch_count = {}
for k in reversed(d): 
    s = 0
    for v in d.get(k):
        s += branch_count.get(v, 1)
    branch_count[k] = s

print("Part 2:", branch_count.get(0))
print("--- %s seconds ---" % (time.time() - start_time))
