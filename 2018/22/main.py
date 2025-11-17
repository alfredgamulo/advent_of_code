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
from typing import Dict, Tuple


def parse(lines):
    d = int(lines[0].split(':')[1].strip())
    t = lines[1].split(':')[1].strip()
    tx, ty = map(int, t.split(','))
    return d, (tx, ty)


def make_erosion(depth: int, target: Tuple[int, int]):
    tx, ty = target
    memo: Dict[Tuple[int, int], int] = {}

    def erosion(x: int, y: int) -> int:
        if (x, y) in memo:
            return memo[(x, y)]
        if (x, y) == (0, 0) or (x, y) == (tx, ty):
            gi = 0
        elif y == 0:
            gi = x * 16807
        elif x == 0:
            gi = y * 48271
        else:
            gi = erosion(x - 1, y) * erosion(x, y - 1)
        el = (gi + depth) % 20183
        memo[(x, y)] = el
        return el

    return erosion


def region_type_from_erosion(el: int) -> int:
    return el % 3


def part1(lines):
    depth, target = parse(lines)
    tx, ty = target
    erosion = make_erosion(depth, target)
    total = 0
    for y in range(0, ty + 1):
        for x in range(0, tx + 1):
            total += region_type_from_erosion(erosion(x, y))
    return total


def part2(lines):
    depth, target = parse(lines)
    tx, ty = target
    erosion = make_erosion(depth, target)

    # tools: 0 = neither, 1 = climbing gear, 2 = torch
    allowed = {
        0: {1, 2},  # rocky: climbing, torch
        1: {0, 1},  # wet: neither, climbing
        2: {0, 2},  # narrow: neither, torch
    }

    import heapq

    # bounds: heuristic margin
    max_x = tx + 100
    max_y = ty + 100

    def get_type(x, y):
        if x < 0 or y < 0 or x > max_x or y > max_y:
            return None
        return region_type_from_erosion(erosion(x, y))

    start = (0, 0, 2)  # at mouth with torch
    target_state = (tx, ty, 2)  # must end with torch

    pq = [(0, start)]
    dist = {start: 0}

    while pq:
        ttime, (x, y, tool) = heapq.heappop(pq)
        if dist.get((x, y, tool), float('inf')) < ttime:
            continue
        if (x, y, tool) == target_state:
            return ttime

        # consider switching tools
        rtype = get_type(x, y)
        for nt in allowed[rtype]:
            if nt != tool:
                ntime = ttime + 7
                state = (x, y, nt)
                if ntime < dist.get(state, float('inf')):
                    dist[state] = ntime
                    heapq.heappush(pq, (ntime, state))

        # consider moving
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > max_x or ny > max_y:
                continue
            nt = get_type(nx, ny)
            if nt is None:
                continue
            # can we keep current tool in the new region?
            if tool in allowed[nt]:
                ntime = ttime + 1
                state = (nx, ny, tool)
                if ntime < dist.get(state, float('inf')):
                    dist[state] = ntime
                    heapq.heappush(pq, (ntime, state))

    raise RuntimeError('No path found')


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
