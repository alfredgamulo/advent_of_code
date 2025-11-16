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
    ip_reg = int(re.match(r"#ip (\d+)", lines[0]).groups()[0])
    prog = [tuple(line.split()) for line in lines[1:]]
    prog = [(op, int(a), int(b), int(c)) for (op, a, b, c) in prog]

    ops = {
        "addr": lambda r, a, b, c: r.__setitem__(c, r[a] + r[b]) or r,
        "addi": lambda r, a, b, c: r.__setitem__(c, r[a] + b) or r,
        "mulr": lambda r, a, b, c: r.__setitem__(c, r[a] * r[b]) or r,
        "muli": lambda r, a, b, c: r.__setitem__(c, r[a] * b) or r,
        "banr": lambda r, a, b, c: r.__setitem__(c, (r[a] & r[b])) or r,
        "bani": lambda r, a, b, c: r.__setitem__(c, (r[a] & b)) or r,
        "borr": lambda r, a, b, c: r.__setitem__(c, (r[a] | r[b])) or r,
        "bori": lambda r, a, b, c: r.__setitem__(c, (r[a] | b)) or r,
        "setr": lambda r, a, b, c: r.__setitem__(c, r[a]) or r,
        "seti": lambda r, a, b, c: r.__setitem__(c, a) or r,
        "gtir": lambda r, a, b, c: r.__setitem__(c, (1 if a > r[b] else 0)) or r,
        "gtri": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] > b else 0)) or r,
        "gtrr": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] > r[b] else 0)) or r,
        "eqir": lambda r, a, b, c: r.__setitem__(c, (1 if a == r[b] else 0)) or r,
        "eqri": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] == b else 0)) or r,
        "eqrr": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] == r[b] else 0)) or r,
    }

    regs = [0] * 6
    ip = 0
    steps = 0
    while 0 <= ip < len(prog):
        regs[ip_reg] = ip
        op, a, b, c = prog[ip]
        ops[op](regs, a, b, c)
        ip = regs[ip_reg]
        ip += 1
        steps += 1
    return regs[0]


def part2(lines):
    # For part 2 the program builds a (much) larger number in register 5 when r0=1,
    # then runs a double loop that accumulates into r0 the divisors of that number.
    # We can run the setup until the main loop starts (ip == 1) and then compute
    # the sum of divisors of register 5 directly.
    ip_reg = int(re.match(r"#ip (\d+)", lines[0]).groups()[0])
    prog = [tuple(line.split()) for line in lines[1:]]
    prog = [(op, int(a), int(b), int(c)) for (op, a, b, c) in prog]

    ops = {
        "addr": lambda r, a, b, c: r.__setitem__(c, r[a] + r[b]) or r,
        "addi": lambda r, a, b, c: r.__setitem__(c, r[a] + b) or r,
        "mulr": lambda r, a, b, c: r.__setitem__(c, r[a] * r[b]) or r,
        "muli": lambda r, a, b, c: r.__setitem__(c, r[a] * b) or r,
        "banr": lambda r, a, b, c: r.__setitem__(c, (r[a] & r[b])) or r,
        "bani": lambda r, a, b, c: r.__setitem__(c, (r[a] & b)) or r,
        "borr": lambda r, a, b, c: r.__setitem__(c, (r[a] | r[b])) or r,
        "bori": lambda r, a, b, c: r.__setitem__(c, (r[a] | b)) or r,
        "setr": lambda r, a, b, c: r.__setitem__(c, r[a]) or r,
        "seti": lambda r, a, b, c: r.__setitem__(c, a) or r,
        "gtir": lambda r, a, b, c: r.__setitem__(c, (1 if a > r[b] else 0)) or r,
        "gtri": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] > b else 0)) or r,
        "gtrr": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] > r[b] else 0)) or r,
        "eqir": lambda r, a, b, c: r.__setitem__(c, (1 if a == r[b] else 0)) or r,
        "eqri": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] == b else 0)) or r,
        "eqrr": lambda r, a, b, c: r.__setitem__(c, (1 if r[a] == r[b] else 0)) or r,
    }

    regs = [0] * 6
    regs[0] = 1
    ip = 0
    # run until we reach the main divisor-checking loop start at ip == 1
    while 0 <= ip < len(prog):
        if ip == 1:
            break
        regs[ip_reg] = ip
        op, a, b, c = prog[ip]
        ops[op](regs, a, b, c)
        ip = regs[ip_reg]
        ip += 1

    target = regs[5]

    # compute sum of divisors of target
    total = 0
    # iterate up to sqrt to be efficient
    import math
    root = int(math.isqrt(target))
    for i in range(1, root + 1):
        if target % i == 0:
            total += i
            j = target // i
            if j != i:
                total += j
    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
