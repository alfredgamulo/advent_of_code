import sys
from math import sqrt
from itertools import product

(ax, zx), (ay, zy) = (
    [int(c.split("..")[0].split("=")[-1]), int(c.split("..")[1])]
    for c in sys.stdin.readline().split(":")[1].strip().split(",")
)

print("Part 1:", ay * -~ay >> 1)

counter = 0
minx = int(sqrt(ax << 1))
for x, y in product(range(minx, zx + 1), range(ay, abs(ay))):
    px = py = s = 0
    while px < ax or py > zy:
        px += x - s if x - s > 0 else 0
        py += y - s
        s += 1
    counter += px <= zx and ay <= py

print("Part 2:", counter)
