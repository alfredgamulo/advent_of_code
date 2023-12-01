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
    chain,
    combinations,
    count,
    cycle,
    permutations,
    product,
    zip_longest,
)
from math import ceil, floor, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter

from more_itertools import grouper


def part1(lines):
    print(lines)


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
