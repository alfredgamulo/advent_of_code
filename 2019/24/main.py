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


def part1(lines):
    # represent grid as 25-bit mask (pos = r*5 + c), LSB = top-left
    start = 0
    for r, line in enumerate(lines):
        for c, ch in enumerate(line.strip()):
            if ch == '#':
                start |= 1 << (r * 5 + c)

    # precompute neighbor bitmasks for each pos
    neigh = [0] * 25
    for r in range(5):
        for c in range(5):
            p = r * 5 + c
            bits = 0
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < 5 and 0 <= cc < 5:
                    bits |= 1 << (rr * 5 + cc)
            neigh[p] = bits

    seen = set()
    cur = start
    while cur not in seen:
        seen.add(cur)
        nxt = 0
        for p in range(25):
            count = bin(cur & neigh[p]).count("1")
            if (cur >> p) & 1:
                # bug survives only if exactly one neighbor
                if count == 1:
                    nxt |= 1 << p
            else:
                # empty becomes bug if 1 or 2 neighbors
                if count == 1 or count == 2:
                    nxt |= 1 << p
        cur = nxt

    # biodiversity rating is the mask value
    return cur


def part2(lines):
    # parse initial level 0
    start = 0
    for r, line in enumerate(lines):
        for c, ch in enumerate(line.strip()):
            if ch == '#':
                start |= 1 << (r * 5 + c)

    CENTER = 2 * 5 + 2

    # precompute neighbor mapping for recursive grids
    # for each pos (except center) produce list of (delta_level, pos_index)
    neighbor_map = {p: [] for p in range(25) if p != CENTER}
    for r in range(5):
        for c in range(5):
            p = r * 5 + c
            if p == CENTER:
                continue
            lst = []
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                # neighbor is the center -> expands to inner level
                if nr == 2 and nc == 2:
                    # entering inner level: add multiple positions in level+1
                    if dr == 1:  # moved down into center -> inner top row
                        for cc in range(5):
                            lst.append((1, 0 * 5 + cc))
                    elif dr == -1:  # moved up into center -> inner bottom row
                        for cc in range(5):
                            lst.append((1, 4 * 5 + cc))
                    elif dc == 1:  # moved right into center -> inner left col
                        for rr in range(5):
                            lst.append((1, rr * 5 + 0))
                    elif dc == -1:  # moved left into center -> inner right col
                        for rr in range(5):
                            lst.append((1, rr * 5 + 4))
                # neighbor is outside -> maps to outer level
                elif not (0 <= nr < 5 and 0 <= nc < 5):
                    # map to outer center-adjacent
                    if nr < 0:
                        lst.append((-1, 1 * 5 + 2))
                    elif nr > 4:
                        lst.append((-1, 3 * 5 + 2))
                    elif nc < 0:
                        lst.append((-1, 2 * 5 + 1))
                    elif nc > 4:
                        lst.append((-1, 2 * 5 + 3))
                else:
                    # normal neighbor in same level
                    lst.append((0, nr * 5 + nc))
            neighbor_map[p] = lst

    # levels dict: level -> mask (exclude center bit from masks)
    levels = {0: start & ~(1 << CENTER)}

    minutes = 200
    for _ in range(minutes):
        new_levels = {}
        min_level = min(levels.keys())
        max_level = max(levels.keys())
        # expand range by 1 on each side because bugs can spread
        for level in range(min_level - 1, max_level + 2):
            cur = levels.get(level, 0)
            nxt = 0
            for p in range(25):
                if p == CENTER:
                    continue
                count = 0
                for dl, np in neighbor_map[p]:
                    m = levels.get(level + dl, 0)
                    if (m >> np) & 1:
                        count += 1
                if (cur >> p) & 1:
                    if count == 1:
                        nxt |= 1 << p
                else:
                    if count == 1 or count == 2:
                        nxt |= 1 << p
            if nxt:
                new_levels[level] = nxt
        levels = new_levels

    # count bugs across all levels
    total = 0
    for m in levels.values():
        total += m.bit_count()
    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
