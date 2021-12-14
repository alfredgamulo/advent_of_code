import sys
from collections import defaultdict

lines = map(str.strip, sys.stdin.read().split("\n\n"))
templ = next(lines)
arrow = " -> "
rules = {r.split(arrow)[0]: r.split(arrow)[1] for r in next(lines).split("\n")}

polymer = templ
for _ in range(10):
    new_poly = polymer[0]
    for a, b in zip(polymer, polymer[1:]):
        new_poly += rules[a + b] + b
    polymer = new_poly
    pairs = defaultdict(int)
    for a,b in zip(polymer,polymer[1:]):
        pairs[a+b] += 1

counter = defaultdict(int)
for p in polymer:
    counter[p] += 1

print("Part 1:", max(counter.values()) - min(counter.values()))

# try something messy clean up later
polymer = templ
pairs = defaultdict(int)
for a,b in zip(polymer,polymer[1:]):
    pairs[a+b] += 1

for _ in range(40):
    newpairs = defaultdict(int)
    for k,v in pairs.items():
        if v > 0:
            newpairs[k[0]+rules[k]] += v-1 + 1
            newpairs[rules[k]+k[1]] += v -1 + 1
    
    pairs = newpairs

counter = defaultdict(int)
for k,v in pairs.items():
    counter[k[0]] += v
    counter[k[1]] += v

print("Part 2:", (max(counter.values()) - min(counter.values()) + 1 )//2)
