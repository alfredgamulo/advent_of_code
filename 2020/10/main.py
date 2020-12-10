from collections import Counter, defaultdict
from itertools import combinations
import time
start_time = time.time()

with open("input") as f:
    joltages = list(sorted(map(int, f.readlines()), reverse=True)) + [0]

c = Counter(x-y for x, y in zip(joltages, joltages[1:]))
print("Part 1:", c[1]*(c[3]+1))

d = defaultdict(list)
for x, y in combinations(joltages, 2):
    if x - y <= 3:
        d[y].append(x)

branch_count = defaultdict(lambda: 1)
for k, values in d.items(): 
    branch_count[k] = sum(branch_count[v] for v in values)

print("Part 2:", branch_count.get(0))
print("--- %s seconds ---" % (time.time() - start_time))
