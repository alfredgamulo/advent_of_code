import sys
from collections import defaultdict, deque
from itertools import cycle


def shapes():
    shapes = [
        [(2, 3), (3, 3), (4, 3), (5, 3)],
        [(3, 3), (2, 4), (3, 4), (4, 4), (3, 5)],
        [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)],
        [(2, 3), (2, 4), (2, 5), (2, 6)],
        [(2, 3), (3, 3), (2, 4), (3, 4)],
    ]
    for i, s in cycle(enumerate(shapes)):
        yield i, s


def jets(pattern):
    lookup = {
        ">": (1, 0),
        "<": (-1, 0),
    }
    for i, j in cycle(enumerate(pattern)):
        yield i, lookup[j]


def shift(shape, offset):
    res = []
    for s in shape:
        res.append(tuple(map(sum, zip(s, offset))))
    return res


def solve(iterations, jet, shape):
    floor = 0
    formation = deque(maxlen=1000)

    for _ in range(iterations):
        rock = shift(next(shape)[1], (0, floor))
        stuck = False
        while not stuck:
            moved_rock = shift(rock, next(jet)[1])
            if all(0 <= x < 7 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            moved_rock = shift(rock, (0, -1))
            if all(y >= 0 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            else:
                stuck = True
        formation.extend(rock)
        floor = max(floor, max(y for _, y in rock) + 1)

    return floor


def part1(lines):
    jet = jets(lines[0])
    shape = shapes()
    return solve(2022, jet, shape)


def movement(rock, init):
    res = []
    for r, i in zip(rock, init):
        res.append((r[0] - i[0], r[1] - i[1]))
    return tuple(res)


def part2(lines):
    # 1000000000000
    jet = jets(lines[0])
    shape = shapes()

    floor = 0
    formation = deque(maxlen=1000)

    cycles = None
    cache = defaultdict(list)
    history = deque(maxlen=len(lines))
    for i in range(9000):
        # print(i, flush=True)
        si, sn = next(shape)
        rock = shift(sn, (0, floor))
        init = rock
        stuck = False
        while not stuck:
            ji, jn = next(jet)
            moved_rock = shift(rock, jn)
            if all(0 <= x < 7 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            moved_rock = shift(rock, (0, -1))
            if all(y >= 0 and (x, y) not in formation for x, y in moved_rock):
                rock = moved_rock
            else:
                stuck = True
        formation.extend(rock)
        floor = max(floor, max(y for _, y in rock) + 1)

        history.append(movement(rock, init))
        cache[(si, ji, tuple(history))].append((i, floor - 1))
        if len(cache[(si, ji, tuple(history))]) > 5:
            cycles = (
                cache[(si, ji, tuple(history))][1],
                cache[(si, ji, tuple(history))][3],
            )
            break

    i1, h1 = cycles[0]
    i2, h2 = cycles[1]

    # return ((1000000000000 - i1) // (i2 - i1) * (h2 - h1)) + h1


# too low 1540634005750
#         1540634005764 < not right

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))  # looking for 1514285714288
