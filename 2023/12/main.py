import sys
from contextlib import suppress
from functools import cache
from itertools import groupby, product
from pathlib import Path


def part1(lines):
    total = 0
    for line in lines:
        arrangement, information = line.split()
        information = tuple(map(int, information.split(",")))
        # total += sum(
        #     information
        #     == tuple(
        #         len(list(group)) for spring, group in groupby(pattern) if spring == "#"
        #     )
        #     for pattern in product(*(a == "?" and "#." or a for a in arrangement))
        # )
        total += recurse(arrangement, information, 0)

    return total


@cache
def recurse(line, numbers, buffer_size):
    if not line:
        return (len(numbers) == 1 and numbers[0] == buffer_size) or (
            not (numbers or buffer_size)
        )
    with suppress(IndexError):
        if numbers[0] < buffer_size:
            return 0
    n = 0
    if line[0] in "#?":
        n += recurse(line[1:], numbers, buffer_size + 1)
    if line[0] in ".?":
        if buffer_size == 0:
            n += recurse(line[1:], numbers, 0)
        elif numbers and numbers[0] == buffer_size:
            n += recurse(line[1:], numbers[1:], 0)
    return n


def part2(lines):
    total = 0
    for line in lines:
        arrangement, information = line.split()
        arrangement = "?".join([arrangement] * 5)
        information = list(map(int, information.split(",")))
        information = tuple(information * 5)
        total += recurse(arrangement, information, 0)

    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
