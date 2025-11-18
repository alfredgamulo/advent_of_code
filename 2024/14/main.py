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


def part1(lines):
    width, height = 101, 103
    seconds = 100
    robots = []
    for line in lines:
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if m:
            x, y, vx, vy = map(int, m.groups())
            robots.append((x, y, vx, vy))

    # Middle column and row
    mid_x = width // 2
    mid_y = height // 2

    quadrant_counts = [0, 0, 0, 0]  # TL, TR, BL, BR
    for x, y, vx, vy in robots:
        # Calculate new position after 100 seconds, wrapping
        nx = (x + vx * seconds) % width
        ny = (y + vy * seconds) % height
        # Exclude robots on the middle row or column
        if nx == mid_x or ny == mid_y:
            continue
        # Determine quadrant
        if nx < mid_x and ny < mid_y:
            quadrant_counts[0] += 1  # Top-left
        elif nx > mid_x and ny < mid_y:
            quadrant_counts[1] += 1  # Top-right
        elif nx < mid_x and ny > mid_y:
            quadrant_counts[2] += 1  # Bottom-left
        elif nx > mid_x and ny > mid_y:
            quadrant_counts[3] += 1  # Bottom-right
        # If not in any quadrant (shouldn't happen), skip

    # Safety factor is product of quadrant counts
    from math import prod
    return prod(quadrant_counts)


def part2(lines):
    # Parse positions and velocities. Accept both common AoC formats.
    robots = []
    for line in lines:
        m = re.match(r"p=<\s*(-?\d+),\s*(-?\d+)\s*> v=<\s*(-?\d+),\s*(-?\d+)\s*>", line)
        if not m:
            m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if m:
            x, y, vx, vy = map(int, m.groups())
            robots.append((x, y, vx, vy))

    if not robots:
        return None

    # Use the same wrapping/grid parameters as part1 (observed in this puzzle)
    width, height = 101, 103

    def minimal_circular_span(coords, limit):
        # coords: iterable of integer coordinates in [0, limit-1]
        vals = sorted(set(coords))
        if not vals:
            return 0, 0
        # compute largest gap between successive coords (circular)
        max_gap = -1
        max_gap_end = None
        for i in range(len(vals)):
            a = vals[i]
            b = vals[(i + 1) % len(vals)]
            gap = (b - a - 1) % limit
            if gap > max_gap:
                max_gap = gap
                # end of max_gap is a
                max_gap_end = a
        # minimal span covering all points contiguously on circle
        span = limit - max_gap
        # start coordinate is (max_gap_end + 1) mod limit
        start = (max_gap_end + 1) % limit
        return span, start

    best_t = None
    best_row_span = None
    best_col_span = None
    best_ranges = None

    max_t = 5099900
    for t in range(max_t + 1):
        pos = [((x + vx * t) % width, (y + vy * t) % height) for x, y, vx, vy in robots]
        xs = [p[0] for p in pos]
        ys = [p[1] for p in pos]

        row_span, row_start = minimal_circular_span(ys, height)
        col_span, col_start = minimal_circular_span(xs, width)

        # Heuristic: message occurs when row_span is minimal (points compressed vertically)
        if best_row_span is None or row_span < best_row_span or (row_span == best_row_span and col_span < best_col_span):
            best_row_span = row_span
            best_col_span = col_span
            best_t = t
            best_ranges = (row_start, row_span, col_start, col_span)

    # Render the message at best_t
    if best_ranges is None:
        return None

    row_start, row_span, col_start, col_span = best_ranges
    # clamp spans to reasonable maximum when rendering
    if row_span > height or col_span > width:
        return best_t

    # Build grid
    grid = [["." for _ in range(col_span)] for _ in range(row_span)]
    pos = [((x + vx * best_t) % width, (y + vy * best_t) % height) for x, y, vx, vy in robots]
    for x, y in pos:
        rx = (x - col_start) % width
        ry = (y - row_start) % height
        if 0 <= rx < col_span and 0 <= ry < row_span:
            grid[ry][rx] = "#"

    print("\nMessage at t=", best_t)
    for row in grid:
        print("".join(row))

    return best_t


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
