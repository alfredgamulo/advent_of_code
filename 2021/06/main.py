import sys
from functools import cache

fish = list(map(int, sys.stdin.readline().strip().split(",")))


@cache
def calculate(n, days):
    total = 0
    if days == 0:
        return 1
    if days > 0:
        if n > 0:
            total += calculate(n - 1, days - 1)
        if n == 0:
            total += calculate(6, days - 1) + calculate(8, days - 1)
    return total


def solve(days):
    total = 0
    for f in fish:
        total += calculate(f, days)
    return total


print("Part 1:", solve(80), flush=True)
print("Part 2:", solve(256), flush=True)
