import sys
from collections import defaultdict, deque
from functools import cache


class hashabledefaultdict(defaultdict):
    def __hash__(self):
        h = 1
        for k, v in self.items():
            h *= hash(tuple((k, (tuple(sorted(v))))))
        return h


@cache
def next_blizz(blizzards, limits):
    nb = hashabledefaultdict(list)
    for dir, coords in blizzards.items():
        for coord in coords:
            match dir:
                case ">":
                    n = (coord[0], coord[1] + 1)
                    if n[1] > limits[1]:
                        n = (coord[0], 1)
                    nb[">"].append(n)
                case "<":
                    n = (coord[0], coord[1] - 1)
                    if n[1] < 1:
                        n = (coord[0], limits[1])
                    nb["<"].append(n)
                case "^":
                    n = (coord[0] - 1, coord[1])
                    if n[0] < 1:
                        n = (limits[0], coord[1])
                    nb["^"].append(n)
                case "v":
                    n = (coord[0] + 1, coord[1])
                    if n[0] > limits[0]:
                        n = (1, coord[1])
                    nb["v"].append(n)
    return nb


def solve(blizzards, limits, start, end):
    q = deque([(0, start, blizzards)])  # step, pos, blizz, waited
    visited = set()
    while q:
        step, position, blizzs = q.popleft()

        if position == end:
            return step, blizzs

        skip = False
        for _, b in blizzs.items():
            if position in b:
                skip = True
                break
        if skip:
            continue

        for a in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            n = (position[0] + a[0], position[1] + a[1])

            if (
                (n in [start, end])
                or (1 <= n[0] <= limits[0] and 1 <= n[1] <= limits[1])
                and (step + 1, n) not in visited
            ):
                visited.add((step + 1, n))
                q.append((step + 1, n, next_blizz(blizzs, limits)))


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    blizzards = hashabledefaultdict(list)
    limits = (len(lines) - 2, len(lines[0]) - 2)
    start, end = (0, 1), None
    for r, line in enumerate(lines):
        for c, row in enumerate(line):
            if lines[r][c] != "#":
                if lines[r][c] != ".":
                    blizzards[lines[r][c]].append((r, c))
                end = (r, c)

    s1, b1 = solve(blizzards, limits, start, end)
    print("Part 1:", s1)
    next_blizz.cache_clear()
    s2, b2 = solve(b1, limits, end, start)
    next_blizz.cache_clear()
    s3, _ = solve(b2, limits, start, end)
    print("Part 2:", s1 + s2 + s3)
