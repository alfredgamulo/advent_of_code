import sys
from functools import reduce

from more_itertools import grouper

string = 256


def part1(lines):
    lengths = list(map(int, lines.split(",")))
    loop = list(range(string))
    curr = 0
    skip = 0
    for length in lengths:
        for i in iter(range(length // 2)):
            swap = loop[(curr + i) % string]
            loop[(curr + i) % string] = loop[(curr + length - i - 1) % string]
            loop[(curr + length - i - 1) % string] = swap
        curr += length + skip
        skip += 1
    return loop[0] * loop[1]


def part2(lines):
    lengths = list(map(ord, lines.strip()))
    lengths.extend([17, 31, 73, 47, 23])  # magic input
    loop = list(range(string))
    curr = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            for i in iter(range(length // 2)):
                swap = loop[(curr + i) % string]
                loop[(curr + i) % string] = loop[(curr + length - i - 1) % string]
                loop[(curr + length - i - 1) % string] = swap
            curr += length + skip
            skip += 1

    dense = []
    for g in grouper(loop, 16):
        dense.append(reduce(lambda x, y: x ^ y, g))
    return "".join(map(lambda n: f"{n:02x}", dense))


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines[0]))
    print("Part 2:", part2(lines[0]))
