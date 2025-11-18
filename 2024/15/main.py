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
    # Parse input: first block is the map, then (after possibly blank line) the moves.
    map_lines = []
    moves_lines = []
    mode = "map"
    for line in lines:
        s = line.rstrip("\n")
        if mode == "map":
            if s == "":
                continue
            # if this line looks like moves (only move chars), switch
            if set(s) <= set("<>^v"):
                mode = "moves"
                moves_lines.append(s)
            else:
                map_lines.append(s)
        else:
            moves_lines.append(s)

    if not map_lines:
        return None

    # Build grid
    grid = [list(r) for r in map_lines]
    h = len(grid)
    w = len(grid[0])

    # find robot
    ry = rx = None
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '@':
                ry, rx = y, x
                break
        if ry is not None:
            break

    if ry is None:
        raise ValueError("No robot '@' found in map")

    moves = "".join(moves_lines).strip()

    dir_map = {
        '^': ( -1,  0),
        'v': (  1,  0),
        '<': (  0, -1),
        '>': (  0,  1),
    }

    for mv in moves:
        if mv not in dir_map:
            continue
        dy, dx = dir_map[mv]
        ny = ry + dy
        nx = rx + dx
        # out-of-bounds treated as wall
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        target = grid[ny][nx]
        if target == '#':
            # blocked
            continue
        if target == '.':
            # simple move
            grid[ry][rx] = '.'
            grid[ny][nx] = '@'
            ry, rx = ny, nx
            continue
        if target == 'O':
            # collect chain of boxes
            chain = []
            by, bx = ny, nx
            while 0 <= by < h and 0 <= bx < w and grid[by][bx] == 'O':
                chain.append((by, bx))
                by += dy
                bx += dx
            # now by,bx is first non-O cell in that direction
            if not (0 <= by < h and 0 <= bx < w):
                # would go out of bounds -> blocked
                continue
            if grid[by][bx] == '#':
                # blocked by wall
                continue
            if grid[by][bx] in ('.',):
                # can push: move boxes from end to front
                for (oby, obx) in reversed(chain):
                    ny2 = oby + dy
                    nx2 = obx + dx
                    grid[ny2][nx2] = 'O'
                    grid[oby][obx] = '.'
                # move robot
                grid[ry][rx] = '.'
                grid[ny][nx] = '@'
                ry, rx = ny, nx
                continue
            # any other content (shouldn't happen) treat as blocked
            continue

    # After moves, compute sum of GPS coordinates for all boxes
    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'O':
                total += 100 * y + x
    return total


def part2(lines):
    # Build map and moves like part1
    map_lines = []
    moves_lines = []
    mode = "map"
    for line in lines:
        s = line.rstrip("\n")
        if mode == "map":
            if s == "":
                continue
            if set(s) <= set("<>^v"):
                mode = "moves"
                moves_lines.append(s)
            else:
                map_lines.append(s)
        else:
            moves_lines.append(s)

    if not map_lines:
        return None

    h = len(map_lines)
    w_orig = len(map_lines[0])
    # expanded width is twice original
    w = w_orig * 2

    # create walls set and boxes set (boxes tracked by left column index)
    walls = set()
    boxes = set()
    ry = rx = None
    for y, row in enumerate(map_lines):
        for x, ch in enumerate(row):
            ex = x * 2
            if ch == '#':
                walls.add((y, ex))
                walls.add((y, ex + 1))
            elif ch == 'O':
                # box occupies ex and ex+1, track left coordinate
                boxes.add((y, ex))
            elif ch == '@':
                # robot occupies left of the pair
                ry = y
                rx = ex
            # '.' ignored

    moves = "".join(moves_lines).strip()

    def get_box_at_cell(y, x):
        # return box left coordinate (y,left) if cell (y,x) is part of a box
        # a box occupies (y,left) and (y,left+1)
        if (y, x) in boxes:
            return (y, x)
        if (y, x - 1) in boxes:
            return (y, x - 1)
        return None

    def cell_is_wall(y, x):
        return (y, x) in walls

    # Use BFS to find all boxes affected by a push in direction (dy, dx)
    def find_boxes_to_move(start_box, dy, dx):
        queue = deque([start_box])
        visited = {start_box}
        result = {start_box}

        while queue:
            by, bleft = queue.popleft()
            tby = by + dy
            tbleft = bleft + dx

            # Check if target cells are in bounds
            if not (0 <= tby < h and 0 <= tbleft and tbleft + 1 < w):
                return None  # Out of bounds = blocked

            # Check if target cells hit a wall
            if cell_is_wall(tby, tbleft) or cell_is_wall(tby, tbleft + 1):
                return None  # Wall = blocked

            # Find boxes in target cells
            for tx in [tbleft, tbleft + 1]:
                b = get_box_at_cell(tby, tx)
                if b is not None and b not in visited:
                    visited.add(b)
                    result.add(b)
                    queue.append(b)

        return list(result)

    dir_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    for mv in moves:
        if mv not in dir_map:
            continue
        dy, dx = dir_map[mv]
        ny = ry + dy
        nx = rx + dx
        # bounds
        if not (0 <= ny < h and 0 <= nx < w):
            continue
        if cell_is_wall(ny, nx):
            continue
        b = get_box_at_cell(ny, nx)
        if b is None:
            # empty, move robot
            ry, rx = ny, nx
            continue
        # Find all boxes that need to move
        to_move = find_boxes_to_move(b, dy, dx)
        if to_move is None:
            continue
        # Sort boxes so we move them in the right order to avoid collision
        # For up (dy=-1): move top boxes first (ascending row)
        # For down (dy=1): move bottom boxes first (descending row)
        # For left (dx=-1): move left boxes first (ascending col)
        # For right (dx=1): move right boxes first (descending col)
        if dy < 0 or dx < 0:
            to_move_sorted = sorted(to_move)
        else:
            to_move_sorted = sorted(to_move, reverse=True)

        for by, bleft in to_move_sorted:
            boxes.discard((by, bleft))
            boxes.add((by + dy, bleft + dx))
        # move robot into the cell
        ry, rx = ny, nx

    # Compute GPS sum: for each box, use its top row and leftmost column
    total = 0
    for by, bleft in boxes:
        total += 100 * by + bleft
    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
