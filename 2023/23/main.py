import sys
from contextlib import suppress
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


def solve(slippery=True):
    hikes = [(0, start, [start])]
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    violation = {(0, 1): "<", (0, -1): ">", (1, 0): "^", (-1, 0): "v"}
    completes = []
    while hikes:
        steps, cursor, history = heappop(hikes)
        if cursor == end:
            heappush(completes, (steps, cursor, history))
        for n in neighbors:
            dr, dc = cursor[0] + n[0], cursor[1] + n[1]
            if slippery and (dr, dc) in slopes and slopes[(dr, dc)] == violation[n]:
                continue
            if (dr, dc) in paths and (dr, dc) not in history:
                heappush(hikes, (steps - 1, (dr, dc), history + [(dr, dc)]))
    return abs(heappop(completes)[0])


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, end = (0, 1), (len(lines) - 1, len(lines[0]) - 2)
    paths, slopes, junctions = set(), dict(), set()
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for r, c in product(range(len(lines)), repeat=2):
        surrounding = []
        for n in neighbors:
            dr, dc = r + n[0], c + n[1]
            with suppress(IndexError):
                surrounding.append(lines[dr][dc] in "^>v<")
        if 3 <= sum(surrounding):
            junctions.add((r, c))
        if lines[r][c] in ".^>v<":
            paths.add((r, c))
        if lines[r][c] in "^>v<":
            slopes[(r, c)] = lines[r][c]

    print("Part 1:", solve())
    print("Part 2:", solve(False))
