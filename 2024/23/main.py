try:
    import numpy as np
except Exception:
    np = None
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
    # Build undirected adjacency sets
    adj = defaultdict(set)
    for ln in lines:
        if not ln or '-' not in ln:
            continue
        a, b = ln.split('-')
        adj[a].add(b)
        adj[b].add(a)

    # Find unique triangles (3-cliques). We'll order nodes to avoid duplicates.
    triangles = set()
    for a in adj:
        for b in adj[a]:
            if b <= a:
                continue
            # iterate neighbors of b greater than b to keep ordering a < b < c
            for c in adj[b]:
                if c <= b:
                    continue
                # check if a connected to c
                if c in adj[a]:
                    tri = tuple(sorted((a, b, c)))
                    triangles.add(tri)

    # count triangles that have at least one node starting with 't'
    count = sum(1 for tri in triangles if any(x.startswith('t') for x in tri))
    return count


def part2(lines):
    # Find the maximum clique (largest set where every node connects to every other)
    adj = defaultdict(set)
    nodes = set()
    for ln in lines:
        if not ln or '-' not in ln:
            continue
        a, b = ln.split('-')
        adj[a].add(b)
        adj[b].add(a)
        nodes.add(a); nodes.add(b)

    # Bron-Kerbosch with pivoting to find maximum clique
    max_clique = []

    def bronk(R, P, X):
        nonlocal max_clique
        if not P and not X:
            # R is a maximal clique
            if len(R) > len(max_clique):
                max_clique = list(R)
            return

        # choose pivot u from P|X to reduce branches
        u = None
        union = P | X
        if union:
            # pick pivot with max neighbors in P
            u = max(union, key=lambda node: len(P & adj[node]))

        # iterate over vertices in P without neighbors of pivot
        for v in list(P - (adj[u] if u else set())):
            bronk(R | {v}, P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)

    bronk(set(), set(nodes), set())

    # Format password: sorted alphabetically, joined with commas
    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
