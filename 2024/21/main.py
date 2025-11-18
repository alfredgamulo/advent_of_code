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
    """
    Strategy: recursively compute cost.
    To type a numeric code like "129A" on the numeric keypad (level 3), we need
    level 2 (a directional keypad controller) to type a sequence of directions+A.
    To type that sequence on level 2, we need level 1 to control it.
    To type that sequence on level 1, we need level 0 (me) to control it.
    """

    def make_directional():
        rows = [ [None, '^', 'A'], ['<', 'v', '>'] ]
        pos_to_label = {}
        label_to_pos = {}
        for y, row in enumerate(rows):
            for x, v in enumerate(row):
                if v is not None:
                    pos_to_label[(x, y)] = v
                    label_to_pos[v] = (x, y)
        return pos_to_label, label_to_pos, label_to_pos['A']

    def make_numeric():
        rows = [ ['7','8','9'], ['4','5','6'], ['1','2','3'], [None,'0','A'] ]
        pos_to_label = {}
        label_to_pos = {}
        for y, row in enumerate(rows):
            for x, v in enumerate(row):
                if v is not None:
                    pos_to_label[(x, y)] = v
                    label_to_pos[v] = (x, y)
        return pos_to_label, label_to_pos, label_to_pos['A']

    dir_pos2label, dir_label2pos, dir_A = make_directional()
    num_pos2label, num_label2pos, num_A = make_numeric()

    @cache
    def bfs_paths(start, end, keypad_type):
        """Find all shortest paths (as strings) on keypad from start to end."""
        if keypad_type == 'dir':
            pos2label = dir_pos2label
        else:
            pos2label = num_pos2label

        if start == end:
            return ['']

        from collections import deque
        dq = deque()
        dq.append((start, ''))
        visited = {start: 0}
        paths = []
        min_len = None

        while dq:
            pos, path = dq.popleft()

            if min_len is not None and len(path) > min_len:
                continue

            if pos == end:
                if min_len is None:
                    min_len = len(path)
                if len(path) == min_len:
                    paths.append(path)
                continue

            x, y = pos
            for d, (dx, dy) in [('<', (-1, 0)), ('>', (1, 0)), ('^', (0, -1)), ('v', (0, 1))]:
                np = (x + dx, y + dy)
                if np not in pos2label:
                    continue
                new_path = path + d
                if np not in visited or visited[np] >= len(new_path):
                    visited[np] = len(new_path)
                    dq.append((np, new_path))

        return paths

    @cache
    def min_cost_to_type(seq, level):
        """
        Min **presses** on keypad at `level` needed to have keypad at `level+1`
        produce the sequence `seq`.

        level 0: my directional keypad (what I press)
        level 1: robot1's directional keypad
        level 2: robot2's directional keypad
        level 3: robot3's numeric keypad (what types the final code)

        When we call min_cost_to_type("129A", 0), we want the cost to have
        robot3 (the numeric keypad arm) type "129A".
        """

        # level=0 controls level=1 controls level=2 controls level=3
        # So at level, we're controlling level+1

        if level == 2:
            # Level 2 controls level 3 (numeric keypad)
            # seq should consist of numeric buttons
            keypad_type = 'num'
            start_pos = num_A
            pos2label = num_pos2label
            label2pos = num_label2pos
        else:
            # Level 0 or 1 controls a directional keypad
            keypad_type = 'dir'
            start_pos = dir_A
            pos2label = dir_pos2label
            label2pos = dir_label2pos

        total_cost = 0
        current_pos = start_pos

        for target_button in seq:
            target_pos = label2pos[target_button]

            # Get all shortest paths on the controlled keypad
            path_strs = bfs_paths(current_pos, target_pos, keypad_type)

            # For each path, add 'A' and compute the cost
            min_next_cost = float('inf')
            for path_str in path_strs:
                # path_str is a sequence of direction buttons to move to target_pos
                # We need to type path_str + 'A' on level to have level+1 press target_button
                to_type_on_this_level = path_str + 'A'

                if level == 2:
                    # Level 2 needs to type to_type_on_this_level to control level 3
                    # But level 2 itself is controlled by level 1
                    # So we need the cost for level 1 to produce to_type_on_this_level
                    cost = min_cost_to_type(to_type_on_this_level, 1)
                elif level == 1:
                    # Level 1 needs to type to_type_on_this_level to control level 2
                    # Level 1 is controlled by level 0
                    cost = min_cost_to_type(to_type_on_this_level, 0)
                else:  # level == 0
                    # Level 0 is me pressing buttons
                    # I need to press the sequence to_type_on_this_level directly
                    # Cost is just the length of the sequence
                    cost = len(to_type_on_this_level)

                min_next_cost = min(min_next_cost, cost)

            total_cost += min_next_cost
            current_pos = target_pos

        return total_cost

    total = 0
    for code in lines:
        code = code.strip()
        if not code:
            continue

        # To have the numeric keypad (level 3) type `code`, level 2 must type
        # a sequence of directions. Level 1 controls level 2, level 0 (me) controls level 1.
        # So we compute: cost_at_level_2(code) -> how many presses from level 1 to type code on level 3
        cost = min_cost_to_type(code, 2)
        numeric_part = int(code[:-1]) if code[-1] == 'A' else int(code)
        complexity = cost * numeric_part
        total += complexity

    return total


