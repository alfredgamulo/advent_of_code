import string
import sys

import more_itertools


def part1(lines):
    s = 0
    for line in lines:
        c1, c2 = line[: len(line) // 2], line[len(line) // 2 :]
        common = set(c1) & set(c2)
        s += string.ascii_letters.index(common.pop()) + 1
    return s


def part2(lines):
    s = 0
    for r1, r2, r3 in more_itertools.grouper(lines, 3):
        common = set(r1) & set(r2) & set(r3)
        s += string.ascii_letters.index(common.pop()) + 1
    return s


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
