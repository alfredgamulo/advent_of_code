import sys
from functools import cache
from itertools import product

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

quantum_moves = [sum(rolls) for rolls in (product([1,2,3], repeat=3))]

@cache
def part2(player1, score1, player2, score2, turn=True):
    if score1 >= 21:
        return 1
    if score2 >= 21:
        return 0
    if turn:
        moves = [(player1 + moves - 1) % 10 + 1 for moves in quantum_moves]
        results = (part2(move, score1 + move, player2, score2, not turn) for move in moves)
    else:
        moves = [(player2 + moves - 1) % 10 + 1 for moves in quantum_moves]
        results = (part2(player1, score1, move, score2 + move, not turn) for move in moves)
    return sum(results)

print("Part 2:", part2(player1, 0, player2, 0))