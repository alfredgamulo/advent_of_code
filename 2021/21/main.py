import sys
from functools import cache
from itertools import product

p1, p2 = map(lambda s: int(s.split(":")[-1].strip()), sys.stdin.readlines())


def die(sides, counter):
    number = 0
    while True:
        counter[0] += 1
        number = (number) % sides + 1
        yield number


def part1(p1, p2):
    roll_counter = [0]
    roll = die(100, roll_counter)
    s1 = 0
    s2 = 0
    while True:
        spaces = next(roll) + next(roll) + next(roll)
        p1 = (p1 + spaces - 1) % 10 + 1
        s1 += p1
        if s1 >= 1000:
            break

        spaces = next(roll) + next(roll) + next(roll)
        p2 = (p2 + spaces - 1) % 10 + 1
        s2 += p2
        if s2 >= 1000:
            break
    return min(s1, s2) * roll_counter[0]


print("Part 1:", part1(p1, p2))

quantum_moves = [sum(rolls) for rolls in (product([1, 2, 3], repeat=3))]


@cache
def part2(p1, s1, p2, s2, turn=True):
    if s1 >= 21:
        return 1
    if s2 >= 21:
        return 0
    if turn:
        moves = [(p1 + moves - 1) % 10 + 1 for moves in quantum_moves]
        results = (part2(move, s1 + move, p2, s2, not turn) for move in moves)
    else:
        moves = [(p2 + moves - 1) % 10 + 1 for moves in quantum_moves]
        results = (part2(p1, s1, move, s2 + move, not turn) for move in moves)
    return sum(results)


print("Part 2:", part2(p1, 0, p2, 0))
