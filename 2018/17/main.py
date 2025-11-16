import copy
import os
import queue
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
from pydoc import classify_class_attrs

import numpy as np


def solve(clay):
    min_y = min(y for x, y in clay)
    max_y = max(y for x, y in clay)
    part1 = set()

    # simulate water flow

    spring = (500, 0)
    flowing = set()
    still = set()

    # stack of sources to process (x, y)
    sources = [spring]

    while sources:
        sx, sy = sources.pop()

        # drop down until we hit clay, still water, or beyond max_y
        x, y = sx, sy
        while True:
            if y > max_y:
                # fell out of the scanned area
                break
            if (x, y) not in flowing:
                flowing.add((x, y))
            below = (x, y + 1)
            if below not in clay and below not in still:
                # can fall further
                y += 1
                continue
            # supported from below (clay or still water)
            break

        if y > max_y:
            continue

        # Now try to spread left and right from (x, y)
        while True:
            # expand left until clay or spill
            lx = x
            left_spill = False
            while True:
                pos = (lx - 1, y)
                below = (lx - 1, y + 1)
                if pos in clay:
                    break
                flowing.add(pos)
                if below not in clay and below not in still:
                    # will spill here
                    left_spill = True
                    sources.append((lx - 1, y))
                    break
                lx -= 1

            # expand right until clay or spill
            rx = x
            right_spill = False
            while True:
                pos = (rx + 1, y)
                below = (rx + 1, y + 1)
                if pos in clay:
                    break
                flowing.add(pos)
                if below not in clay and below not in still:
                    right_spill = True
                    sources.append((rx + 1, y))
                    break
                rx += 1

            # if neither side spills, region is bounded and becomes still water
            if not left_spill and not right_spill:
                for xx in range(lx, rx + 1):
                    still.add((xx, y))
                    flowing.discard((xx, y))
                # try to fill the row above
                if y - 1 >= 0:
                    sources.append((x, y - 1))
                break
            else:
                # unbounded: mark current span as flowing and stop
                for xx in range(lx, rx + 1):
                    flowing.add((xx, y))
                break

    # count tiles reached by water within min_y..max_y
    reached = {p for p in flowing.union(still) if min_y <= p[1] <= max_y}
    part1 = len(reached)

    print("Part 1:", part1)
    print("Part 2:", len(still))


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    clay = set()
    for line in lines:
        origin, segment = line.split(", ")
        fixed_coord, fixed_value = origin.split("=")
        range_coord, range_values = segment.split("=")
        range_start, range_end = map(int, range_values.split(".."))
        fixed_value = int(fixed_value)
        for v in range(range_start, range_end + 1):
            if fixed_coord == "x":
                clay.add((fixed_value, v))
            else:
                clay.add((v, fixed_value))
    solve(clay)
