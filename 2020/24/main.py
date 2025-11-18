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
    # Parse directions and flip tiles. Return number of black tiles.
    dirs_re = re.compile(r"se|sw|ne|nw|e|w")
    # axial coordinates (x, y)
    deltas = {
        "e": (1, 0),
        "w": (-1, 0),
        "ne": (0, -1),
        "nw": (-1, -1),
        "se": (1, 1),
        "sw": (0, 1),
    }

    black = set()
    for line in lines:
        if not line:
            continue
        moves = dirs_re.findall(line.strip())
        x = y = 0
        for m in moves:
            dx, dy = deltas[m]
            x += dx
            y += dy
        pos = (x, y)
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)

    return len(black)


def part2(lines):
    # Build initial black tile set using part1 logic (reuse parser)
    dirs_re = re.compile(r"se|sw|ne|nw|e|w")
    deltas = {
        "e": (1, 0),
        "w": (-1, 0),
        "ne": (0, -1),
        "nw": (-1, -1),
        "se": (1, 1),
        "sw": (0, 1),
    }

    black = set()
    for line in lines:
        if not line:
            continue
        moves = dirs_re.findall(line.strip())
        x = y = 0
        for m in moves:
            dx, dy = deltas[m]
            x += dx
            y += dy
        pos = (x, y)
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)

    # neighbors helper
    neighbor_deltas = list(deltas.values())

    for _day in range(100):
        counts = Counter()
        # Count black neighbors for each tile around blacks
        for x, y in black:
            for dx, dy in neighbor_deltas:
                counts[(x + dx, y + dy)] += 1

        new_black = set()
        # Consider all tiles that have any black neighbor plus existing blacks
        tiles_to_consider = set(counts.keys()) | set(black)
        for tile in tiles_to_consider:
            n = counts.get(tile, 0)
            if tile in black:
                # black tile stays black only if 1 or 2 black neighbors
                if n == 1 or n == 2:
                    new_black.add(tile)
            else:
                # white tile becomes black if exactly 2 black neighbors
                if n == 2:
                    new_black.add(tile)

        black = new_black

    return len(black)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
