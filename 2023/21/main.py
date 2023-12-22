import sys
from collections import deque
from pathlib import Path


def solve(limit):
    parity = [0, 0]
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    possibilities = deque(((0, start),))
    visited = set([start])
    while possibilities and (check := possibilities.popleft()):
        steps, position = check
        if steps > limit:
            continue
        parity[steps % 2] += 1
        for n in neighbors:
            dr, dc = position[0] + n[0], position[1] + n[1]
            if (dr, dc) not in visited and (dr, dc) in plots:
                possibilities.append((steps + 1, (dr, dc)))
                visited.add((dr, dc))
    return parity


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, plots = (len(lines) // 2, len(lines[0]) // 2), set()
    for r, line in enumerate(lines):
        for c, l in enumerate(line):
            if l != "#":
                plots.add((r, c))

    print("Part 1:", solve(64)[0])

    # math required summarized here: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
    even_full, odd_full = solve(200)  # even & odd tiles of a fully saturated square
    even_diamond, odd_diamond = solve(start[0])  # a saturated diamond
    even_corners, odd_corners = (  # outer corners is full minus inner diamond
        even_full - even_diamond,
        odd_full - odd_diamond,
    )
    n = (26501365 - start[0]) // len(lines)  # n is the number of grids out we will go
    p2 = (
        ((n + 1) ** 2 * odd_full)
        + (n**2 * even_full)
        - ((n + 1) * odd_corners)
        + (n * even_corners)
    )  # this math explained in the link above
    print("Part 2:", p2)
