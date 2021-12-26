import sys
from functools import cache, reduce

program = []
subprogram = None
for p in [p.split() for p in sys.stdin.readlines()]:
    if "inp" in p:
        if subprogram:
            program.append(subprogram)
        subprogram = []
    subprogram.append(p)
program.append(subprogram)

bees = [1,1,1,1,26,1,1,26,1,26,26,26,26,26]

register_lookup = {
            "w": 0,
            "x": 1,
            "y": 2,
            "z": 3,
        }

@cache
def run_sub(subprogram, registers, n):
    registers = list(registers)
    for instruction in program[subprogram]:
        match instruction[0]:
            case "inp":
                registers[register_lookup[instruction[1]]] = n
            case "add":
                registers[register_lookup[instruction[1]]] = registers[register_lookup[instruction[1]]] + int(register_lookup.get(instruction[2], instruction[2]))
            case "mul":
                registers[register_lookup[instruction[1]]] = registers[register_lookup[instruction[1]]] * int(register_lookup.get(instruction[2], instruction[2]))
            case "div":
                registers[register_lookup[instruction[1]]] = registers[register_lookup[instruction[1]]] // int(register_lookup.get(instruction[2], instruction[2]))
            case "mod":
                registers[register_lookup[instruction[1]]] = registers[register_lookup[instruction[1]]] % int(register_lookup.get(instruction[2], instruction[2]))
            case "eql":
                registers[register_lookup[instruction[1]]] = registers[register_lookup[instruction[1]]] == int(register_lookup.get(instruction[2], instruction[2])) and 1 or 0
    return tuple(registers)

@cache
def work(subprogram, registers, model):
    print(model, flush=True)
    registers = list(registers)
    models = []
    if subprogram == 14:
        if registers[3] == 0:
            return model
        return None
    for i in range(1,10):
        registers = run_sub(subprogram, tuple(registers), i)
        
        if registers[3] >= reduce(lambda x, y: x*y, bees[subprogram:]):
            return None
        recurse = work(subprogram+1, tuple(registers), model+str(i))
        if recurse:
            models.append(recurse)
    if registers[3] >= reduce(lambda x, y: x*y, bees[subprogram:]):
        return None
    return models

part1 = work(0, (0,0,0,0), "")

print("Part 1:", part1)
