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


def solve(graph, expansion):
    galaxies = [
        (x, y)
        for x, y in product(range(len(graph)), range(len(graph[0])))
        if graph[x][y] == "#"
    ]
    xs = [x for x, line in enumerate(graph) if "#" not in line]
    graph = list(zip(*graph[::-1]))
    ys = [x for x, line in enumerate(graph) if "#" not in line]
    print(xs)
    print(ys)
    galaxies = [
        (
            (x + (next((i for i, v in enumerate(xs) if v > x), 0) * expansion)),
            (y + (next((i for i, v in enumerate(ys) if v > y), 0) * expansion)),
        )
        for x, y in galaxies
    ]
    return sum(abs(a - b) for a, b in combinations(galaxies, 2))


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", solve(lines, 2))
    # print("Part 2:", solve(lines, 1000000))
