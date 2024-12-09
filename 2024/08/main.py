import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def part1(frequencies, limit):
    new_points = set()
    for antennas in frequencies.values():
        if len(antennas) == 1:
            continue
        for a, b in combinations(antennas, 2):
            dx, dy = a[0] - b[0], a[1] - b[1]
            x1, y1 = a[0] + dx, a[1] + dy
            x2, y2 = b[0] - dx, b[1] - dy
            if 0 <= x1 < limit and 0 <= y1 < limit:
                new_points.add((x1, y1))
            if 0 <= x2 < limit and 0 <= y2 < limit:
                new_points.add((x2, y2))

    return len(new_points)


def part2(frequencies, limit):
    new_points = set()
    for antennas in frequencies.values():
        if len(antennas) == 1:
            continue
        for a, b in combinations(antennas, 2):
            new_points.add(a)
            new_points.add(b)
            dx, dy = a[0] - b[0], a[1] - b[1]
            x1, y1 = a[0] + dx, a[1] + dy
            while 0 <= x1 < limit and 0 <= y1 < limit:
                new_points.add((x1, y1))
                x1, y1 = x1 + dx, y1 + dy

            x2, y2 = b[0] - dx, b[1] - dy
            while 0 <= x2 < limit and 0 <= y2 < limit:
                new_points.add((x2, y2))
                x2, y2 = x2 - dx, y2 - dy

    return len(new_points)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    frequencies = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                frequencies[c].add((x, y))
    limit = len(lines)
    print("Part 1:", part1(frequencies, limit))
    print("Part 2:", part2(frequencies, limit))
