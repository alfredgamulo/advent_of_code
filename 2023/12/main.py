import sys
from functools import cache
from itertools import groupby, product
from pathlib import Path


def get_patterns(arrangement):
    return set(product(*(a == "?" and "#." or a for a in arrangement)))


@cache
def matches(arrangement, information):
    return sum(
        information
        == tuple(
            len(list(group)) for spring, group in groupby(pattern) if spring == "#"
        )
        for pattern in get_patterns(arrangement)
    )


def part1(lines):
    total = 0
    for line in lines:
        arrangement, information = line.split()
        information = tuple(map(int, information.split(",")))
        total += matches(arrangement, information)

    return total


def part2(lines):
    total = 0
    for line in lines:
        arrangement, information = line.split()
        arrangement = "?".join([arrangement] * 5)
        information = list(map(int, information.split(",")))
        information = tuple(information * 5)
        # total += matches(arrangement, information)

    return total


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
