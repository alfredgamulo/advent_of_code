import re
import sys
from collections import defaultdict
from functools import cache

symbols = "#%&*+-/=@$"


def parse(lines):
    numbers, symbols = {}, {}
    for i, line in enumerate(lines):
        for finding in re.finditer("\\d+|[^.]", line):
            start, end = (i, finding.start()), (i, finding.end())
            try:
                num = int(finding.group())
                numbers[(start, end)] = num
            except ValueError:
                symbols[(start)] = finding.group()
    return numbers, symbols


@cache
def neighbors(coords):
    adjacentset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighborset = set()
    x = coords[0][0]
    for y in range(coords[0][1], coords[1][1]):
        for a in adjacentset:
            if x + a[0] == x and y + a[1] in range(coords[0][1], coords[1][1]):
                continue
            neighborset.add(((x + a[0], y + a[1])))
    return neighborset


def part1(numbers, symbols):
    parts = 0
    for coords, num in numbers.items():
        neighborset = neighbors(coords)
        if any(n in symbols.keys() for n in neighborset):
            parts += num
    return parts


def part2(numbers, symbols):
    gear_ratios = defaultdict(list)
    gear_coords = list(filter(lambda s: symbols[s] == "*", symbols))
    for coords, num in numbers.items():
        neighborset = neighbors(coords)
        for g in gear_coords:
            if g in neighborset:
                gear_ratios[g].append(num)
    return sum(
        gear_ratios[gear][0] * gear_ratios[gear][1]
        for gear in filter(lambda g: len(gear_ratios[g]) == 2, gear_ratios)
    )


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    numbers, symbols = parse(lines)
    print("Part 1:", part1(numbers, symbols))
    print("Part 2:", part2(numbers, symbols))
