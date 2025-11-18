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
    text = "\n".join(lines)
    blocks = [b for b in text.split("\n\n") if b.strip()]
    tiles = {}
    for b in blocks:
        head, *grid = b.splitlines()
        tid = int(head.split()[1].strip(':'))
        tiles[tid] = grid

    # Build normalized edge -> list of tile ids
    edges = defaultdict(list)
    for tid, grid in tiles.items():
        top = grid[0]
        bottom = grid[-1]
        left = ''.join(r[0] for r in grid)
        right = ''.join(r[-1] for r in grid)
        for e in (top, bottom, left, right):
            norm = min(e, e[::-1])
            edges[norm].append(tid)

    corners = []
    for tid, grid in tiles.items():
        top = grid[0]
        bottom = grid[-1]
        left = ''.join(r[0] for r in grid)
        right = ''.join(r[-1] for r in grid)
        unique = 0
        for e in (top, bottom, left, right):
            if len(edges[min(e, e[::-1])]) == 1:
                unique += 1
        if unique == 2:
            corners.append(tid)

    prod_ids = 1
    for c in corners:
        prod_ids *= c
    return prod_ids


def part2(lines):
    text = "\n".join(lines)
    blocks = [b for b in text.split("\n\n") if b.strip()]
    tiles = {}
    for b in blocks:
        head, *grid = b.splitlines()
        tid = int(head.split()[1].strip(':'))
        tiles[tid] = grid

    # helper: rotate and flip
    def rotate(grid):
        n = len(grid)
        return [''.join(grid[n-1-r][c] for r in range(n)) for c in range(n)]

    def flip(grid):
        return [row[::-1] for row in grid]

    def orientations(grid):
        outs = []
        g = grid
        for _ in range(4):
            outs.append(g)
            outs.append(flip(g))
            g = rotate(g)
        # deduplicate
        seen = []
        uniq = []
        for o in outs:
            key = tuple(o)
            if key not in seen:
                seen.append(key)
                uniq.append(o)
        return uniq

    def edges_of(grid):
        top = grid[0]
        bottom = grid[-1]
        left = ''.join(r[0] for r in grid)
        right = ''.join(r[-1] for r in grid)
        return top, right, bottom, left

    N = int(len(tiles) ** 0.5)

    # Precompute orientations
    tile_orients = {tid: orientations(grid) for tid, grid in tiles.items()}

    placed = {}  # (r,c) -> (tid, grid)
    used = set()

    positions = [(r, c) for r in range(N) for c in range(N)]

    sys.setrecursionlimit(10000)

    def backtrack(idx=0):
        if idx == N * N:
            return True
        r, c = positions[idx]
        for tid, orients in tile_orients.items():
            if tid in used:
                continue
            for g in orients:
                top, right, bottom, left = edges_of(g)
                ok = True
                # check top neighbor
                if r > 0:
                    tid2, g2 = placed[(r-1, c)]
                    _, _, bottom2, _ = edges_of(g2)
                    if bottom2 != top:
                        ok = False
                if not ok:
                    continue
                # check left neighbor
                if c > 0:
                    tid2, g2 = placed[(r, c-1)]
                    _, right2, _, _ = edges_of(g2)
                    if right2 != left:
                        ok = False
                if not ok:
                    continue
                placed[(r, c)] = (tid, g)
                used.add(tid)
                if backtrack(idx+1):
                    return True
                used.remove(tid)
                del placed[(r, c)]
        return False

    ok = backtrack()
    if not ok:
        raise RuntimeError("Could not assemble tiles")

    # build full image without borders
    tile_size = len(next(iter(tiles.values())))
    inner = tile_size - 2
    image_rows = []
    for tr in range(N):
        # collect inner rows for each tile row
        rows_block = ['' for _ in range(inner)]
        for tc in range(N):
            tid, g = placed[(tr, tc)]
            # strip borders
            stripped = [row[1:-1] for row in g[1:-1]]
            for i in range(inner):
                rows_block[i] += stripped[i]
        image_rows.extend(rows_block)

    # sea monster pattern
    monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
    monster_coords = [(r, c) for r, line in enumerate(monster) for c, ch in enumerate(line) if ch == '#']
    H = len(image_rows)
    W = len(image_rows[0])

    def search_monsters(grid):
        count = 0
        for r in range(H - len(monster) + 1):
            for c in range(W - len(monster[0]) + 1):
                if all(grid[r+dr][c+dc] == '#' for dr, dc in monster_coords):
                    count += 1
        return count

    # try all orientations of the full image
    full_orients = orientations(image_rows)
    found = 0
    for fo in full_orients:
        found = search_monsters(fo)
        if found:
            rough = sum(row.count('#') for row in fo) - found * len(monster_coords)
            return rough

    # if none found, return None or 0
    return None


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
