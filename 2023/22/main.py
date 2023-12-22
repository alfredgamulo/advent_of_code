import re
import sys
from collections import defaultdict
from copy import copy
from heapq import heappop, heappush
from itertools import chain
from pathlib import Path


def intersect(a, b):
    return bool(range(max(a[0], b[0]), min(a[1], b[1]) + 1))


def drop(bricks):
    settled = defaultdict(list)
    settled[1] = []
    while bricks:
        z, x, y = heappop(bricks)
        level = len(settled)
        while checks := settled[level]:
            collision = False
            for check in checks:
                if intersect(check[1], x) and intersect(check[2], y):
                    collision = True
                    level = check[0][1] + 1
            if not collision:
                break
        z = (level, z[1] - z[0] + level)
        settled[level].append([z, x, y])
    # print(settled)
    heap = []
    for brick in chain(*settled.values()):
        heappush(heap, brick)
    return heap


def part1():
    settled = drop(copy(bricks))
    count = 0
    for i in range(len(settled)):
        a = copy(settled)
        del a[i]
        b = copy(a)
        if a == (c := drop(b)):
            count += 1
    return count


def part2():
    ...


if __name__ == "__main__":
    bricks = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        x1, y1, z1, x2, y2, z2 = map(int, re.findall("\\d+", line))
        heappush(bricks, [(z1, z2), (x1, x2), (y1, y2)])
    print("Part 1:", part1())
    print("Part 2:", part2())
