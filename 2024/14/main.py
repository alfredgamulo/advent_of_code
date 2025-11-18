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
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
