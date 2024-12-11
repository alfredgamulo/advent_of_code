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
from itertools import (batched, chain, combinations, count, groupby,
                       permutations, product, zip_longest)
from math import ceil, floor, lcm, prod, sqrt
from operator import index
from pathlib import Path
from pprint import PrettyPrinter

import numpy as np


def neighbors(coords):
    return [
        (coords[0] - 1, coords[1] - 1),
        (coords[0] - 1, coords[1] + 1),
        (coords[0] + 1, coords[1] - 1),
        (coords[0] + 1, coords[1] + 1),
    ]


def part1(indexes, topography):
    print(indexes)
    print(topography)
    zeroes = indexes[0]
    p1 = 0
    for zero in zeroes:
        print(zero)
    ...


def part2(indexes):
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    indexes = defaultdict(set)
    topography = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            indexes[int(c)].add((x, y))
            topography[(x, y)] = c
    print("Part 1:", part1(indexes, topography))
    print("Part 2:", part2(indexes))
