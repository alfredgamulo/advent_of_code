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
    prog = [int(x) for x in lines[0].split(',') if x != '']

    class Computer:
        def __init__(self, program):
            self.mem = list(program) + [0] * 10000
            self.ip = 0
            self.rb = 0

        def run_until_output(self, inputs):
            """Consume inputs list (may be empty). Return list of outputs produced (may be empty)."""
            mem = self.mem
            ip = self.ip
            rb = self.rb
            outputs = []

            def param(n):
                mode = (mem[ip] // (10 ** (n + 1))) % 10
                if mode == 0:
                    return mem[mem[ip + n]]
                elif mode == 1:
                    return mem[ip + n]
                else:
                    return mem[mem[ip + n] + rb]

            def write_addr(n):
                mode = (mem[ip] // (10 ** (n + 1))) % 10
                if mode == 0:
                    return mem[ip + n]
                else:
                    return mem[ip + n] + rb

            provided_neg = False
            while True:
                op = mem[ip] % 100
                if op == 1:
                    mem[write_addr(3)] = param(1) + param(2)
                    ip += 4
                elif op == 2:
                    mem[write_addr(3)] = param(1) * param(2)
                    ip += 4
                elif op == 3:
                    # input: if we have queued inputs use them; otherwise supply -1 once
                    if inputs:
                        val = inputs.pop(0)
                        mem[write_addr(1)] = int(val)
                        ip += 2
                        # reset provided_neg because we consumed real input
                        provided_neg = False
                    else:
                        if provided_neg:
                            # no input available and we've already provided -1 -> block
                            break
                        mem[write_addr(1)] = -1
                        ip += 2
                        provided_neg = True
                elif op == 4:
                    outputs.append(int(param(1)))
                    ip += 2
                    # return immediately after producing outputs (could be batched by caller)
                    # but continue to collect more outputs in this call
                    if len(outputs) >= 1:
                        break
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
                    # halt
                    self.ip = ip
                    self.rb = rb
                    self.mem = mem
                    return outputs
                else:
                    raise RuntimeError(f"Unknown opcode {op} at {ip}")

            self.ip = ip
            self.rb = rb
            self.mem = mem
            return outputs

    # initialize 50 computers
    comps = [Computer(prog) for _ in range(50)]
    queues = [[i] for i in range(50)]
    out_buffers = [[] for _ in range(50)]

    while True:
        for i in range(50):
            outputs = comps[i].run_until_output(queues[i])
            if outputs:
                out_buffers[i].extend(outputs)
                # process triples
                while len(out_buffers[i]) >= 3:
                    dest = out_buffers[i].pop(0)
                    x = out_buffers[i].pop(0)
                    y = out_buffers[i].pop(0)
                    if dest == 255:
                        return y
                    else:
                        queues[dest].append(x)
                        queues[dest].append(y)



def part2(lines):
    prog = [int(x) for x in lines[0].split(',') if x != '']

    class Computer:
        def __init__(self, program):
            self.mem = list(program) + [0] * 10000
            self.ip = 0
            self.rb = 0

        def run_until_output(self, inputs):
            mem = self.mem
            ip = self.ip
            rb = self.rb
            outputs = []

            def param(n):
                mode = (mem[ip] // (10 ** (n + 1))) % 10
                if mode == 0:
                    return mem[mem[ip + n]]
                elif mode == 1:
                    return mem[ip + n]
                else:
                    return mem[mem[ip + n] + rb]

            def write_addr(n):
                mode = (mem[ip] // (10 ** (n + 1))) % 10
                if mode == 0:
                    return mem[ip + n]
                else:
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
                    # input: if we have queued inputs use them; otherwise supply -1 once
                    # and then 'block' (return) to let the controller know we're idle.
                    if 'provided_neg' not in locals():
                        provided_neg = False
                    if inputs:
                        val = inputs.pop(0)
                        mem[write_addr(1)] = int(val)
                        ip += 2
                        # reset provided_neg because we consumed real input
                        provided_neg = False
                    else:
                        if provided_neg:
                            # no input available and we've already provided -1 -> block
                            break
                        mem[write_addr(1)] = -1
                        ip += 2
                        provided_neg = True
                elif op == 4:
                    outputs.append(int(param(1)))
                    ip += 2
                    if len(outputs) >= 1:
                        break
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
                    self.ip = ip
                    self.rb = rb
                    self.mem = mem
                    return outputs
                else:
                    raise RuntimeError(f"Unknown opcode {op} at {ip}")

            self.ip = ip
            self.rb = rb
            self.mem = mem
            return outputs

    comps = [Computer(prog) for _ in range(50)]
    queues = [[i] for i in range(50)]
    out_buffers = [[] for _ in range(50)]
    nat = None
    last_nat_y_sent = None

    while True:
        network_idle = True
        for i in range(50):
            outputs = comps[i].run_until_output(queues[i])
            if outputs:
                network_idle = False
                out_buffers[i].extend(outputs)
                while len(out_buffers[i]) >= 3:
                    dest = out_buffers[i].pop(0)
                    x = out_buffers[i].pop(0)
                    y = out_buffers[i].pop(0)
                    if dest == 255:
                        nat = (x, y)
                    else:
                        queues[dest].append(x)
                        queues[dest].append(y)
        # if network is idle (no outputs this round) and all queues empty -> NAT activity
        if network_idle and all(len(q) == 0 for q in queues):
            if nat is None:
                continue
            x, y = nat
            queues[0].append(x)
            queues[0].append(y)
            if last_nat_y_sent == y:
                return y
            last_nat_y_sent = y



if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
