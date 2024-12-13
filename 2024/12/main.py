

import sys
from collections import deque
from functools import cache
from pathlib import Path


def neighbors(coords, limit):
    r = []
    if 0 < coords[0] < limit:
        r.append((coords[0] - 1, coords[1]))
    if 0 <= coords[0] < limit - 1:
        r.append((coords[0] + 1, coords[1]))
    if 0 < coords[1] < limit:
        r.append((coords[0], coords[1] - 1))
    if 0 <= coords[1] < limit - 1:
        r.append((coords[0], coords[1] + 1))
    return r


def solve(coords):
    @cache
    def is_boundary(x, y):
        # Check if a point is a boundary point
        return (x - 1, y) not in coords or (x + 1, y) not in coords or (x, y - 1) not in coords or (x, y + 1) not in coords

    boundary_points = [point for point in coords if is_boundary(*point)]
    perimeter = 0
    sides = set()

    for x, y in boundary_points:
        if (x - 1, y) not in coords:
            perimeter += 1
            sides.add((x - 1, "vertical"))
        if (x + 1, y) not in coords:
            perimeter += 1
            sides.add((x + 1, "vertical"))
        if (x, y - 1) not in coords:
            perimeter += 1
            sides.add((y - 1, "horizontal"))
        if (x, y + 1) not in coords:
            perimeter += 1
            sides.add((y + 1, "horizontal"))

    return perimeter, len(sides)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    regions = list()
    visited = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if ((x, y)) in visited:
                continue
            new_region = set()
            search = deque([(x, y)])
            while search:
                sx, sy = search.popleft()
                new_region.add((sx, sy))
                for n in neighbors((sx, sy), len(lines)):
                    if n in visited:
                        continue
                    if lines[n[1]][n[0]] == c:
                        visited.add((n[0], n[1]))
                        search.append(n)
            regions.append(new_region)
    p1 = 0
    p2 = 0
    for r in regions:
        perimeter, sides = solve(r)
        p1 += len(r) * perimeter
        p2 += len(r) * sides

    print("Part 1:", p1)
    print("Part 2:", p2)
