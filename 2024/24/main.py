try:
    import numpy as np
except Exception:
    np = None
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
    # Parse initial wire values and gate definitions, then simulate until steady state.
    values = {}
    gates = []  # (a, b, op, out)

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # initial assignment like: x00: 1
        if ":" in line:
            name, val = line.split(":", 1)
            values[name.strip()] = int(val.strip())
            continue

        # gate line like: a AND b -> c
        m = re.match(r"(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)", line)
        if not m:
            raise ValueError(f"Unrecognized instruction: {line}")
        a, op, b, out = m.groups()
        gates.append((a, b, op, out))

    # Evaluate gates until no further changes (acyclic graph guarantees termination)
    progress = True
    while progress:
        progress = False
        for a, b, op, out in gates:
            if out in values:
                continue
            if a in values and b in values:
                av = values[a]
                bv = values[b]
                if op == "AND":
                    res = av & bv
                elif op == "OR":
                    res = av | bv
                elif op == "XOR":
                    res = av ^ bv
                else:
                    raise ValueError(f"Unknown op: {op}")
                values[out] = int(bool(res))
                progress = True

    # Combine z-bit wires: z00 is least-significant bit (bit 0)
    z_bits = {}
    for name, val in values.items():
        m = re.match(r"^z(\d+)$", name)
        if m:
            idx = int(m.group(1))
            z_bits[idx] = val

    if not z_bits:
        return 0

    result = 0
    for idx, bit in z_bits.items():
        if bit:
            result |= (1 << idx)
    return result


def part2(lines):
    gates = {}
    for line in lines:
        line = line.strip()
        if "->" in line:
            m = re.match(r"(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)", line)
            if m:
                a, op, b, out = m.groups()
                gates[out] = (a, op, b)

    # Reverse lookup: wire -> list of gates where wire is an input
    wire_usage = defaultdict(list)
    for out, (a, op, b) in gates.items():
        wire_usage[a].append((out, op))
        wire_usage[b].append((out, op))

    suspicious = set()

    max_z = "z00"
    for out in gates:
        if out.startswith("z") and out > max_z:
            max_z = out

    for out, (a, op, b) in gates.items():
        # Rule 1: If output is z (and not last z), op must be XOR
        if out.startswith("z") and out != max_z:
            if op != "XOR":
                suspicious.add(out)

        # Rule 2: If op is XOR and output is not z, inputs must be x and y
        if op == "XOR" and not out.startswith("z"):
            is_xy_input = (a.startswith("x") or a.startswith("y")) and (b.startswith("x") or b.startswith("y"))
            if not is_xy_input:
                suspicious.add(out)

        # Rule 3: If op is XOR and inputs are x and y (and not x00, y00), output must be input to another XOR and an AND
        if op == "XOR":
            is_xy_input = (a.startswith("x") or a.startswith("y")) and (b.startswith("x") or b.startswith("y"))
            if is_xy_input:
                if "x00" in (a, b): continue

                usages = wire_usage.get(out, [])
                has_xor = False
                has_and = False
                for _, next_op in usages:
                    if next_op == "XOR": has_xor = True
                    if next_op == "AND": has_and = True

                if not (has_xor and has_and):
                    suspicious.add(out)

        # Rule 4: If op is AND and inputs are x and y (and not x00, y00), output must be input to an OR
        if op == "AND":
            is_xy_input = (a.startswith("x") or a.startswith("y")) and (b.startswith("x") or b.startswith("y"))
            if is_xy_input:
                if "x00" in (a, b): continue

                usages = wire_usage.get(out, [])
                has_or = False
                for _, next_op in usages:
                    if next_op == "OR": has_or = True

                if not has_or:
                    suspicious.add(out)

    return ",".join(sorted(list(suspicious)))


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
