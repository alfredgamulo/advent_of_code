import re
import sys
from collections import defaultdict
from math import prod


def parse(lines):
    numbers, symbols = {}, {}
    for i, line in enumerate(lines):
        for finding in re.finditer("\\d+|[^.]", line):
            start, end = (i, finding.start()), (i, finding.end())
            try:
                numbers[(start, end)] = int(finding.group())
            except ValueError:
                symbols[(start)] = finding.group()
    return numbers, symbols


def neighbors(span):
    adjacentset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighborset = set()
    x = span[0][0]
    for y in range(span[0][1], span[1][1]):
        for a in adjacentset:
            if a[0] == 0 and y + a[1] in range(span[0][1], span[1][1]):
                continue
            neighborset.add(((x + a[0], y + a[1])))
    return neighborset


def solve(numbers, symbols):
    part1 = 0
    gear_ratios = defaultdict(list)
    gear_coords = set(filter(lambda s: symbols[s] == "*", symbols))
    for span, num in numbers.items():
        neighborset = neighbors(span)
        part1 += num * any(n in symbols.keys() for n in neighborset)
        if intersection := gear_coords.intersection(neighborset):
            gear_ratios[tuple(intersection)].append(num)

    part2 = sum(
        prod(gear_ratios[gear])
        for gear in filter(lambda g: len(gear_ratios[g]) == 2, gear_ratios)
    )
    return part1, part2


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    numbers, symbols = parse(lines)
    part1, part2 = solve(numbers, symbols)
    print("Part 1:", part1)
    print("Part 2:", part2)
