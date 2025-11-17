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
from typing import List, Tuple


def parse_points(lines: List[str]) -> List[Tuple[int, int, int, int]]:
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = list(map(int, line.split(',')))
        pts.append((parts[0], parts[1], parts[2], parts[3]))
    return pts


class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, a: int) -> int:
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            self.p[ra] = rb
        elif self.r[rb] < self.r[ra]:
            self.p[rb] = ra
        else:
            self.p[rb] = ra
            self.r[ra] += 1
        return True


def manhattan(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])


def part1(lines: List[str]) -> int:
    pts = parse_points(lines)
    n = len(pts)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if manhattan(pts[i], pts[j]) <= 3:
                uf.union(i, j)
    roots = set()
    for i in range(n):
        roots.add(uf.find(i))
    return len(roots)


def part2(lines: List[str]):
    # No part 2 for 2018 Day 25
    return None


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
