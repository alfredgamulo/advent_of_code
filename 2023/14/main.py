import sys
from functools import cache
from itertools import product
from pathlib import Path


def parse(lines):
    rocks, walls = set(), []
    for x, line in enumerate(lines):
        for y, l in enumerate(line):
            if l == "O":
                rocks.add((x, y))
            elif l == "#":
                walls.append((x, y))
    walls.extend((x, y) for x, y in product([-1, len(lines[0])], range(len(lines))))
    walls.extend((x, y) for x, y in product(range(len(lines[0])), [-1, len(lines[0])]))
    return frozenset(rocks), frozenset(walls)


@cache
def tilt(rocks, walls, roll):
    rocks = set(rocks)
    moved = True
    while moved:
        moved = False
        tmp_rocks = set()
        while rocks and (pop := rocks.pop()):
            x, y = pop[0] + roll[0], pop[1] + roll[1]
            if (x, y) not in walls and (x, y) not in rocks and (x, y) not in tmp_rocks:
                tmp_rocks.add((x, y))
                moved = True
            else:
                tmp_rocks.add(pop)
        rocks = tmp_rocks
    return frozenset(rocks)


def part1(rocks, walls):
    rocks = tilt(rocks, walls, (-1, 0))
    return sum(len(lines) - r[0] for r in rocks)


def part2(rocks, walls):
    loads = []
    for _ in range(1_000):
        for roll in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            rocks = tilt(rocks, walls, roll)
        loads.append(sum(len(lines) - r[0] for r in rocks))
    return loads[-1]


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    rocks, walls = parse(lines)
    print("Part 1:", part1(rocks, walls))
    print("Part 2:", part2(rocks, walls))
