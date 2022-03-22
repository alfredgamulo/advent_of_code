import sys
from functools import reduce

# Use Chinese Remainder Theorem:
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


# A shortcut for this: `mod_inverse = pow(div, -1, t)`
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part1(discs):
    n = [d[0] for d in discs]
    a = [(d[0] - d[1] - i - 1) for i, d in enumerate(discs)]
    return chinese_remainder(n, a)


def part2(discs):
    discs.append((11, 0))
    return part1(discs)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    discs = []
    for line in lines:
        _, _, _, x, *_, y = line.strip()[:-1].split(" ")
        discs.append((int(x), int(y)))

    print("Part 1:", part1(discs))
    print("Part 2:", part2(discs))
