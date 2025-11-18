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


class Computer:
    def __init__(self, a, b, c, program):
        self.registers = {'A': a, 'B': b, 'C': c}
        self.program = program
        self.ip = 0  # instruction pointer
        self.output = []

    def get_combo_operand(self, operand):
        """Get the value of a combo operand."""
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        else:
            raise ValueError(f"Invalid combo operand: {operand}")

    def run(self):
        """Run the program until it halts."""
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]

            if opcode == 0:  # adv
                combo_val = self.get_combo_operand(operand)
                self.registers['A'] = self.registers['A'] // (2 ** combo_val)
            elif opcode == 1:  # bxl
                self.registers['B'] = self.registers['B'] ^ operand
            elif opcode == 2:  # bst
                combo_val = self.get_combo_operand(operand)
                self.registers['B'] = combo_val % 8
            elif opcode == 3:  # jnz
                if self.registers['A'] != 0:
                    self.ip = operand
                    continue
            elif opcode == 4:  # bxc
                self.registers['B'] = self.registers['B'] ^ self.registers['C']
            elif opcode == 5:  # out
                combo_val = self.get_combo_operand(operand)
                self.output.append(combo_val % 8)
            elif opcode == 6:  # bdv
                combo_val = self.get_combo_operand(operand)
                self.registers['B'] = self.registers['A'] // (2 ** combo_val)
            elif opcode == 7:  # cdv
                combo_val = self.get_combo_operand(operand)
                self.registers['C'] = self.registers['A'] // (2 ** combo_val)

            self.ip += 2

        return self.output


def parse_input(lines):
    """Parse the input file."""
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    program = list(map(int, lines[4].split(": ")[1].split(",")))
    return a, b, c, program


def part1(lines):
    a, b, c, program = parse_input(lines)
    computer = Computer(a, b, c, program)
    output = computer.run()
    return ",".join(map(str, output))


def part2(lines):
    _, _, _, program = parse_input(lines)

    def get_output(a):
        """Get the program output for a given initial A value."""
        computer = Computer(a, 0, 0, program)
        return computer.run()

    # Key insight: Build candidates from the last output digit backwards
    # We start with all possible 8-bit prefixes that could give us the last digit
    # Then work backwards to match the entire program

    # Start by finding all small values of A that eventually produce outputs
    # We'll use BFS/dynamic programming approach

    candidates = [0]

    # For each position in the program (from right to left)
    for pos in range(len(program) - 1, -1, -1):
        target = program[pos:]  # The suffix we need to match
        new_candidates = []

        for cand in candidates:
            # Try all 8 possible extensions (3 bits)
            for ext in range(8):
                a_val = cand * 8 + ext
                output = get_output(a_val)

                # Check if this produces the right suffix
                if len(output) >= len(target) and output[-len(target):] == target:
                    new_candidates.append(a_val)

        candidates = new_candidates

        if not candidates:
            # This shouldn't happen if the problem has a solution
            break

    return min(candidates) if candidates else -1


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
