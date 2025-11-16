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


def solve(samples, instructions=None):
    ops = {
        "addr": lambda registers, a, b, c: registers.__setitem__(c, registers[a] + registers[b]) or registers,
        "addi": lambda registers, a, b, c: registers.__setitem__(c, registers[a] + b) or registers,
        "mulr": lambda registers, a, b, c: registers.__setitem__(c, registers[a] * registers[b]) or registers,
        "muli": lambda registers, a, b, c: registers.__setitem__(c, registers[a] * b) or registers,
        "banr": lambda registers, a, b, c: registers.__setitem__(c, (registers[a] & registers[b])) or registers,
        "bani": lambda registers, a, b, c: registers.__setitem__(c, (registers[a] & b)) or registers,
        "borr": lambda registers, a, b, c: registers.__setitem__(c, (registers[a] | registers[b])) or registers,
        "bori": lambda registers, a, b, c: registers.__setitem__(c, (registers[a] | b)) or registers,
        "setr": lambda registers, a, b, c: registers.__setitem__(c, registers[a]) or registers,
        "seti": lambda registers, a, b, c: registers.__setitem__(c, a) or registers,
        "gtir": lambda registers, a, b, c: registers.__setitem__(c, (1 if a > registers[b] else 0)) or registers,
        "gtri": lambda registers, a, b, c: registers.__setitem__(c, (1 if registers[a] > b else 0)) or registers,
        "gtrr": lambda registers, a, b, c: registers.__setitem__(c, (1 if registers[a] > registers[b] else 0)) or registers,
        "eqir": lambda registers, a, b, c: registers.__setitem__(c, (1 if a == registers[b] else 0)) or registers,
        "eqri": lambda registers, a, b, c: registers.__setitem__(c, (1 if registers[a] == b else 0)) or registers,
        "eqrr": lambda registers, a, b, c: registers.__setitem__(c, (1 if registers[a] == registers[b] else 0)) or registers,
    }
    part1 = 0
    opcode_possibilities = {i: set(ops.keys()) for i in range(16)}

    for sample in samples.split("\n\n"):
        before, instruction, after = sample.splitlines()
        before = list(map(int, re.findall(r"\d+", before)))
        after = list(map(int, re.findall(r"\d+", after)))
        opcode, a, b, c = map(int, instruction.split())
        matching_ops = 0
        possible_ops = set()
        for op_name, op_func in ops.items():
            registers = before.copy()
            result = op_func(registers, a, b, c)
            if result == after:
                matching_ops += 1
                possible_ops.add(op_name)
        if matching_ops >= 3:
            part1 += 1
        opcode_possibilities[opcode] &= possible_ops
    print("Part 1:", part1)
    opcode_mapping = {}
    while len(opcode_mapping) < 16:
        for opcode, possible_ops in opcode_possibilities.items():
            possible_ops -= set(opcode_mapping.values())
            if len(possible_ops) == 1:
                opcode_mapping[opcode] = possible_ops.pop()
    registers = [0, 0, 0, 0]
    for line in instructions.splitlines():
        opcode, a, b, c = map(int, line.split())
        op_name = opcode_mapping[opcode]
        ops[op_name](registers, a, b, c)
    print("Part 2:", registers[0])



if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text()
    sections = lines.split("\n\n\n\n")
    solve(sections[0], sections[1])

