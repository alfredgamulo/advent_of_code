import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
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


def part1():
    accepted, namespace = [], {}
    for part in parts:
        for rating in part[1:-1].split(","):
            exec(rating, namespace)
        consider = "in"
        while consider not in "RA":
            workflow = rules[consider]
            for w in workflow:
                with suppress(ValueError):
                    condition, outcome = w.split(":")
                    if eval(condition, namespace):
                        consider = outcome
                        break
                consider = w
        [[], accepted]["RA".index(consider)].append(
            sum([namespace["x"], namespace["m"], namespace["a"], namespace["s"]])
        )
    return sum(accepted)


def part2():
    ...


if __name__ == "__main__":
    raw_rules, parts = (l.split() for l in Path(sys.argv[1]).read_text().split("\n\n"))
    rules = {(r := re.split("{|,", raw[:-1])) and r[0]: r[1:] for raw in raw_rules}
    print("Part 1:", part1())
    print("Part 2:", part2())
