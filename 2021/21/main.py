import sys

player1, player2 = map(lambda s: int(s.split(":")[-1].strip()), sys.stdin.readlines())


def die(sides, counter):
    number = 0
    while True:
        counter[0] += 1
        number = (number) % sides + 1
        yield number


def part1(player1, player2):
    roll_counter = [0]
    roll = die(100, roll_counter)
    score1 = 0
    score2 = 0
    while True:
        spaces = next(roll) + next(roll) + next(roll)
        player1 = (player1 + spaces - 1) % 10 + 1
        score1 += player1
        if score1 >= 1000:
            break

        spaces = next(roll) + next(roll) + next(roll)
        player2 = (player2 + spaces - 1) % 10 + 1
        score2 += player2
        if score2 >= 1000:
            break
    return min(score1, score2) * roll_counter[0]


print("Part 1:", part1(player1, player2))
