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


def can_make_design(design, patterns):
    """Check if a design can be made with available patterns using DP"""
    # dp[i] = True if design[:i] can be made
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Empty string can always be made

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            pattern_len = len(pattern)
            # If we can make design[:i-pattern_len] and design[i-pattern_len:i] matches pattern
            if i >= pattern_len and dp[i - pattern_len] and design[i - pattern_len:i] == pattern:
                dp[i] = True
                break

    return dp[len(design)]


def count_ways(design, patterns):
    """Count the number of ways to make a design using available patterns"""
    memo = {}

    def dp(pos):
        if pos == len(design):
            return 1
        if pos in memo:
            return memo[pos]

        ways = 0
        for pattern in patterns:
            if design[pos:pos + len(pattern)] == pattern:
                ways += dp(pos + len(pattern))

        memo[pos] = ways
        return ways

    return dp(0)


def part1(lines):
    # Find the blank line
    blank_idx = lines.index("")

    # Parse towel patterns
    patterns = lines[0].split(", ")

    # Parse designs
    designs = lines[blank_idx + 1:]

    # Count how many designs are possible
    count = 0
    for design in designs:
        if can_make_design(design, patterns):
            count += 1

    return count


def part2(lines):
    # Find the blank line
    blank_idx = lines.index("")

    # Parse towel patterns
    patterns = lines[0].split(", ")

    # Parse designs
    designs = lines[blank_idx + 1:]

    # Count total ways to make all designs
    total_ways = 0
    for design in designs:
        total_ways += count_ways(design, patterns)

    return total_ways


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
