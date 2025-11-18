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
    # Parse first 1024 coordinates
    corrupted = []
    for i, line in enumerate(lines):
        if i >= 1024:
            break
        x, y = map(int, line.strip().split(","))
        corrupted.append((x, y))

    # Build grid
    grid = [[False for _ in range(71)] for _ in range(71)]
    for x, y in corrupted:
        grid[y][x] = True

    # BFS
    from collections import deque
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, steps)
    visited = set()
    visited.add((0, 0))
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == (70, 70):
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # No path found


def part2(lines):
    grid = [[False for _ in range(71)] for _ in range(71)]
    from collections import deque
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    def has_path():
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        while queue:
            x, y = queue.popleft()
            if (x, y) == (70, 70):
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 71 and 0 <= ny < 71 and not grid[ny][nx] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False
    for i, line in enumerate(lines):
        x, y = map(int, line.strip().split(","))
        grid[y][x] = True
        if not has_path():
            return f"{x},{y}"
    return None


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
