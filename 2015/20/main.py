import sys
from functools import reduce

target = int(sys.stdin.readline())


def part1():
    def sum_houses(n):
        found = set(
            reduce(
                list.__add__,
                ([i, (n // i)] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
            )
        )
        return sum(found) * 10

    t = 1
    while True:
        if sum_houses(t) >= target:
            print("Part 1:", t)
            break
        t += 1


part1()


def part2():
    def sum_houses(n):
        found = set(
            reduce(
                list.__add__,
                ([i, (n // i)] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
            )
        )
        found = [f for f in found if f * 50 >= n]
        return sum(found) * 11

    t = 1
    while True:
        if sum_houses(t) >= target:
            print("Part 2:", t)
            break
        t += 1


part2()
