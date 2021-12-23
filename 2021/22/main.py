import sys
from dataclasses import dataclass
from itertools import product

lines = sys.stdin.readlines()
directions = []
for line in lines:
    toggle, coords = line.split()
    x, y, z = (eval(c[2:].replace("..", ",")) for c in coords.split(","))
    directions.append((toggle == "on", x, y, z))


@dataclass(frozen=True)
class Cuboid:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def size(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def subtract(a, b):
        if not (
            a.x1 < b.x2
            and a.x2 > b.x1
            and a.y1 < b.y2
            and a.y2 > b.y1
            and a.z1 < b.z2
            and a.z2 > b.z1
        ):
            yield a
        else:
            b = Cuboid(
                min(max(b.x1, a.x1), a.x2),
                min(max(b.x2, a.x1), a.x2),
                min(max(b.y1, a.y1), a.y2),
                min(max(b.y2, a.y1), a.y2),
                min(max(b.z1, a.z1), a.z2),
                min(max(b.z2, a.z1), a.z2),
            )

            yield Cuboid(a.x1, b.x1, a.y1, a.y2, a.z1, a.z2)
            yield Cuboid(b.x2, a.x2, a.y1, a.y2, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, a.y1, b.y1, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, b.y2, a.y2, a.z1, a.z2)
            yield Cuboid(b.x1, b.x2, b.y1, b.y2, a.z1, b.z1)
            yield Cuboid(b.x1, b.x2, b.y1, b.y2, b.z2, a.z2)


def reboot(directions, limiter):
    cubes = set()
    for (on, (x1, x2), (y1, y2), (z1, z2)) in directions:
        if limiter:
            x1, y1, z1 = max(-50, x1), max(-50, y1), max(-50, z1)
            x2, y2, z2 = min(50, x2) + 1, min(50, y2) + 1, min(50, z2) + 1
        if on:
            for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
                cubes.add((cx, cy, cz))
        else:
            for cx, cy, cz in product(range(x1, x2), range(y1, y2), range(z1, z2)):
                cubes.discard((cx, cy, cz))
    return len(cubes)


print("Part 1:", reboot(directions, 50), flush=True)


def reboot(directions):
    cubes = []
    for (on, (x1, x2), (y1, y2), (z1, z2)) in directions:
        cuboid = Cuboid(x1, x2 + 1, y1, y2 + 1, z1, z2 + 1)
        cubes = [sub for cube in cubes for sub in cube.subtract(cuboid) if sub.size()]
        if on:
            cubes.append(cuboid)
    return sum(map(Cuboid.size, cubes))


print("Part 2:", reboot(directions), flush=True)
