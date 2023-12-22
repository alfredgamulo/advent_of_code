import re
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter


def intersect(a, b):
    return bool(range(max(a[0], b[0]), min(a[1], b[1]) + 1))


def drop(bricks):
    settled = defaultdict(list)
    settled[1] = []
    while bricks:
        z, x, y = heappop(bricks)
        level = len(settled)
        while checks := settled[level]:
            # collision = False
            # for check in checks:
            #     if intersect(check[1], x) and intersect(check[2], y):
            #         collision = True
            # if collision:
            #     level += 1
            if any(
                intersect(check[1], x) and intersect(check[2], y) for check in checks
            ):
                level += 1
            else:
                break
        z = (level, z[1] - z[0] + level)
        settled[level].append([z, x, y])
    return settled


def part1():
    settled = drop(deepcopy(bricks))
    print(settled)
    print()
    print()
    count = 0
    for level in range(1, len(settled)):
        print()
        for a in settled[level]:
            for b in settled[level + 1]:
                c = (a[0][1], b[0][1] - b[0][0] + a[0][1])
                print("-->", a, b, c)
                if (
                    intersect(a[1], b[1])
                    and intersect(a[2], b[2])
                    and intersect(a[0], c)
                ):
                    continue
                else:
                    print("clear!")
                    count += 1
    return count


def part2():
    ...


if __name__ == "__main__":
    bricks = []

    for line in Path(sys.argv[1]).read_text().splitlines():
        x1, y1, z1, x2, y2, z2 = map(int, re.findall("\\d", line))
        heappush(bricks, [(z1, z2), (x1, x2), (y1, y2)])
    print("Part 1:", part1())
    print("Part 2:", part2())