def part2(lines):
    """
    Part 2: Same logic as part1, but with 26 directional keypads instead of 2.
    Levels 0-25: directional keypads (I control level 0, levels 1-25 are robots)
    Level 26: numeric keypad
    """

    def make_directional():
        rows = [ [None, '^', 'A'], ['<', 'v', '>'] ]
        pos_to_label = {}
        label_to_pos = {}
        for y, row in enumerate(rows):
            for x, v in enumerate(row):
                if v is not None:
                    pos_to_label[(x, y)] = v
                    label_to_pos[v] = (x, y)
        return pos_to_label, label_to_pos, label_to_pos['A']

    def make_numeric():
        rows = [ ['7','8','9'], ['4','5','6'], ['1','2','3'], [None,'0','A'] ]
        pos_to_label = {}
        label_to_pos = {}
        for y, row in enumerate(rows):
            for x, v in enumerate(row):
                if v is not None:
                    pos_to_label[(x, y)] = v
                    label_to_pos[v] = (x, y)
        return pos_to_label, label_to_pos, label_to_pos['A']

    dir_pos2label, dir_label2pos, dir_A = make_directional()
    num_pos2label, num_label2pos, num_A = make_numeric()

    @cache
    def bfs_paths(start, end, keypad_type):
        """Find all shortest paths (as strings) on keypad from start to end."""
        if keypad_type == 'dir':
            pos2label = dir_pos2label
        else:
            pos2label = num_pos2label

        if start == end:
            return ['']

        from collections import deque
        dq = deque()
        dq.append((start, ''))
        visited = {start: 0}
        paths = []
        min_len = None

        while dq:
            pos, path = dq.popleft()

            if min_len is not None and len(path) > min_len:
                continue

            if pos == end:
                if min_len is None:
                    min_len = len(path)
                if len(path) == min_len:
                    paths.append(path)
                continue

            x, y = pos
            for d, (dx, dy) in [('<', (-1, 0)), ('>', (1, 0)), ('^', (0, -1)), ('v', (0, 1))]:
                np = (x + dx, y + dy)
                if np not in pos2label:
                    continue
                new_path = path + d
                if np not in visited or visited[np] >= len(new_path):
                    visited[np] = len(new_path)
                    dq.append((np, new_path))

        return paths

    @cache
    def min_cost_to_type(seq, level):
        """
        Min presses on keypad at `level` needed to have keypad at `level+1`
        produce the sequence `seq`.

        level 0-25: directional keypads
        level 26: numeric keypad
        """

        if level == 25:
            # Level 25 controls level 26 (numeric keypad)
            keypad_type = 'num'
            start_pos = num_A
            pos2label = num_pos2label
            label2pos = num_label2pos
        else:
            # All other levels control directional keypads
            keypad_type = 'dir'
            start_pos = dir_A
            pos2label = dir_pos2label
            label2pos = dir_label2pos

        total_cost = 0
        current_pos = start_pos

        for target_button in seq:
            target_pos = label2pos[target_button]

            # Get all shortest paths on the controlled keypad
            path_strs = bfs_paths(current_pos, target_pos, keypad_type)

            # For each path, add 'A' and compute the cost
            min_next_cost = float('inf')
            for path_str in path_strs:
                to_type_on_this_level = path_str + 'A'

                if level == 0:
                    # Level 0 is me; just count button presses
                    cost = len(to_type_on_this_level)
                else:
                    # Recurse to the previous level
                    cost = min_cost_to_type(to_type_on_this_level, level - 1)

                min_next_cost = min(min_next_cost, cost)

            total_cost += min_next_cost
            current_pos = target_pos

        return total_cost

    total = 0
    for code in lines:
        code = code.strip()
        if not code:
            continue

        # Entry point: level 25 controls the numeric keypad (level 26)
        cost = min_cost_to_type(code, 25)
        numeric_part = int(code[:-1]) if code[-1] == 'A' else int(code)
        complexity = cost * numeric_part
        total += complexity

    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))

