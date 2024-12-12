

import sys
from pathlib import Path


def neighbors(coords):
    return [
        (coords[0] - 1, coords[1]),
        (coords[0] + 1, coords[1]),
        (coords[0], coords[1] - 1),
        (coords[0], coords[1] + 1),
    ]


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    regions = list()
    visited = set()
    for y, line in enumerate(lines):
        for x, c in line:
            visited.add((x, y))
    print("Part 1:", ...)
    print("Part 2:", ...)
