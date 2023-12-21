import sys
from collections import deque
from pathlib import Path


def solve(limit):
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
            if (dr, dc) not in visited and (dr, dc) in plots:
                possibilities.append((steps + 1, (dr, dc)))
                visited.add((dr, dc))
    return answer


def part2():
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, plots = None, set()
    for r, line in enumerate(lines):
        for c, l in enumerate(line):
            if l != "#":
                plots.add((r, c))
                if l == "S":
                    start = (r, c)
    print("Part 1:", solve(64))
    print("Part 2:", part2())
