import sys
from functools import cmp_to_key
from itertools import zip_longest
from math import prod


def compare(left, right):
    match left, right:
        case int(l), int(r):
            return l < r if l != r else None
        case int(l), list(r):
            return compare([l], r)
        case list(l), int(r):
            return compare(l, [r])
        case list(l), list(r):
            for x, y in zip_longest(l, r):
                if x is None:
                    return True
                if y is None:
                    return False
                if (found := compare(x, y)) is not None:
                    return found


def part1(lines):
    return sum(
        i * compare(*(eval(packet) for packet in pair.splitlines()))
        for i, pair in enumerate(lines, start=1)
    )


def cmp_wrapper(left, right):
    return -1 if compare(left, right) else 1


def part2(lines):
    dividers = [[[2]], [[6]]]
    packets = [
        eval(packet) for pair in lines for packet in pair.splitlines()
    ] + dividers
    packets.sort(key=cmp_to_key(cmp_wrapper))
    return prod(packets.index(d) + 1 for d in dividers)


if __name__ == "__main__":
    lines = sys.stdin.read().split("\n\n")

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
