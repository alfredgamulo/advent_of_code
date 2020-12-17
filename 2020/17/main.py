import time as timer
start_time = timer.time()
from collections import Counter
import itertools

with open("input") as f:
    lines = f.read().splitlines()

# Part 1
cubes = set()
for i, row in enumerate(lines):
    for j,col in enumerate(row):
        if col == "#":
            cubes.add((i, j, 0))

neighbors = set(itertools.product((-1, 0, 1), repeat=3)) - set([(0,0,0)])

for _ in range(6):
    touched = Counter(tuple(sum(z) for z in zip(c,n)) for c in cubes for n in neighbors)
    cubes = set(c for c in cubes if touched[c] in (2,3)) | set(c for c in touched if touched[c] == 3)

print("Part 1:", len(cubes))

# Part 2
cubes = set()
for i, row in enumerate(lines):
    for j,col in enumerate(row):
        if col == "#":
            cubes.add((i, j, 0, 0))

neighbors = set(itertools.product((-1, 0, 1), repeat=4)) - set([(0,0,0,0)])

for _ in range(6):
    touched = Counter(tuple(sum(z) for z in zip(c,n)) for c in cubes for n in neighbors)
    cubes = set(c for c in cubes if touched[c] in (2,3)) | set(c for c in touched if touched[c] == 3)

print("Part 2:", len(cubes))

print("--- %s millis ---" % ((timer.time() - start_time)*1000))
