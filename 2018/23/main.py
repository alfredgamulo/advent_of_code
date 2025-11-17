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
from typing import List, Tuple


def parse(lines: List[str]) -> List[Tuple[int, int, int, int]]:
    bots = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # pos=<x,y,z>, r=R
        p, rpart = line.split('>,')
        coords = p[p.find('<')+1:]
        x, y, z = map(int, coords.split(','))
        r = int(rpart.split('=')[1])
        bots.append((x, y, z, r))
    return bots


def part1(lines):
    bots = parse(lines)
    # find strongest
    bx, by, bz, br = max(bots, key=lambda b: b[3])
    def man(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
    cnt = 0
    for x, y, z, r in bots:
        if abs(x-bx) + abs(y-by) + abs(z-bz) <= br:
            cnt += 1
    return cnt


def cube_distance_to_point(cube, point):
    # cube: (x0,x1,y0,y1,z0,z1) inclusive
    x0, x1, y0, y1, z0, z1 = cube
    x, y, z = point
    d = 0
    if x < x0:
        d += x0 - x
    elif x > x1:
        d += x - x1
    if y < y0:
        d += y0 - y
    elif y > y1:
        d += y - y1
    if z < z0:
        d += z0 - z
    elif z > z1:
        d += z - z1
    return d


def count_bots_in_range_of_cube(bots, cube):
    # count bots whose range intersects cube
    cnt = 0
    for bx, by, bz, br in bots:
        if cube_distance_to_point(cube, (bx, by, bz)) <= br:
            cnt += 1
    return cnt


def part2(lines):
    bots = parse(lines)
    xs = [b[0] for b in bots]
    ys = [b[1] for b in bots]
    zs = [b[2] for b in bots]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    minz, maxz = min(zs), max(zs)

    # expand to include origin
    minx = min(minx, 0)
    miny = min(miny, 0)
    minz = min(minz, 0)
    maxx = max(maxx, 0)
    maxy = max(maxy, 0)
    maxz = max(maxz, 0)

    # start with a cube size that's power of two
    size = 1
    max_range = max(maxx - minx, maxy - miny, maxz - minz)
    while size < max_range:
        size *= 2

    import heapq

    # priority queue: (-count, distance_to_origin, size, x0, y0, z0)
    pq = []
    # initial cube origin at multiples of size covering the range
    x0 = minx
    y0 = miny
    z0 = minz
    # align to multiples of size
    x0 = (x0 // size) * size
    y0 = (y0 // size) * size
    z0 = (z0 // size) * size

    def push_cube(x0, y0, z0, size):
        cube = (x0, x0+size-1, y0, y0+size-1, z0, z0+size-1)
        cnt = count_bots_in_range_of_cube(bots, cube)
        dist = cube_distance_to_point(cube, (0,0,0))
        # use negative count so heapq is max-heap by count
        heapq.heappush(pq, (-cnt, dist, size, x0, y0, z0))

    # push all initial cubes that cover the whole bounding box
    rx = range(x0, maxx+1, size)
    ry = range(y0, maxy+1, size)
    rz = range(z0, maxz+1, size)
    for xi in rx:
        for yi in ry:
            for zi in rz:
                push_cube(xi, yi, zi, size)

    best_point = None
    best_count = 0
    best_dist = None

    while pq:
        negcnt, dist, sz, x0, y0, z0 = heapq.heappop(pq)
        cnt = -negcnt
        if best_count > cnt:
            # cannot improve
            break
        if sz == 1:
            # single point
            x, y, z = x0, y0, z0
            # update best
            if cnt > best_count or (cnt == best_count and (best_dist is None or dist < best_dist)):
                best_count = cnt
                best_point = (x, y, z)
                best_dist = dist
            # once we've found point with max possible count, and pq entries have <= cnt, we can finish
            if best_count == cnt:
                # continue to pop to find possibly smaller distance with same count
                continue
            else:
                continue
        # split cube into 8 subcubes
        half = sz // 2
        for dx in (0, half):
            for dy in (0, half):
                for dz in (0, half):
                    nx = x0 + dx
                    ny = y0 + dy
                    nz = z0 + dz
                    push_cube(nx, ny, nz, half)

    # best_point should be found; return distance to origin
    if best_point is None:
        return None
    x, y, z = best_point
    return abs(x) + abs(y) + abs(z)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
