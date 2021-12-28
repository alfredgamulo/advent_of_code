import sys
from pprint import PrettyPrinter
from collections import deque
import copy

pp = PrettyPrinter()

instructions = {}
evaluated = deque()

for circuit in sys.stdin.readlines():
    left, right = circuit.split(" -> ")
    right = right.strip()
    left = left.strip()
    if "NOT" in left:
        instructions[right] = left.replace("NOT", "~")
    elif "AND" in left:
        instructions[right] = left.replace("AND", "&")
    elif "OR" in left:
        instructions[right] = left.replace("OR", "|")
    elif "LSHIFT" in left:
        instructions[right] = left.replace("LSHIFT", "<<")
    elif "RSHIFT" in left:
        instructions[right] = left.replace("RSHIFT", ">>")
    else:
        try:
            instructions[right] = int(left)
            evaluated.append(right)
        except ValueError:
            instructions[right] = left


def evaluate(instructions, evaluated):
    while evaluated:
        key = evaluated.popleft()
        for k, v in instructions.items():
            if type(v) == str and {key}.intersection(v.split(" ")):
                instructions[k] = v.replace(key, str(instructions[key]))
                try:
                    instructions[k] = int(eval(instructions[k]))
                    evaluated.append(k)
                except:
                    pass
    return instructions


instructions2 = copy.deepcopy(instructions)
evaluated2 = copy.deepcopy(evaluated)

part1 = evaluate(instructions, evaluated)["a"]
print("Part 1:", part1)

instructions2["b"] = part1
part2 = evaluate(instructions2, evaluated2)["a"]
print("Part 2:", part2)
