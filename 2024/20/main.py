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
    # parse grid
    grid = [list(l) for l in lines]
    R = len(grid)
    C = len(grid[0]) if R else 0
    start = end = None
    tracks = set()
    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch in ('.', 'S', 'E'):
                tracks.add((r, c))
            if ch == 'S':
                start = (r, c)
            elif ch == 'E':
                end = (r, c)

    if start is None or end is None:
        return None

    # BFS on tracks only
    from collections import deque

    def bfs_sources(src):
        dist = {src: 0}
        q = deque([src])
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) in tracks and (nr, nc) not in dist:
                    dist[(nr, nc)] = dist[(r, c)] + 1
                    q.append((nr, nc))
        return dist

    distS = bfs_sources(start)
    distE = bfs_sources(end)

    if end not in distS:
        # unreachable even without cheating
        return 0

    baseline = distS[end]

    # For each track cell as cheat start, enumerate end cells reachable in 1 or 2 moves
    cheats = {}
    for s in list(tracks):
        if s not in distS:
            continue
        r, c = s
        # length 1 moves
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            r1, c1 = r+dr, c+dc
            if not (0 <= r1 < R and 0 <= c1 < C):
                continue
            # end must be a track cell
            if (r1, c1) in tracks:
                # cheat from s -> (r1,c1) with length 1
                cheats[(s, (r1, c1))] = 1
            # length 2: second step from (r1,c1)
            for dr2, dc2 in ((1,0),(-1,0),(0,1),(0,-1)):
                r2, c2 = r1+dr2, c1+dc2
                if not (0 <= r2 < R and 0 <= c2 < C):
                    continue
                if (r2, c2) in tracks:
                    # cheat from s -> (r2,c2) with length 2
                    # if already present with length 1, keep 1
                    prev = cheats.get((s, (r2, c2)))
                    if prev is None or prev > 2:
                        cheats[(s, (r2, c2))] = 2

    # Count cheats that save at least 100 picoseconds
    count = 0
    for (s, epos), clen in cheats.items():
        if epos not in distE:
            continue
        time = distS[s] + clen + distE[epos]
        save = baseline - time
        if save >= 100:
            count += 1

    return count


def part2(lines):
    # parse grid
    grid = [list(l) for l in lines]
    R = len(grid)
    C = len(grid[0]) if R else 0
    start = end = None
    tracks = set()
    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch in ('.', 'S', 'E'):
                tracks.add((r, c))
            if ch == 'S':
                start = (r, c)
            elif ch == 'E':
                end = (r, c)

    if start is None or end is None:
        return None

    from collections import deque

    # BFS on tracks only
    def bfs_sources(src):
        dist = {src: 0}
        q = deque([src])
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) in tracks and (nr, nc) not in dist:
                    dist[(nr, nc)] = dist[(r, c)] + 1
                    q.append((nr, nc))
        return dist

    distS = bfs_sources(start)
    distE = bfs_sources(end)

    if end not in distS:
        return 0

    baseline = distS[end]

    # BFS in full grid (ignore walls) up to maxd steps from a source
    def bfs_full_limited(src, maxd=20):
        dist = {src: 0}
        q = deque([src])
        while q:
            r, c = q.popleft()
            d = dist[(r, c)]
            if d >= maxd:
                continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in dist:
                    dist[(nr, nc)] = d + 1
                    q.append((nr, nc))
        return dist

    seen_pairs = set()
    count = 0

    # For each possible cheat start reachable from S, run limited full-grid BFS
    for s in list(tracks):
        if s not in distS:
            continue
        # BFS ignoring walls up to 20
        fulldist = bfs_full_limited(s, maxd=20)
        for epos, d in fulldist.items():
            if d == 0:
                continue
            if d > 20:
                continue
            if epos not in tracks:
                continue
            if epos not in distE:
                continue
            pair = (s, epos)
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            time = distS[s] + d + distE[epos]
            save = baseline - time
            if save >= 100:
                count += 1

    return count


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
