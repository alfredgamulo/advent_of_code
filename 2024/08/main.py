import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path


def solver(antennas, limit, part2=False):
    new_points = set()
    for antennas in frequencies.values():
        for a, b in combinations(antennas, 2):
            if part2:
                new_points.add(a)
                new_points.add(b)
            dx, dy = a[0] - b[0], a[1] - b[1]
            x, y = a[0] + dx, a[1] + dy
            while 0 <= x < limit and 0 <= y < limit:
                new_points.add((x, y))
                if not part2:
                    break
                x, y = x + dx, y + dy
            x, y = b[0] - dx, b[1] - dy
            while 0 <= x < limit and 0 <= y < limit:
                new_points.add((x, y))
                if not part2:
                    break
                x, y = x - dx, y - dy
    return len(new_points)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    frequencies = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                frequencies[c].add((x, y))
    limit = len(lines)
    print("Part 1:", solver(frequencies, limit))
    print("Part 2:", solver(frequencies, limit, part2=True))
