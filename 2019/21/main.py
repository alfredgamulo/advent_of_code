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

    def run(self, inputs):
        mem = self.mem
        ip = self.ip
        rb = self.rb
        inp = list(inputs)
        outputs = []

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


def part1(lines):
    prog = [int(x) for x in lines[0].split(',') if x != '']

    # SpringScript for part 1: jump if any of A,B,C is hole and D is ground
    script = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n"

    inputs = [ord(c) for c in script]

    comp = IntcodeComputer(prog)
    out = comp.run(inputs)

    # If there's a numeric output > 127 it's the hull damage
    for v in out:
        if v > 127:
            return v
    # otherwise return 0
    return None


def part2(lines):
    prog = [int(x) for x in lines[0].split(',') if x != '']

    # SpringScript for part 2: more advanced - ensure E or H available
    script = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n"

    inputs = [ord(c) for c in script]

    comp = IntcodeComputer(prog)
    out = comp.run(inputs)
    for v in out:
        if v > 127:
            return v
    return None


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
