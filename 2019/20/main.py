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
    # parse grid
    grid = {}
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            grid[(x, y)] = ch

    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    # find labels and portal positions
    labels = {}
    portal_at = {}

    def add_label(name, pos):
        labels.setdefault(name, []).append(pos)
        portal_at[pos] = name

    for (x, y), ch in list(grid.items()):
        if not ch.isupper():
            continue
        # check right
        if grid.get((x + 1, y), ' ').isupper():
            name = ch + grid[(x + 1, y)]
            # check left or right for entrance '.'
            if grid.get((x - 1, y), '#') == '.':
                add_label(name, (x - 1, y))
            elif grid.get((x + 2, y), '#') == '.':
                add_label(name, (x + 2, y))
        # check down
        if grid.get((x, y + 1), ' ').isupper():
            name = ch + grid[(x, y + 1)]
            if grid.get((x, y - 1), '#') == '.':
                add_label(name, (x, y - 1))
            elif grid.get((x, y + 2), '#') == '.':
                add_label(name, (x, y + 2))

    # build adjacency for '.' cells
    def neighbors(p):
        x, y = p
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + dx, y + dy)
            if grid.get(q) == '.':
                yield q

    # find start and end
    start = labels['AA'][0]
    end = labels['ZZ'][0]

    # BFS
    from collections import deque

    dq = deque()
    dq.append((start, 0))
    seen = {start}
    while dq:
        pos, d = dq.popleft()
        if pos == end:
            return d
        # normal neighbors
        for q in neighbors(pos):
            if q not in seen:
                seen.add(q)
                dq.append((q, d + 1))
        # portal
        label = portal_at.get(pos)
        if label and label not in ('AA', 'ZZ'):
            ps = labels[label]
            # teleport to the other position
            other = ps[1] if ps[0] == pos else ps[0]
            if other not in seen:
                seen.add(other)
                dq.append((other, d + 1))

    return None


def part2(lines):
    grid = {}
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            grid[(x, y)] = ch

    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    labels = {}
    portal_at = {}

    def add_label(name, pos):
        labels.setdefault(name, []).append(pos)
        portal_at[pos] = name

    for (x, y), ch in list(grid.items()):
        if not ch.isupper():
            continue
        if grid.get((x + 1, y), ' ').isupper():
            name = ch + grid[(x + 1, y)]
            if grid.get((x - 1, y), '#') == '.':
                add_label(name, (x - 1, y))
            elif grid.get((x + 2, y), '#') == '.':
                add_label(name, (x + 2, y))
        if grid.get((x, y + 1), ' ').isupper():
            name = ch + grid[(x, y + 1)]
            if grid.get((x, y - 1), '#') == '.':
                add_label(name, (x, y - 1))
            elif grid.get((x, y + 2), '#') == '.':
                add_label(name, (x, y + 2))

    def neighbors(p):
        x, y = p
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + dx, y + dy)
            if grid.get(q) == '.':
                yield q

    # classify outer vs inner portal by position
    def is_outer(pos):
        x, y = pos
        if x <= 2 or y <= 2 or x >= max_x - 2 or y >= max_y - 2:
            return True
        return False

    start = labels['AA'][0]
    end = labels['ZZ'][0]

    from collections import deque
    dq = deque()
    dq.append((start, 0, 0))  # pos, level, dist
    seen = {(start, 0)}

    while dq:
        pos, level, d = dq.popleft()
        if pos == end and level == 0:
            return d
        # move normally
        for q in neighbors(pos):
            st = (q, level)
            if st not in seen:
                seen.add(st)
                dq.append((q, level, d + 1))
        # portal
        label = portal_at.get(pos)
        if label and label not in ('AA', 'ZZ'):
            ps = labels[label]
            other = ps[1] if ps[0] == pos else ps[0]
            if is_outer(pos):
                # going out decreases level
                if level > 0:
                    st = (other, level - 1)
                    if st not in seen:
                        seen.add(st)
                        dq.append((other, level - 1, d + 1))
            else:
                # inner -> increase level
                st = (other, level + 1)
                if st not in seen:
                    seen.add(st)
                    dq.append((other, level + 1, d + 1))

    return None


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
