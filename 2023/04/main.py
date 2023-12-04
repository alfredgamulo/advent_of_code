import re
import sys
from collections import defaultdict


def solve(cards):
    part1 = 0
    multipliers = defaultdict(int)
    for id, numbers in enumerate(cards, 1):
        if matches := len(next(numbers).intersection(next(numbers))):
            part1 += 2 ** (matches - 1)
        for future in range(1, matches + 1):
            multipliers[id + future] += multipliers[id] + 1
    return part1, sum(multipliers.values()) + len(cards)


if __name__ == "__main__":
    cards = [
        map(
            lambda card: set(re.findall("(\\d+)", card)),
            line.split(":")[1].split("|"),
        )
        for line in sys.stdin.read().splitlines()
    ]
    part1, part2 = solve(cards)
    print("Part 1:", part1)
    print("Part 2:", part2)
