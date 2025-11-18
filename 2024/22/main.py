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
    MOD = 16777216
    results = []
    for line in lines:
        secret = int(line)
        for _ in range(2000):
            # Step 1: multiply by 64, mix, prune
            secret = (secret ^ (secret * 64)) % MOD
            # Step 2: divide by 32 (floor), mix, prune
            secret = (secret ^ (secret // 32)) % MOD
            # Step 3: multiply by 2048, mix, prune
            secret = (secret ^ (secret * 2048)) % MOD
        results.append(secret)
    return sum(results)


def part2(lines):
    # Optimized: for each buyer, record the first price for each 4-change
    # sequence (encode sequences as a small integer) and accumulate into a
    # global sums dict. This avoids iterating all possible sequences.
    MOD = 16777216
    N = 2000
    from collections import defaultdict

    global_sums = defaultdict(int)
    BASE = 19  # changes from -9..9 -> 19 values
    OFF = 9

    for line in lines:
        secret = int(line)
        secrets = [secret]
        for _ in range(N):
            secret = (secret ^ (secret * 64)) % MOD
            secret = (secret ^ (secret // 32)) % MOD
            secret = (secret ^ (secret * 2048)) % MOD
            secrets.append(secret)

        prices = [s % 10 for s in secrets]
        changes = [prices[i+1] - prices[i] for i in range(N)]

        seen = set()
        # Slide a window of 4 over changes and record first occurrence per buyer
        for i in range(len(changes) - 3):
            a, b, c, d = changes[i], changes[i+1], changes[i+2], changes[i+3]
            key = (((a + OFF) * BASE + (b + OFF)) * BASE + (c + OFF)) * BASE + (d + OFF)
            if key in seen:
                continue
            seen.add(key)
            # price at the time of sale is the price after the 4th change
            global_sums[key] += prices[i + 4]

    if not global_sums:
        return 0

    best_key, best_sum = max(global_sums.items(), key=lambda kv: kv[1])
    # decode sequence for debug
    seq = []
    k = best_key
    for _ in range(4):
        seq.append((k % BASE) - OFF)
        k //= BASE
    seq = list(reversed(seq))
    print(f"Best sequence: {seq}, Bananas: {best_sum}")
    return best_sum


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
