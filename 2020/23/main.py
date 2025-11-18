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
    # parse input: single line of digits
    if not lines:
        return None
    cups_input = lines[0].strip()

    def play(cups_str, moves, total_cups=None):
        labels = [int(ch) for ch in cups_str]
        orig_max = max(labels)
        if total_cups is None:
            max_label = orig_max
        else:
            max_label = total_cups

        # next[i] = label that comes after i
        nxt = [0] * (max_label + 1)

        # link initial labels
        for a, b in zip(labels, labels[1:]):
            nxt[a] = b

        if total_cups and total_cups > len(labels):
            nxt[labels[-1]] = orig_max + 1
            # fill remaining labels
            for v in range(orig_max + 1, total_cups):
                nxt[v] = v + 1
            nxt[total_cups] = labels[0]
        else:
            nxt[labels[-1]] = labels[0]

        current = labels[0]
        for _ in range(moves):
            pick1 = nxt[current]
            pick2 = nxt[pick1]
            pick3 = nxt[pick2]
            # remove picked up
            nxt[current] = nxt[pick3]

            dest = current - 1 or max_label
            while dest == pick1 or dest == pick2 or dest == pick3:
                dest -= 1
                if dest <= 0:
                    dest = max_label

            # insert picked after dest
            nxt[pick3] = nxt[dest]
            nxt[dest] = pick1

            current = nxt[current]

        return nxt

    nxt = play(cups_input, 100)
    # build output string after cup 1
    out = []
    x = nxt[1]
    while x != 1:
        out.append(str(x))
        x = nxt[x]
    return ''.join(out)


def part2(lines):
    if not lines:
        return None
    cups_input = lines[0].strip()

    def play(cups_str, moves, total_cups=None):
        labels = [int(ch) for ch in cups_str]
        orig_max = max(labels)
        if total_cups is None:
            max_label = orig_max
        else:
            max_label = total_cups

        nxt = [0] * (max_label + 1)
        for a, b in zip(labels, labels[1:]):
            nxt[a] = b

        if total_cups and total_cups > len(labels):
            nxt[labels[-1]] = orig_max + 1
            for v in range(orig_max + 1, total_cups):
                nxt[v] = v + 1
            nxt[total_cups] = labels[0]
        else:
            nxt[labels[-1]] = labels[0]

        current = labels[0]
        for _ in range(moves):
            pick1 = nxt[current]
            pick2 = nxt[pick1]
            pick3 = nxt[pick2]
            nxt[current] = nxt[pick3]

            dest = current - 1 or max_label
            while dest == pick1 or dest == pick2 or dest == pick3:
                dest -= 1
                if dest <= 0:
                    dest = max_label

            nxt[pick3] = nxt[dest]
            nxt[dest] = pick1

            current = nxt[current]

        return nxt

    nxt = play(cups_input, 10_000_000, total_cups=1_000_000)
    a = nxt[1]
    b = nxt[a]
    return a * b


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
