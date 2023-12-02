import sys
from collections import defaultdict
from math import prod


def solve(handfuls):
    rules = {"red": 12, "green": 13, "blue": 14}
    possible = True
    maxes = defaultdict(lambda: 0)
    for handful in handfuls.split(";"):
        for cubes in handful.split(","):
            amount, color = cubes.split()
            if int(amount) > rules[color] and possible:
                possible = False
            if int(amount) > maxes[color]:
                maxes[color] = int(amount)
    return possible, prod(maxes.values())


if __name__ == "__main__":
    games = sys.stdin.read().splitlines()

    answer1 = 0
    answer2 = 0
    for game in games:
        id, handfuls = game.split(":")
        id = int(id.split()[-1])
        part1, part2 = solve(handfuls)
        if part1:
            answer1 += id
        answer2 += part2

    print("Part 1:", answer1)
    print("Part 2:", answer2)
