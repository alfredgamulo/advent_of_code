import sys

ma = 16807
mb = 48271
md = 2147483647


def part1(a, b):
    matches = 0
    for _ in range(40000000):
        a = a * ma % md
        b = b * mb % md
        if (a & 0xFFFF) == (b & 0xFFFF):
            matches += 1
    return matches


def gena(a):
    while True:
        a = a * ma % md
        if a % 4 == 0:
            yield a


def genb(b):
    while True:
        b = b * mb % md
        if b % 8 == 0:
            yield b


def part2(a, b):
    ga = gena(a)
    gb = genb(b)
    matches = 0
    for _ in range(5000000):
        if (next(ga) & 0xFFFF) == (next(gb) & 0xFFFF):
            matches += 1
    return matches


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])
    print("Part 1:", part1(a, b))
    print("Part 2:", part2(a, b))
