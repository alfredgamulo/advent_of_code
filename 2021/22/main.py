import sys
from pprint import PrettyPrinter
from itertools import product
from contextlib import suppress


pp = PrettyPrinter(indent=2)

lines = sys.stdin.readlines()
directions = []
for line in lines:
    toggle, coords = line.split()
    x, y, z = (eval(c[2:].replace("..", ",")) for c in coords.split(","))
    directions.append((toggle == "on", x, y, z))


cubes = set()
for (on, x, y, z) in directions:
    x1, y1, z1 = max(-50, x[0]), max(-50, y[0]), max(-50, z[0])
    x2, y2, z2 = min(50, x[1]) + 1, min(50, y[1]) + 1, min(50, z[1]) + 1
    if on:
        for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
            cubes.add((cx, cy, cz))
    else:
        for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
            with suppress(KeyError):
                cubes.remove((cx, cy, cz))

print("Part 1:", len(cubes))
