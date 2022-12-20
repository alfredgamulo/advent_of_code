import sys
from dataclasses import dataclass


@dataclass
class Number:
    n: int
    _: int


def part1(coords):
    decrypted = coords[:]

    z = None
    for c in coords:
        i = decrypted.index(c)
        if not z and c.n == 0:
            z = c
        popped = decrypted.pop(i)
        decrypted.insert(((i + c.n + len(decrypted)) % len(decrypted)), popped)

    zi = decrypted.index(z)
    res = 0
    for i in (1000, 2000, 3000):
        res += decrypted[(zi + i) % len(decrypted)].n

    return res


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    coords = [Number(int(line), i) for i, line in enumerate(lines)]
    print("Part 1:", part1(coords))
    print("Part 2:", part2())
