

import sys
from collections import defaultdict, deque
from functools import cache
from math import gcd
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


def calculate_perimeter(coords):
    @cache
    def is_boundary(x, y):
        # Check if a point is a boundary point
        return (x - 1, y) not in coords or (x + 1, y) not in coords or (x, y - 1) not in coords or (x, y + 1) not in coords

    boundary_points = [point for point in coords if is_boundary(*point)]
    perimeter = 0

    for x, y in boundary_points:
        if (x - 1, y) not in coords:
            perimeter += 1
        if (x + 1, y) not in coords:
            perimeter += 1
        if (x, y - 1) not in coords:
            perimeter += 1
        if (x, y + 1) not in coords:
            perimeter += 1

    return perimeter, boundary_points


def count_continuous_lines(coords):
    from collections import defaultdict

    # Group coordinates by rows and columns
    rows = defaultdict(list)
    cols = defaultdict(list)
    for x, y in coords:
        rows[y].append(x)
        cols[x].append(y)

    def count_lines(group):
        count = 0
        for key in group:
            group[key].sort()
            start = group[key][0]
            for i in range(1, len(group[key])):
                if group[key][i] != group[key][i - 1] + 1:
                    count += 1
                    start = group[key][i]
            count += 1
        return count

    # Count horizontal and vertical lines
    horizontal_lines = count_lines(rows)
    vertical_lines = count_lines(cols)
    print(horizontal_lines, vertical_lines)
    return horizontal_lines + vertical_lines


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
        perimeter, boundary = calculate_perimeter(r)
        print("bounds = ", boundary)
        p1 += len(r) * perimeter
        p2 += len(r) * count_continuous_lines(boundary)

    print("Part 1:", p1)
    print("Part 2:", p2)
