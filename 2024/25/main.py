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
    # Split input by blank lines to get individual schematics
    schematics = []
    current = []
    for line in lines:
        if line.strip():
            current.append(line)
        else:
            if current:
                schematics.append(current)
                current = []
    if current:
        schematics.append(current)

    locks = []
    keys = []

    for schematic in schematics:
        # Determine if it's a lock or key
        is_lock = schematic[0] == "#####"

        # Calculate heights for each column
        heights = []
        for col in range(5):
            height = 0
            for row in range(len(schematic)):
                if schematic[row][col] == "#":
                    height += 1
            # Subtract 1 because the top or bottom row is always filled
            heights.append(height - 1)

        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    # Count matching pairs
    count = 0
    for lock in locks:
        for key in keys:
            # Check if key fits in lock (no overlap in any column)
            fits = True
            for i in range(5):
                if lock[i] + key[i] > 5:
                    fits = False
                    break
            if fits:
                count += 1

    return count


def part2(lines):
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
