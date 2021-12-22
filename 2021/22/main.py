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


def reboot(limiter=0):
    cubes = set()
    for i, (on, x, y, z) in enumerate(directions):
        if limiter:
            x1, y1, z1 = max(-50, x[0]), max(-50, y[0]), max(-50, z[0])
            x2, y2, z2 = min(50, x[1]) + 1, min(50, y[1]) + 1, min(50, z[1]) + 1
        else:
            x1, y1, z1 = x[0], y[0], z[0]
            x2, y2, z2 = x[1] + 1, y[1] + 1, z[1] + 1
        if on:
            for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
                cubes.add((cx, cy, cz))
        else:
            for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
                cubes.discard((cx, cy, cz))
    return len(cubes)


print("Part 1:", reboot(50), flush=True)
print("Part 2:", reboot())
