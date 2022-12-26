import math
import sys


def val(registers, v):
    try:
        return int(v)
    except ValueError:
        return registers[v]


def part1(lines):
    registers = {c: 0 for c in "abcdefgh"}
    pointer = 0
    count = 0
    while pointer < len(lines):
        match lines[pointer].split():
            case ["set", x, y]:
                registers[x] = val(registers, y)
            case ["sub", x, y]:
                registers[x] -= val(registers, y)
            case ["mul", x, y]:
                registers[x] = val(registers, x) * val(registers, y)
                count += 1
            case ["jnz", x, y]:
                if val(registers, x) != 0:
                    pointer += val(registers, y) - 1
        pointer += 1
    return count


def isPrime(x):
    for mult in range(2, int(math.sqrt(x) + 1)):
        if x % mult == 0:
            return False
    return True


def part2():
    b = 108100
    h = 0
    while b <= 125100:
        h += 0 if isPrime(b) else 1
        b += 17
    return h


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
