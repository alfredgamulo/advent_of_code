import sys
from collections import defaultdict, deque
from pathlib import Path


def neighbors(coords):
    return [
        (coords[0] - 1, coords[1]),
        (coords[0] + 1, coords[1]),
        (coords[0], coords[1] - 1),
        (coords[0], coords[1] + 1),
    ]


def solve(indexes):
    p1 = 0
    p2 = 0
    for zero in indexes[0]:
        search = deque([(0, zero)])
        peaks = set()
        while search:
            height, location = search.popleft()
            if height == 9:
                peaks.add(location)
                p2 += 1
                continue
            for n in neighbors(location):
                if n in indexes[height + 1]:
                    search.append((height + 1, n))
        p1 += len(peaks)
    return p1, p2
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    indexes = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            indexes[int(c)].add((x, y))
    p1, p2 = solve(indexes)
    print("Part 1:", p1)
    print("Part 2:", p2)
