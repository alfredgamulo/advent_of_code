import sys
from collections import defaultdict

lines = sys.stdin.readlines()


def get_instruction():
    for line in lines:
        words = line.strip().split(" ")
        a = tuple(map(int, words[-3].split(",")))
        b = tuple(map(int, words[-1].split(",")))
        i = " ".join(words[-4::-1][::-1])
        yield a, b, i


def part1():
    m = defaultdict(bool)

    instruction = {
        "turn on": lambda x: True,
        "turn off": lambda x: False,
        "toggle": lambda x: not x,
    }

    for a, b, i in get_instruction():
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                m[(x, y)] = instruction[i](m[(x, y)])
    return sum(m.values())


def part2():
    m = defaultdict(int)

    instruction = {
        "turn on": lambda x: x + 1,
        "turn off": lambda x: x > 1 and x - 1 or 0,
        "toggle": lambda x: x + 2,
    }

    for a, b, i in get_instruction():
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                m[(x, y)] = instruction[i](m[(x, y)])
    return sum(m.values())


print("Part 1:", part1())
print("Part 2:", part2())
