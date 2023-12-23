import sys

from heapq import heappop, heappush
from itertools import product
from pathlib import Path


def solve(slippery=True):
    hikes = [(0, start, [start])]
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    violation = {(0, 1): "<", (0, -1): ">", (1, 0): "^", (-1, 0): "v"}
    duplicate = dict()
    completes = []
    while hikes:
        steps, cursor, history = heappop(hikes)
        if cursor == end:
            heappush(completes, (steps, cursor, history))
        if cursor in duplicate and duplicate[cursor] > steps:
            continue
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
    paths, slopes = set(), dict()
    for r, c in product(range(len(lines)), repeat=2):
        if lines[r][c] in ".^>v<":
            paths.add((r, c))
        if lines[r][c] in "^>v<":
            slopes[(r, c)] = lines[r][c]

    print("Part 1:", solve())
    print("Part 2:", solve(False))
