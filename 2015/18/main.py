import sys
from itertools import product

lights = set()
lenx = leny = 0
for i, line in enumerate(sys.stdin.readlines()):
    lenx = max(i, lenx)
    for j, c in enumerate(line.strip()):
        leny = max(i, leny)
        if c == "#":
            lights.add((i, j))

neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def part1(lights):
    for _ in range(100):
        new_lights = set()
        for x1, y1 in product(range(lenx + 1), range(leny + 1)):
            count = 0
            for (x2, y2) in neighbors:
                count += (x1 + x2, y1 + y2) in lights
            if (x1, y1) in lights and count in (2, 3):
                new_lights.add((x1, y1))
            elif (x1, y1) not in lights and count == 3:
                new_lights.add((x1, y1))
        lights = new_lights
    return len(lights)


def part2(lights):
    lights.add((0, 0))
    lights.add((lenx, 0))
    lights.add((0, leny))
    lights.add((lenx, leny))
    for _ in range(100):
        new_lights = set()
        for x1, y1 in product(range(lenx + 1), range(leny + 1)):
            count = 0
            for (x2, y2) in neighbors:
                count += (x1 + x2, y1 + y2) in lights
            if (x1, y1) in lights and count in (2, 3):
                new_lights.add((x1, y1))
            elif (x1, y1) not in lights and count == 3:
                new_lights.add((x1, y1))
        lights = new_lights
        lights.add((0, 0))
        lights.add((lenx, 0))
        lights.add((0, leny))
        lights.add((lenx, leny))
    return len(lights)


print("Part 1:", part1(lights))
print("Part 2:", part2(lights))
