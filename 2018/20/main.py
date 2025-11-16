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

import numpy as np


def part1(lines):
    regex = lines[0].strip()
    graph = build_graph(regex)
    dist = bfs_distances(graph, (0, 0))
    return max(dist.values())


def part2(lines):
    regex = lines[0].strip()
    graph = build_graph(regex)
    dist = bfs_distances(graph, (0, 0))
    return sum(1 for d in dist.values() if d >= 1000)


def build_graph(regex):
    """Parse the regex and build an undirected graph of rooms.

    Rooms are points (x,y). Moves N/S/E/W add edges between adjacent rooms.
    Parentheses and | create branches. ^ and $ are ignored.
    """
    # strip anchors
    if regex.startswith("^"):
        regex = regex[1:]
    if regex.endswith("$"):
        regex = regex[:-1]

    dirs = {"N": (0, -1), "S": (0, 1), "W": (-1, 0), "E": (1, 0)}
    graph = defaultdict(set)

    positions = {(0, 0)}
    stack = []  # each element: (entry_positions, accumulated_branch_ends)

    for ch in regex:
        if ch == '(':
            # start a group; record entry positions and empty set for ends
            stack.append((positions.copy(), set()))
        elif ch == '|':
            # add current branch end positions to accumulated ends and reset to entry
            entry_positions, ends = stack[-1]
            ends |= positions
            stack[-1] = (entry_positions, ends)
            positions = entry_positions.copy()
        elif ch == ')':
            entry_positions, ends = stack.pop()
            ends |= positions
            positions = ends
        elif ch in dirs:
            dx, dy = dirs[ch]
            new_positions = set()
            for (x, y) in positions:
                nx, ny = x + dx, y + dy
                # connect both ways
                graph[(x, y)].add((nx, ny))
                graph[(nx, ny)].add((x, y))
                new_positions.add((nx, ny))
            positions = new_positions
        else:
            # ignore any other characters (shouldn't be any)
            pass

    if stack:
        raise ValueError("Unbalanced parentheses in regex")

    return graph


def bfs_distances(graph, start):
    """Return dict of shortest distances (in edges) from start to all reachable nodes."""
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
