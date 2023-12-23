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
    hikes = [(0, start, [start])]
    neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    violation = {(0, 1): "<",(0, -1): ">", (1, 0):"^", (-1, 0):"v"}
    completes = []
    while hikes:
        steps, cursor, visited = heappop(hikes)
        if cursor == end:
            heappush(completes,(steps, cursor, visited))
        for n in neighbors:
            dr, dc = cursor[0]+n[0], cursor[1]+n[1]
            if (dr, dc) in slopes and slopes[(dr,dc)] == violation[n]:
                continue
            if (dr,dc) in paths and (dr,dc) not in visited:
                heappush(hikes, (steps-1, (dr, dc), visited + [(dr,dc)]))
    return abs(heappop(completes)[0])

            


def part2():
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    start, end = (0, 1), (len(lines) - 1, len(lines[0]) - 2)
    paths, slopes = set(), dict()
    for r, c in product(range(len(lines)), repeat=2):
        if lines[r][c] in ".^>v<":
            paths.add((r, c))
        if lines[r][c] in "^>v<":
            slopes[(r, c)] = lines[r][c]
    print("Part 1:", part1())
    print("Part 2:", part2())
