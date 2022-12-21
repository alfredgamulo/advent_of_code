import sys
from collections import namedtuple
from itertools import product


def solve(lines, key=1, times=1):
    Number = namedtuple("Number", "n, i")
    coords = [Number(int(line) * key, i) for i, line in enumerate(lines)]
    decrypted = coords[:]

    z = None
    for _, c in product(range(times), coords):
        i = decrypted.index(c)
        if not z and c.n == 0:
            z = c
        decrypted.pop(i)
        decrypted.insert(((i + c.n) % len(decrypted)), c)

    zi = decrypted.index(z)
    return sum(decrypted[(zi + i) % len(decrypted)].n for i in (1000, 2000, 3000))


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    print("Part 1:", solve(lines))
    print("Part 2:", solve(lines, 811589153, 10))
