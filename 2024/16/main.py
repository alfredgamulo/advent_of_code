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
    # Parse the maze
    maze = [list(line) for line in lines]
    rows = len(maze)
    cols = len(maze[0])

    # Find start and end positions
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # Directions: East, South, West, North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # State: (score, row, col, direction_index)
    # direction_index: 0=East, 1=South, 2=West, 3=North
    # Start facing East (direction 0)

    # Priority queue: (score, row, col, direction_idx)
    pq = [(0, start[0], start[1], 0)]
    visited = {}  # (row, col, dir_idx) -> min_score

    while pq:
        score, r, c, dir_idx = heappop(pq)

        state = (r, c, dir_idx)
        if state in visited:
            continue
        visited[state] = score

        # If we reached the end facing any direction
        if (r, c) == end:
            return score

        # Option 1: Move forward in current direction
        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            new_state = (nr, nc, dir_idx)
            if new_state not in visited:
                heappush(pq, (score + 1, nr, nc, dir_idx))

        # Option 2: Turn clockwise (0->1->2->3->0)
        new_dir = (dir_idx + 1) % 4
        new_state = (r, c, new_dir)
        if new_state not in visited:
            heappush(pq, (score + 1000, r, c, new_dir))

        # Option 3: Turn counterclockwise (0->3->2->1->0)
        new_dir = (dir_idx - 1) % 4
        new_state = (r, c, new_dir)
        if new_state not in visited:
            heappush(pq, (score + 1000, r, c, new_dir))

    return -1  # No path found


def part2(lines):
    # Parse the maze
    maze = [list(line) for line in lines]
    rows = len(maze)
    cols = len(maze[0])

    # Find start and end positions
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # Directions: East, South, West, North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Dijkstra to find best scores
    pq = [(0, start[0], start[1], 0)]
    best_score = {}  # (row, col, dir_idx) -> min_score

    while pq:
        score, r, c, dir_idx = heappop(pq)

        state = (r, c, dir_idx)

        # If we've already found a better path to this state, skip
        if state in best_score:
            continue
        best_score[state] = score

        # Option 1: Move forward in current direction
        dr, dc = directions[dir_idx]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            new_state = (nr, nc, dir_idx)
            if new_state not in best_score:
                heappush(pq, (score + 1, nr, nc, dir_idx))

        # Option 2: Turn clockwise
        new_dir = (dir_idx + 1) % 4
        new_state = (r, c, new_dir)
        if new_state not in best_score:
            heappush(pq, (score + 1000, r, c, new_dir))

        # Option 3: Turn counterclockwise
        new_dir = (dir_idx - 1) % 4
        new_state = (r, c, new_dir)
        if new_state not in best_score:
            heappush(pq, (score + 1000, r, c, new_dir))

    # Find the best score to reach the end
    min_score_to_end = float('inf')
    for dir_idx in range(4):
        state = (end[0], end[1], dir_idx)
        if state in best_score:
            min_score_to_end = min(min_score_to_end, best_score[state])

    # Reverse Dijkstra: work backwards from end to find all cells on optimal paths
    # Priority queue for reverse search: (score, row, col, direction_idx)
    pq = []
    for dir_idx in range(4):
        state = (end[0], end[1], dir_idx)
        if state in best_score and best_score[state] == min_score_to_end:
            heappush(pq, (best_score[state], end[0], end[1], dir_idx))

    visited = set()
    tiles_on_path = set()

    while pq:
        score, r, c, dir_idx = heappop(pq)

        state = (r, c, dir_idx)

        if state in visited:
            continue
        visited.add(state)
        tiles_on_path.add((r, c))

        # Look for predecessors (reverse moves)
        # A predecessor could be:
        # 1. Previous position in same direction (moved forward)
        dr, dc = directions[dir_idx]
        pr, pc = r - dr, c - dc
        if 0 <= pr < rows and 0 <= pc < cols and maze[pr][pc] != '#':
            prev_state = (pr, pc, dir_idx)
            if prev_state in best_score and best_score[prev_state] + 1 == score:
                if prev_state not in visited:
                    heappush(pq, (best_score[prev_state], pr, pc, dir_idx))

        # 2. Same position, but rotated from counterclockwise direction
        prev_dir = (dir_idx - 1) % 4
        prev_state = (r, c, prev_dir)
        if prev_state in best_score and best_score[prev_state] + 1000 == score:
            if prev_state not in visited:
                heappush(pq, (best_score[prev_state], r, c, prev_dir))

        # 3. Same position, but rotated from clockwise direction
        prev_dir = (dir_idx + 1) % 4
        prev_state = (r, c, prev_dir)
        if prev_state in best_score and best_score[prev_state] + 1000 == score:
            if prev_state not in visited:
                heappush(pq, (best_score[prev_state], r, c, prev_dir))

    return len(tiles_on_path)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
