from collections import Counter
from itertools import combinations
import time
start_time = time.time()

with open("input") as f:
    joltages = list(sorted(map(int, f.readlines()), reverse=True)) + [0]

c = Counter(x-y for x, y in zip(joltages, joltages[1:]))
print("Part 1:", c[1]*(c[3]+1))

d = {}
for x, y in combinations(joltages, 2):
    if x - y <= 3:
        d.setdefault(y, []).append(x)

branch_count = {}
for k, values in d.items(): 
    branch_count[k] = sum(branch_count.get(v, 1) for v in values)

print("Part 2:", branch_count.get(0))
print("--- %s seconds ---" % (time.time() - start_time))
