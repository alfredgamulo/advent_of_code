import sys
from collections import defaultdict
from itertools import cycle, product

neight = set(product((-1, 0, 1), repeat=2)) - set([(0, 0)])
north = ([n for n in neight if n[0] == -1], (-1, 0))
south = ([n for n in neight if n[0] == 1], (1, 0))
east = ([n for n in neight if n[1] == 1], (0, 1))
west = ([n for n in neight if n[1] == -1], (0, -1))


def direction_order():
    directions = [north, south, west, east]
    for c in cycle(range(4)):
        yield directions[c:] + directions[:c]


def part1(elves):
    d = direction_order()
    for _ in range(10):
        # check eights
        movers = set()
        for e in elves:
            for n in neight:
                if tuple(map(sum, zip(e, n))) in elves:
                    movers.add(e)
                    break
        elves = elves - movers

        # find potential moves
        dirs = next(d)
        proposals = defaultdict(list)
        for m in movers:
            for checks, p in dirs:
                if not (
                    set(
                        [
                            tuple(map(sum, zip(m, checks[0]))),
                            tuple(map(sum, zip(m, checks[1]))),
                            tuple(map(sum, zip(m, checks[2]))),
                        ]
                    )
                    & elves.union(movers)
                ):
                    proposals[tuple(map(sum, zip(m, p)))].append(m)
                    break

        # move if no conflicts
        for p, o in proposals.items():
            if len(o) == 1:
                elves.add(p)
                movers.remove(o[0])

        elves.update(movers)  # add back conflicted movers

    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for e in elves:
        min_x = min(min_x, e[0])
        max_x = max(max_x, e[0])
        min_y = min(min_y, e[1])
        max_y = max(max_y, e[1])

    return abs(max_x + 1 - min_x) * abs(max_y + 1 - min_y) - len(elves)


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    elves = set()
    for r, line in enumerate(lines):
        for c, space in enumerate(line):
            if space == "#":
                elves.add((r, c))

    print("Part 1:", part1(elves))
    print("Part 2:", part2())
