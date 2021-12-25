import sys
from itertools import product, chain
from io import StringIO
from collections import defaultdict
from functools import cache

program = []
subprogram = None
for p in [p.split() for p in sys.stdin.readlines()]:
    if "inp" in p:
        if subprogram:
            program.append(subprogram)
        subprogram = []
    subprogram.append(p)
program.append(subprogram)

part1 = ""

magic = -100000


def find_z_targets(subprogram, target):
    global magic
    print(magic, flush=True)
    div = 1
    z_targets = set()
    for z in range(magic, abs(magic*26)):
        for i in range(1,10):
            registers = {
                "w": 0,
                "x": 0,
                "y": 0,
                "z": z,
            }
            for instruction in subprogram:
                match instruction[0]:
                    case "inp":
                        registers[instruction[1]] = i
                    case "add":
                        registers[instruction[1]] = int(registers.get(instruction[1])) + int(registers.get(instruction[2], instruction[2]))
                    case "mul":
                        registers[instruction[1]] = int(registers.get(instruction[1])) * int(registers.get(instruction[2], instruction[2]))
                    case "div":
                        registers[instruction[1]] = int(registers.get(instruction[1])) // int(registers.get(instruction[2], instruction[2]))
                        div = int(registers.get(instruction[2], instruction[2]))
                    case "mod":
                        registers[instruction[1]] = int(registers.get(instruction[1])) % int(registers.get(instruction[2], instruction[2]))
                    case "eql":
                        registers[instruction[1]] = int(registers.get(instruction[1])) == int(registers.get(instruction[2], instruction[2])) and 1 or 0
        if registers["z"] in target:
            global part1
            part1 = str(i) + part1
            z_targets.add(z)
            magic = z * div
            return z_targets
    return z_targets


z_targets = defaultdict(set)
z_targets[14] = {0}

for i in range(14):
    p = 14 - (i + 1)
    print(p, flush=True)
    z_targets[p] = find_z_targets(program[p], z_targets[p + 1])
    print(z_targets)
    print(part1)

print("Part 1:", part1)
