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


class IntcodeComputer:
    def __init__(self, program):
        self.mem = list(program) + [0] * 10000
        self.ip = 0
        self.rb = 0

    def _get(self, idx):
        return self.mem[idx]

    def _set(self, idx, val):
        self.mem[idx] = val

    def run(self, inputs):
        """Run the program with the provided inputs (list). Return list of outputs."""
        inp = list(inputs)
        outputs = []
        mem = self.mem
        ip = self.ip
        rb = self.rb

        def param(n):
            mode = (mem[ip] // (10 ** (n + 1))) % 10
            if mode == 0:
                return mem[mem[ip + n]]
            elif mode == 1:
                return mem[ip + n]
            elif mode == 2:
                return mem[mem[ip + n] + rb]

        def write_addr(n):
            mode = (mem[ip] // (10 ** (n + 1))) % 10
            if mode == 0:
                return mem[ip + n]
            elif mode == 2:
                return mem[ip + n] + rb

        while True:
            op = mem[ip] % 100
            if op == 1:
                mem[write_addr(3)] = param(1) + param(2)
                ip += 4
            elif op == 2:
                mem[write_addr(3)] = param(1) * param(2)
                ip += 4
            elif op == 3:
                if not inp:
                    raise RuntimeError("No input available")
                mem[write_addr(1)] = int(inp.pop(0))
                ip += 2
            elif op == 4:
                outputs.append(int(param(1)))
                ip += 2
            elif op == 5:
                if param(1) != 0:
                    ip = param(2)
                else:
                    ip += 3
            elif op == 6:
                if param(1) == 0:
                    ip = param(2)
                else:
                    ip += 3
            elif op == 7:
                mem[write_addr(3)] = 1 if param(1) < param(2) else 0
                ip += 4
            elif op == 8:
                mem[write_addr(3)] = 1 if param(1) == param(2) else 0
                ip += 4
            elif op == 9:
                rb += param(1)
                ip += 2
            elif op == 99:
                break
            else:
                raise RuntimeError(f"Unknown opcode {op} at ip {ip}")

        self.ip = ip
        self.rb = rb
        self.mem = mem
        return outputs


def _load_program(lines):
    if not lines:
        return []
    return [int(x) for x in lines[0].strip().split(',') if x != '']


def part1(lines):
    prog = _load_program(lines)
    count = 0
    for y in range(50):
        for x in range(50):
            comp = IntcodeComputer(prog)
            out = comp.run([x, y])
            if out and out[0] == 1:
                count += 1
    return count


def part2(lines):
    prog = _load_program(lines)
    cache = {}

    def beam(x, y):
        if (x, y) in cache:
            return cache[(x, y)]
        comp = IntcodeComputer(prog)
        out = comp.run([x, y])
        val = out[0] if out else 0
        cache[(x, y)] = val
        return val

    # Sliding window search
    x = 0
    y = 99  # square height - 1
    while True:
        # move x right until we hit beam at this y
        while beam(x, y) == 0:
            x += 1
        # now check top-right corner of 100x100 square: (x+99, y-99)
        if beam(x + 99, y - 99) == 1:
            return x * 10000 + (y - 99)
        y += 1


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
