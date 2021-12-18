import sys
import math
from itertools import product

(ax, zx), (ay, zy) = (
    sorted([int(c.split("..")[0].split("=")[-1]), int(c.split("..")[1])])
    for c in sys.stdin.readline().split(":")[1].strip().split(",")
)

print("Part 1:", ay *-~ ay >> 1)

counter = 0
minx = math.floor(math.sqrt(ax * 2))
for x, y in product(range(minx, zx + 1), range(ay, abs(ay) + 1)):
    xp = yp = s = 0
    while xp < ax or yp > zy:
        xp += x - s if x - s > 0 else 0
        yp += y - s
        s += 1
    counter += ax <= xp <= zx and ay <= yp <= zy

print("Part 2:", counter)
