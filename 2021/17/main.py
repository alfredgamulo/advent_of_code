import sys
import math
from itertools import product

(ax, zx), (ay, zy) = (
    sorted([int(c.split("..")[0].split("=")[-1]), int(c.split("..")[1])])
    for c in sys.stdin.readline().split(":")[1].strip().split(",")
)
minx = math.floor(math.sqrt(ax * 2))
y = abs(ay + 1)

print("Part 1:", (y * (y + 1) // 2))

initial_velocities = set()
for x, y in product(range(minx, zx + 1), range(ay, abs(ay) + 1)):
    xp = 0
    yp = 0
    s = 0
    while xp < ax or yp > zy:
        xp = xp + (x - (1 * s) if x - (1 * s) > 0 else 0)
        yp = yp + (y - (1 * s))
        s += 1
    if ax <= xp <= zx and ay <= yp <= zy:
        initial_velocities.add((x, y))

print("Part 2:", len(initial_velocities))
