import sys
from collections import defaultdict
from math import prod


def solve(handfuls):
    rules = {"red": 12, "green": 13, "blue": 14}
    maxes = defaultdict(int)
    for handful in handfuls.split(";"):
        for cubes in handful.split(","):
            amount, color = cubes.split()
            maxes[color] = max(int(amount), maxes[color])
    part1 = all(a >= maxes[c] for c, a in rules.items())
    part2 = prod(maxes.values())
    return part1, part2


if __name__ == "__main__":
    games = sys.stdin.read().splitlines()

    answer1 = 0
    answer2 = 0
    for id, game in enumerate(games, 1):
        handfuls = game.split(":")[1]
        part1, part2 = solve(handfuls)
        answer1 += part1 * id
        answer2 += part2

    print("Part 1:", answer1)
    print("Part 2:", answer2)
