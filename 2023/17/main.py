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
from math import ceil, floor, inf, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter


@cache
def solve(pos, prev_dir, straight_moves, count = 0):
        print("---->", pos)
        if pos == end:
            return 0
        x, y = pos
        heats = []
        for dx, dy, dir in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0])  or (dir == prev_dir and straight_moves < 3):
                breakpoint()
                heats.append(int(grid[x][y]) + solve((nx, ny), dir, straight_moves + 1 if dir == prev_dir else 0, count +1))
        return min(heats) if heats else inf

    
def part1():
    return solve((0,0), None, 0)
    


def part2():
    ...


if __name__ == "__main__":
    grid = Path(sys.argv[1]).read_text().splitlines()
    end = (len(grid)-1, len(grid[0])-1)
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    print("Part 1:", part1())
    print("Part 2:", part2())
