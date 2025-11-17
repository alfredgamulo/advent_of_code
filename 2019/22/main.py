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

import numpy as np


def part1(lines):
    # deck size for part1
    m = 10007

    a = 1
    b = 0

    def compose(op_a, op_b, cur_a, cur_b):
        # op(f(x)) where op(x)=op_a*x+op_b and f(x)=cur_a*x+cur_b
        na = (op_a * cur_a) % m
        nb = (op_a * cur_b + op_b) % m
        return na, nb

    for line in lines:
        line = line.strip()
        if line == 'deal into new stack':
            op_a, op_b = -1 % m, -1 % m
        elif line.startswith('cut'):
            n = int(line.split()[-1])
            op_a, op_b = 1, (-n) % m
        elif line.startswith('deal with increment'):
            n = int(line.split()[-1])
            op_a, op_b = n % m, 0
        else:
            continue
        a, b = compose(op_a, op_b, a, b)

    # position of card 2019 after shuffle
    pos = (a * 2019 + b) % m
    return pos


def part2(lines):
    # large deck and iterations
    m = 119315717514047
    times = 101741582076661

    # compose modulo m for a chain of operations
    def compose_pair(op, cur):
        (op_a, op_b) = op
        (cur_a, cur_b) = cur
        na = (op_a * cur_a) % m
        nb = (op_a * cur_b + op_b) % m
        return na, nb

    # parse operations to a single linear transform f(x)=a*x+b (mod m)
    a = 1
    b = 0
    for line in lines:
        line = line.strip()
        if line == 'deal into new stack':
            op_a, op_b = -1 % m, -1 % m
        elif line.startswith('cut'):
            n = int(line.split()[-1])
            op_a, op_b = 1, (-n) % m
        elif line.startswith('deal with increment'):
            n = int(line.split()[-1])
            op_a, op_b = n % m, 0
        else:
            continue
        a, b = compose_pair((op_a, op_b), (a, b))

    # compute inverse transform f^{-1}(x) = a_inv * (x - b)
    def egcd(a0, b0):
        if b0 == 0:
            return (a0, 1, 0)
        g, x1, y1 = egcd(b0, a0 % b0)
        return (g, y1, x1 - (a0 // b0) * y1)

    def modinv(x, mod):
        g, inv, _ = egcd(x, mod)
        if g != 1:
            raise ValueError('No modular inverse')
        return inv % mod

    a_inv = modinv(a, m)
    b_inv = (-a_inv * b) % m

    # exponentiate linear function by repeated squaring: compose pairs
    def pow_lin(pair, exponent):
        res = (1, 0)
        base = pair
        e = exponent
        while e > 0:
            if e & 1:
                res = compose_pair(base, res)
            base = compose_pair(base, base)
            e >>= 1
        return res

    inv_total = pow_lin((a_inv, b_inv), times)

    # apply inverse^times to position 2020 to get original card at that position
    res_a, res_b = inv_total
    card = (res_a * 2020 + res_b) % m
    return card


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
