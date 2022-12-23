import sys
from collections import defaultdict
from itertools import count, cycle, product

neight = set(product((-1, 0, 1), repeat=2)) - set([(0, 0)])
north = ([n for n in neight if n[0] == -1], (-1, 0))
south = ([n for n in neight if n[0] == 1], (1, 0))
east = ([n for n in neight if n[1] == 1], (0, 1))
west = ([n for n in neight if n[1] == -1], (0, -1))


def direction_order():
    directions = [north, south, west, east]
    for c in cycle(range(4)):
        yield directions[c:] + directions[:c]


def solve(elves):
    d = direction_order()
    for i in count(1):
        # check eights
        movers = set()
        for e in elves:
            for n in neight:
                if (e[0] + n[0], e[1] + n[1]) in elves:
                    movers.add(e)
                    break
        elves = elves - movers

        if not movers:
            print("Part 2:", i)
            return

        # find potential moves
        dirs = next(d)
        proposals = defaultdict(list)
        for m in movers:
            for checks, p in dirs:
                check_set = {
                    (m[0] + checks[0][0], m[1] + checks[0][1]),
                    (m[0] + checks[1][0], m[1] + checks[1][1]),
                    (m[0] + checks[2][0], m[1] + checks[2][1]),
                }
                if not (check_set & elves or check_set & movers):
                    proposals[(m[0] + p[0], m[1] + p[1])].append(m)
                    break

        # move if no conflicts
        for p, o in proposals.items():
            if len(o) == 1:
                elves.add(p)
                movers.remove(o[0])

        elves.update(movers)  # add back conflicted movers

        if i == 10:
            min_x, max_x, min_y, max_y = 0, 0, 0, 0
            for e in elves:
                min_x, max_x = min(min_x, e[0]), max(max_x, e[0])
                min_y, max_y = min(min_y, e[1]), max(max_y, e[1])

            print(
                "Part 1:", abs(max_x + 1 - min_x) * abs(max_y + 1 - min_y) - len(elves)
            )


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    elves = set()
    for r, line in enumerate(lines):
        for c, space in enumerate(line):
            if space == "#":
                elves.add((r, c))

    solve(elves)
