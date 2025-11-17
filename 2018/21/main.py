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


def parse(lines: List[str]):
    ip_reg = int(lines[0].split()[1])
    prog = []
    for line in lines[1:]:
        parts = line.split()
        op = parts[0]
        a, b, c = map(int, parts[1:])
        prog.append((op, a, b, c))
    return ip_reg, prog

def make_ops():
    def addr(r, a, b, c): r[c] = r[a] + r[b]
    def addi(r, a, b, c): r[c] = r[a] + b
    def mulr(r, a, b, c): r[c] = r[a] * r[b]
    def muli(r, a, b, c): r[c] = r[a] * b
    def banr(r, a, b, c): r[c] = r[a] & r[b]
    def bani(r, a, b, c): r[c] = r[a] & b
    def borr(r, a, b, c): r[c] = r[a] | r[b]
    def bori(r, a, b, c): r[c] = r[a] | b
    def setr(r, a, b, c): r[c] = r[a]
    def seti(r, a, b, c): r[c] = a
    def gtir(r, a, b, c): r[c] = 1 if a > r[b] else 0
    def gtri(r, a, b, c): r[c] = 1 if r[a] > b else 0
    def gtrr(r, a, b, c): r[c] = 1 if r[a] > r[b] else 0
    def eqir(r, a, b, c): r[c] = 1 if a == r[b] else 0
    def eqri(r, a, b, c): r[c] = 1 if r[a] == b else 0
    def eqrr(r, a, b, c): r[c] = 1 if r[a] == r[b] else 0

    return {
        'addr': addr, 'addi': addi,
        'mulr': mulr, 'muli': muli,
        'banr': banr, 'bani': bani,
        'borr': borr, 'bori': bori,
        'setr': setr, 'seti': seti,
        'gtir': gtir, 'gtri': gtri, 'gtrr': gtrr,
        'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr,
    }

def run_until_repeat(ip_reg: int, prog: List[Tuple[str, int, int, int]]):
    ops = make_ops()
    eqrr_idx = None
    for i, (op, a, b, c) in enumerate(prog):
        if op == 'eqrr' and ((a == 5 and b == 0) or (a == 0 and b == 5)):
            eqrr_idx = i
            break
    if eqrr_idx is None:
        raise RuntimeError('Could not find eqrr comparing reg5 and reg0')

    seen = set()
    last = None

    regs = [0] * 6
    ip = 0
    first = None
    while 0 <= ip < len(prog):
        if ip == eqrr_idx:
            r5 = regs[5]
            if first is None:
                first = r5
            if r5 in seen:
                return first, last
            seen.add(r5)
            last = r5

        regs[ip_reg] = ip
        op, a, b, c = prog[ip]
        ops[op](regs, a, b, c)
        ip = regs[ip_reg]
        ip += 1

    return first, last

def part1(lines):
    ip_reg, prog = parse(lines)
    first, _ = run_until_repeat(ip_reg, prog)
    return first

def part2(lines):
    ip_reg, prog = parse(lines)
    _, last = run_until_repeat(ip_reg, prog)
    return last

if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
