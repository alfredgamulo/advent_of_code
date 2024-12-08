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
from pathlib import Path
from pprint import PrettyPrinter

import numpy as np

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def part1(lines, location, obstacles):
    visited = set()
    direction = dirs[0]
    while 0 <= location[0] < len(lines) and 0 <= location[1] < len(lines):
        visited.add(location)
        nxt = location[0] + direction[0], location[1] + direction[1]
        if nxt not in obstacles:
            location = nxt
        else:
            direction = dirs[(dirs.index(direction) + 1) % 4]
    return len(visited)


def part2():
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    location = None
    obstacles = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                location = (x, y)
            if c == "#":
                obstacles.add((x, y))
    print("Part 1:", part1(lines, location, obstacles))
    print("Part 2:", part2())
