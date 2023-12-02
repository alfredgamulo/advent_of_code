import sys
from collections import defaultdict
from math import prod


def solve(games):
    possibles, power_sum = 0, 0
    rules = {"red": 12, "green": 13, "blue": 14}

    for id, game in enumerate(games, 1):
        maxes = defaultdict(int)
        for handful in game.split(":")[1].split(";"):
            for cubes in handful.split(","):
                amount, color = cubes.split()
                maxes[color] = max(int(amount), maxes[color])

        possibles += all(a >= maxes[c] for c, a in rules.items()) * id
        power_sum += prod(maxes.values())

    return possibles, power_sum


if __name__ == "__main__":
    games = sys.stdin.read().splitlines()

    part1, part2 = solve(games)

    print("Part 1:", part1)
    print("Part 2:", part2)
