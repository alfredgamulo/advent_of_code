import copy
import os
import re
import string
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from io import StringIO
from itertools import permutations  # noqa
from itertools import batched, chain, combinations, count, cycle, product, zip_longest
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter


def parse1(lines):
    pass1 = []
    for line in lines:
        pass1.append(deque(line))
        if "#" not in line:
            pass1.append(deque(line))
    rotated = list(zip(*pass1[::-1]))
    pass2 = []
    for line in rotated:
        pass2.append(deque(line))
        if "#" not in line:
            pass2.append(deque(line))
    graph = list(reversed(list(zip(*pass2))))
    galaxies = []
    for x, y in product(range(len(graph)), range(len(graph[0]))):
        if graph[x][y] == "#":
            galaxies.append((x, y))
    return galaxies


def part1(lines):
    galaxies = parse1(lines)
    n = len(galaxies)
    distances = 0
    for i in range(n):
        for j in range(i + 1, n):
            distances += sum(abs(a - b) for a, b in zip(galaxies[i], galaxies[j]))
    return distances


def part2():
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2())
