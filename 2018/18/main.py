import copy
import os
import re
import string
import sys
from ast import parse
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

def solve(ground, trees, lumberyards):
    # The top-level __main__ in this file currently loops in a way that may
    # pass an unexpected value into this function (the loop in __main__ calls
    # parse(line) for each line and ends up passing only the last one). To be
    # robust, re-read and parse the full input file here using sys.argv[1]
    # so the solver always has the complete grid.
    path = Path(sys.argv[1])
    lines = path.read_text().splitlines()

    # parse full grid into a list of rows
    grid = [list(l) for l in lines]
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    # neighbor offsets
    neigh = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def step(g):
        new = [row.copy() for row in g]
        for y in range(height):
            for x in range(width):
                counts = {'.': 0, '|': 0, '#': 0}
                for dx, dy in neigh:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        counts[g[ny][nx]] += 1

                cur = g[y][x]
                if cur == '.':
                    # open -> trees if 3+ adjacent trees
                    new[y][x] = '|' if counts['|'] >= 3 else '.'
                elif cur == '|':
                    # trees -> lumberyard if 3+ adjacent lumberyards
                    new[y][x] = '#' if counts['#'] >= 3 else '|'
                elif cur == '#':
                    # lumberyard stays if adjacent to at least one lumberyard and one tree
                    new[y][x] = '#' if (counts['#'] >= 1 and counts['|'] >= 1) else '.'
        return new

    # Part 1: resource value after 10 minutes
    # Part 2: resource value after 1_000_000_000 minutes (use cycle detection)
    target1 = 10
    target2 = 1000000000

    def state_str(g):
        return ''.join(''.join(row) for row in g)

    g = grid
    states = [state_str(g)]
    seen = {states[0]: 0}
    part1_value = None
    final_state_str = None

    for minute in range(1, target2 + 1):
        g = step(g)
        s = state_str(g)
        if minute == target1:
            trees_count = s.count('|')
            lumber_count = s.count('#')
            part1_value = trees_count * lumber_count

        if s in seen:
            # cycle detected from seen[s] .. minute-1
            cycle_start = seen[s]
            cycle_len = minute - cycle_start
            # compute index of the state at target2
            if target2 >= cycle_start:
                final_index = cycle_start + ((target2 - cycle_start) % cycle_len)
            else:
                final_index = target2
            final_state_str = states[final_index]
            break
        else:
            seen[s] = minute
            states.append(s)

    if final_state_str is None:
        # no cycle found within target2 iterations (unlikely); use last state
        final_state_str = states[-1]

    if part1_value is None:
        # If we detected a cycle before reaching target1, compute its index
        if target1 < len(states):
            s1 = states[target1]
        else:
            # cycle must exist; compute index
            cycle_start = seen[states[-1]]
            cycle_len = len(states) - cycle_start
            idx = cycle_start + ((target1 - cycle_start) % cycle_len)
            s1 = states[idx]
        part1_value = s1.count('|') * s1.count('#')

    part2_value = final_state_str.count('|') * final_state_str.count('#')

    print("Part 1:", part1_value)
    print("Part 2:", part2_value)
    return part1_value, part2_value


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    def parse(l):
        ground = set()
        trees = set()
        lumberyards = set()
        for y, row in enumerate(l):
            for x, c in enumerate(row):
                if c == '.':
                    ground.add((x, y))
                elif c == '|':
                    trees.add((x, y))
                elif c == '#':
                    lumberyards.add((x, y))
        return ground, trees, lumberyards
    for line in lines:
        ground, trees, lumberyards = parse(line)

    solve(ground, trees, lumberyards)
