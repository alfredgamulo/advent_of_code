#!/usr/bin/env python3
"""Fast solver for Advent of Code 2019 Day 18.

Approach:
- Parse grid, locate start and keys.
- For each important node (start + each key) run BFS to find reachable keys with distance
  and which doors (required keys) are on the path (as a bitmask).
- Run Dijkstra over state (current_node, collected_keys_bitmask) to find minimal steps to
  collect all keys.

This replaces a brute-force permutation approach which is infeasible on large inputs.
"""

import collections
import heapq
import string
from typing import Dict, Tuple


def read_input(file):
    with open(file) as f:
        return [line.rstrip('\n') for line in f]


def neighbors(pos):
    x, y = pos
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)


def bfs_from(start_pos, grid, keys_pos, doors_pos):
    """BFS from start_pos over grid. Return dict key_char -> (dist, required_keys_mask).

    required_keys_mask uses bit 0 for 'a', bit 25 for 'z'.
    """
    q = collections.deque()
    q.append((start_pos, 0, 0))
    seen = {start_pos}
    found = {}
    while q:
        pos, dist, req = q.popleft()
        # if we hit a key (and it's not the start), record it
        if pos in keys_pos and pos != start_pos:
            k = keys_pos[pos]
            found[k] = (dist, req)
        for nb in neighbors(pos):
            if nb in seen:
                continue
            if nb not in grid:
                continue
            cell = grid[nb]
            # if it's a door, add required key to mask
            nreq = req
            if nb in doors_pos:
                door_char = doors_pos[nb]
                nreq = req | (1 << (ord(door_char) - ord('a')))
            seen.add(nb)
            q.append((nb, dist + 1, nreq))
    return found


def solve(grid_lines):
    grid: Dict[Tuple[int, int], str] = {}
    keys_pos: Dict[Tuple[int, int], str] = {}
    doors_pos: Dict[Tuple[int, int], str] = {}
    starts = []

    for y, row in enumerate(grid_lines):
        for x, ch in enumerate(row):
            if ch != '#':
                grid[(x, y)] = ch
            if ch == '@':
                starts.append((x, y))
            elif ch in string.ascii_lowercase:
                keys_pos[(x, y)] = ch
            elif ch in string.ascii_uppercase:
                # store lowercase required key char
                doors_pos[(x, y)] = ch.lower()

    # map key char -> position for convenience
    key_char_to_pos = {v: k for k, v in keys_pos.items()}

    # create node labels for starts: @0, @1, ... and include keys
    nodes = {}
    for i, pos in enumerate(starts):
        nodes[f'@{i}'] = pos
    for ch, pos in key_char_to_pos.items():
        nodes[ch] = pos

    # precompute distances and required masks between nodes (only to keys)
    # graph_edges[src_char] = dict(target_key_char -> (dist, req_mask))
    graph_edges = {}
    for src_char, src_pos in nodes.items():
        found = bfs_from(src_pos, grid, keys_pos, doors_pos)
        graph_edges[src_char] = found

    all_keys_mask = 0
    for k in key_char_to_pos.keys():
        all_keys_mask |= 1 << (ord(k) - ord('a'))

    # Dijkstra over (tuple_of_robot_positions, keys_mask)
    start_positions = tuple(f'@{i}' for i in range(len(starts)))
    start_state = (start_positions, 0)
    heap = [(0, start_state)]
    dist_seen = {start_state: 0}

    while heap:
        steps, (robot_positions, keys_mask) = heapq.heappop(heap)
        if dist_seen.get((robot_positions, keys_mask), float('inf')) < steps:
            continue
        if keys_mask == all_keys_mask:
            return steps

        # for each robot, try to pick any key not yet collected
        for i, robot_pos in enumerate(robot_positions):
            for target_key, (d, req_mask) in graph_edges[robot_pos].items():
                key_bit = 1 << (ord(target_key) - ord('a'))
                # skip if we already have this key
                if keys_mask & key_bit:
                    continue
                # skip if required keys are not satisfied
                if (req_mask & keys_mask) != req_mask:
                    continue
                new_mask = keys_mask | key_bit
                new_positions = list(robot_positions)
                new_positions[i] = target_key
                new_positions = tuple(new_positions)
                new_state = (new_positions, new_mask)
                new_dist = steps + d
                if new_dist < dist_seen.get(new_state, float('inf')):
                    dist_seen[new_state] = new_dist
                    heapq.heappush(heap, (new_dist, new_state))

    return None


def main(path):
    grid = read_input(path)
    part1 = solve(grid)
    print('Part 1:', part1)

    # prepare map for part 2: replace the single starting position with walls
    # and place four new starting positions on the diagonals
    # find original start
    orig = None
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == '@':
                orig = (x, y)
                break
        if orig:
            break

    part2 = None
    if orig:
        x, y = orig
        # make a mutable copy
        grid2 = [list(r) for r in grid]
        # set center and N/S/E/W to walls
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            grid2[y + dy][x + dx] = '#'
        # set diagonals to new starts
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            grid2[y + dy][x + dx] = '@'
        grid2 = [''.join(r) for r in grid2]
        part2 = solve(grid2)
        print('Part 2:', part2)

    return (part1, part2)


if __name__ == '__main__':
    main('input')
