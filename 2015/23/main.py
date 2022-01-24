import sys

lines = sys.stdin.readlines()


def compute(a):
    registers = {
        "a": a,
        "b": 0,
    }
    p = 0
    while p < len(lines):
        match lines[p].split():
            case ["hlf", x]:
                registers[x] = registers[x] / 2
            case ["tpl", x]:
                registers[x] = registers[x] * 3
            case ["inc", x]:
                registers[x] = registers[x] + 1
            case ["jmp", n]:
                p += int(n) - 1
            case ["jie", x, n]:
                if registers[x[0]] % 2 == 0:
                    p += int(n) - 1
            case ["jio", x, n]:
                if registers[x[0]] == 1:
                    p += int(n) - 1
        p += 1

    return registers["b"]


print("Part 1:", compute(0))
print("Part 2:", compute(1))
