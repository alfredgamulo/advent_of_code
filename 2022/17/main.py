import sys
from itertools import cycle

"""
shapes:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

"""

"""
seven-wide

2 to the right
3 up
|..@@@@.|
|.......|
|.......|
|.......|
+-------+
"""


def shapes():
    shapes = [
        [(2, 3), (3, 3), (4, 3), (5, 3)],
        [(3, 3), (2, 4), (3, 4), (4, 4), (3, 5)],
        [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)],
        [(2, 3), (2, 4), (2, 5), (2, 6)],
        [(2, 3), (3, 3), (2, 4), (3, 4)],
    ]
    for s in cycle(shapes):
        yield s


def jets(pattern):
    lookup = {
        ">": (1, 0),
        "<": (-1, 0),
    }
    for j in cycle(pattern):
        yield lookup[j]


def shift(shape, offset):
    res = []
    for s in shape:
        res.append(tuple(map(sum, zip(s, offset))))
    return res


def part1(lines):
    shape = shapes()
    jet = jets(lines[0])
    floor = 0
    formation = set()
    for _ in range(2022):
        rock = shift(next(shape), (0, floor))
        stuck = False
        while not stuck:
            moved_rock = shift(rock, next(jet))
            if all(0 <= x < 7 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            moved_rock = shift(rock, (0, -1))
            if all(y >= 0 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            else:
                stuck = True
        formation.update(rock)
        floor = max(y for _, y in rock) + 1
    return floor - 1


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
