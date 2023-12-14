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
from itertools import (
    batched,
    chain,
    combinations,
    count,
    groupby,
    permutations,
    product,
    zip_longest,
)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter


def tumble(platform):
    total = 0
    for x, p in enumerate(platform):
        wall = len(platform) + 1
        for i in re.finditer("#|O", "".join(p)):
            if i.group() == "#":
                wall = len(platform) - i.span()[0]
            if i.group() == "O":
                wall -= 1
                total += wall
                platform[x][i.span()[0]] = "."
                platform[x][len(platform) - wall] = "O"
    return total, platform


def part1(platform):
    total, platform = tumble(platform)
    return total


def part2(platform):
    load = 0
    for i in range(1_000_000_000):
        load, platform = tumble(platform)
        platform = [deque(list((item)[::-1])) for item in zip(*platform)]
        if (i % 4) == 3:
            print(i, load)
    return load


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1([deque(item) for item in zip(*lines)][::-1]))
    print("Part 2:", part2([deque(item) for item in zip(*lines)][::-1]))
