import re
import sys
from collections import defaultdict


def solve(cards):
    part1 = 0
    part2 = 0
    multipliers = defaultdict(int)
    for id, numbers in enumerate(cards, 1):
        if matches := len(next(numbers).intersection(next(numbers))):
            part1 += 2 ** (matches - 1)
        part2 += (instances := multipliers[id] + 1)
        for future in range(1, matches + 1):
            multipliers[id + future] += instances

    return part1, part2


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
