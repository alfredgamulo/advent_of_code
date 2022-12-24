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


def part1(blizzards, limits, end):
    q = deque([(0, (0, 1), blizzards)])  # step, pos, blizz, waited
    visited = set()
    while q:
        step, position, blizzs = q.popleft()
        # print(step, position, len(q))
        # check if position is on a blizz
        skip = False
        for _, b in blizzs.items():
            if position in b:
                skip = True
                break
        if skip:
            continue

        for a in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            n = (position[0] + a[0], position[1] + a[1])
            if n == end:
                return step + 1
            if (
                (n == (0, 1))
                or (1 <= n[0] <= limits[0] and 1 <= n[1] <= limits[1])
                and (step + 1, n) not in visited
            ):
                visited.add((step + 1, n))
                q.append((step + 1, n, next_blizz(blizzs, limits)))


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    blizzards = hashabledefaultdict(list)
    max_r = len(lines) - 2
    max_c = len(lines[0]) - 2
    end = None
    for r, line in enumerate(lines):
        for c, row in enumerate(line):
            if lines[r][c] != "#":
                if lines[r][c] != ".":
                    blizzards[lines[r][c]].append((r, c))
                end = (r, c)

    print("Part 1:", part1(blizzards, (max_r, max_c), end))
    print("Part 2:", part2())
