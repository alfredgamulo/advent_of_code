import sys


def part1(lines):
    i = 0
    steps = 0
    while i >= 0 and i < len(lines):
        j = i + lines[i]
        lines[i] += 1
        i = j
        steps += 1
    return steps


def part2(lines):
    i = 0
    steps = 0
    while i >= 0 and i < len(lines):
        j = i + lines[i]
        lines[i] += lines[i] >= 3 and -1 or 1
        i = j
        steps += 1
    return steps


if __name__ == "__main__":
    lines = list(map(int, sys.stdin.readlines()))

    print("Part 1:", part1(lines.copy()))
    print("Part 2:", part2(lines.copy()))
