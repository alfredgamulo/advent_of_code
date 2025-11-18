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
    # parse decks
    decks = [[]]
    cur = None
    for line in lines:
        if not line:
            continue
        if line.startswith("Player"):
            if line.startswith("Player 1"):
                decks = [[], []]
                cur = 0
            elif line.startswith("Player 2"):
                cur = 1
            continue
        decks[cur].append(int(line))

    from collections import deque

    d1 = deque(decks[0])
    d2 = deque(decks[1])

    while d1 and d2:
        a = d1.popleft()
        b = d2.popleft()
        if a > b:
            d1.append(a)
            d1.append(b)
        else:
            d2.append(b)
            d2.append(a)

    winner = d1 if d1 else d2
    score = sum(card * mult for mult, card in enumerate(reversed(winner), start=1))
    return score


def part2(lines):
    # parse decks
    decks = [[]]
    cur = None
    for line in lines:
        if not line:
            continue
        if line.startswith("Player"):
            if line.startswith("Player 1"):
                decks = [[], []]
                cur = 0
            elif line.startswith("Player 2"):
                cur = 1
            continue
        decks[cur].append(int(line))

    from collections import deque

    def play_recursive(d1, d2):
        # returns (winner_id, winning_deck)
        seen = set()
        while d1 and d2:
            state = (tuple(d1), tuple(d2))
            if state in seen:
                return 1, d1  # player 1 wins (use 1-based id for clarity)
            seen.add(state)

            a = d1.popleft()
            b = d2.popleft()

            if len(d1) >= a and len(d2) >= b:
                # sub-game
                new_d1 = deque(list(d1)[:a])
                new_d2 = deque(list(d2)[:b])
                winner_id, _ = play_recursive(new_d1, new_d2)
            else:
                winner_id = 1 if a > b else 2

            if winner_id == 1:
                d1.append(a)
                d1.append(b)
            else:
                d2.append(b)
                d2.append(a)

        if d1:
            return 1, d1
        else:
            return 2, d2

    d1 = deque(decks[0])
    d2 = deque(decks[1])
    winner_id, winner_deck = play_recursive(d1, d2)
    score = sum(card * mult for mult, card in enumerate(reversed(winner_deck), start=1))
    return score


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
