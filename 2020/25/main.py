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
    # Parse the two public keys
    card_pub = int(lines[0].strip())
    door_pub = int(lines[1].strip())

    MOD = 20201227

    def find_loop_size(target_pub):
        """Find the loop size for a given public key"""
        value = 1
        loop_size = 0
        while value != target_pub:
            value = (value * 7) % MOD
            loop_size += 1
        return loop_size

    def transform(subject_number, loop_size):
        """Compute the encryption key using subject number and loop size"""
        value = 1
        for _ in range(loop_size):
            value = (value * subject_number) % MOD
        return value

    # Find the card's loop size
    card_loop = find_loop_size(card_pub)

    # Compute the encryption key using the door's public key and card's loop size
    encryption_key = transform(door_pub, card_loop)

    return encryption_key


def part2(lines):
    # Part 2 is typically just to confirm (submit the answer from part 1)
    return "Activate"


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
