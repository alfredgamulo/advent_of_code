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


def part1():
    hikes = [(0, start, set())]
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while hikes:
        steps, cursor, visited = heappop(hikes)
        if cursor == end:
            return abs(steps)
        for n in neighbors:
            


def part2():
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, end = (0, 1), (len(lines) - 1, len(lines[0]) - 2)
    paths, slopes = set(), dict()
    print(start, end)
    for r, c in product(range(len(lines)), repeat=2):
        if lines[r][c] == ".":
            paths.add((r, c))
        elif lines[r][c] in "^>v<":
            slopes[(r, c)] = lines[r][c]
    print(paths)
    print(slopes)

    print("Part 1:", part1())
    print("Part 2:", part2())
