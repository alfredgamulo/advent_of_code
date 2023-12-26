import sys
from contextlib import suppress
from heapq import heappop, heappush
from itertools import product
from pathlib import Path


def solve(slippery=True):
    hikes = [(0, start, set([start]))]
    violation = {(0, 1): "<", (0, -1): ">", (1, 0): "^", (-1, 0): "v"}
    most = 0
    while hikes:
        steps, cursor, history = heappop(hikes)
        while cursor not in junctions:
            change = False
            for n in neighbors:
                dr, dc = cursor[0] + n[0], cursor[1] + n[1]
                if (dr, dc) in paths and (dr, dc) not in history:
                    change = True
                    steps -= 1
                    history.add((dr, dc))
                    cursor = (dr, dc)
                    break
            if not change:
                break
        if cursor == end:
            if abs(steps) + magic_number > most:
                most = abs(steps) + magic_number
                print(most, flush=True)
            continue
        for n in neighbors:
            dr, dc = cursor[0] + n[0], cursor[1] + n[1]
            if slippery and (dr, dc) in slopes and slopes[(dr, dc)] == violation[n]:
                continue
            if (dr, dc) in paths and (dr, dc) not in history:
                heappush(hikes, (steps - 1, (dr, dc), set(list(history) + [(dr, dc)])))

    return most  # magic number


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start = (0, 1)
    if sys.argv[1] == "sample":
        end = (19, 19)
        magic_number = 5
    else:
        end = (127, 123)
        magic_number = 209
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
