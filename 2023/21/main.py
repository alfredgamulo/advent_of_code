import sys
from collections import deque
from itertools import product
from pathlib import Path


def expand(plots, boundaries):
    new = set()
    neighbors = list(product([0, -1, 1], repeat=2))
    multiplier = boundaries[1] // len(lines)
    boundaries = (
        boundaries[0] - len(lines) * multiplier,
        boundaries[1] + len(lines) * multiplier,
    )
    for r, c in plots:
        new.update(
            [
                (
                    r + n[0] * multiplier * len(lines),
                    c + n[1] * multiplier * len(lines),
                )
                for n in neighbors
            ]
        )
    plots.update(new)
    return plots, boundaries


def solve(limit, plots, boundaries):
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    possibilities = deque(((0, start),))
    visited = set([start])
    answer = 0
    while possibilities and (check := possibilities.popleft()):
        steps, position = check
        if steps > limit:
            continue
        if steps % 2 == 0:
            answer += 1
        for n in neighbors:
            dr, dc = position[0] + n[0], position[1] + n[1]
            if any(not boundaries[0] <= x <= boundaries[1] for x in [dr, dc]):
                plots, boundaries = expand(plots, boundaries)
            if (dr, dc) not in visited and (dr, dc) in plots:
                possibilities.append((steps + 1, (dr, dc)))
                visited.add((dr, dc))
    return answer


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, plots = (len(lines) // 2, len(lines[0]) // 2), set()
    for r, line in enumerate(lines):
        for c, l in enumerate(line):
            if l != "#":
                plots.add((r, c))
    print("Part 1:", solve(6, plots, (0, len(lines))))
    print("Part 2:", solve(1000, plots, (0, len(lines))))
