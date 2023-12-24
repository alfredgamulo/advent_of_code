import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from itertools import (
    batched,
    chain,
    combinations,
    count,
    groupby,
    permutations,
    product,
    zip_longest,
)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter


def slope_intercept(x, y, dx, dy):  # return m and b
    return dy / dx, -x * (dy / dx) + y


def intersection(m1, b1, m2, b2):
    if m1 == m2:
        return None, None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


def part1():
    for one, two in combinations(stones, 2):
        x, y = intersection(*one[-1], *two[-1])
        print("\n====>", one, two)
        print(x, y)


def part2():
    ...


if __name__ == "__main__":
    stones = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        x, y, z, dx, dy, dz = map(int, re.findall("-?\\d+", line))
        stones.append([x, y, z, dx, dy, dz, slope_intercept(x, y, dx, dy)])
    if sys.argv[1] == "input":
        search = (7, 27)
    else:
        search = (200_000_000_000_000, 400_000_000_000_000)
    print(stones)
    print("Part 1:", part1())
    print("Part 2:", part2())
