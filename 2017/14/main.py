import sys
from functools import reduce

from more_itertools import grouper


def knot(string):
    lengths = list(map(ord, string))
    lengths.extend([17, 31, 73, 47, 23])  # magic input
    loop = list(range(256))  # magic number
    curr = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            for i in iter(range(length // 2)):
                swap = loop[(curr + i) % 256]
                loop[(curr + i) % 256] = loop[(curr + length - i - 1) % 256]
                loop[(curr + length - i - 1) % 256] = swap
            curr += length + skip
            skip += 1
    dense = []
    for g in grouper(loop, 16):
        dense.append(reduce(lambda x, y: x ^ y, g))
    return "".join(map(lambda n: f"{n:02x}", dense))


def hex_to_bin(hexval):
    return bin(int(hexval, 16))[2:].zfill(4)


disk = set()


def part1(lines):
    key = lines[0].strip()
    global disk
    for n in range(128):
        row = knot(f"{key}-{n}")
        bins = hex_to_bin(row).zfill(128)
        for i in range(128):
            if bins[i] == "1":
                disk.add((n, i))
    return len(disk)


def part2():
    # This is a counting islands problem
    pass


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
