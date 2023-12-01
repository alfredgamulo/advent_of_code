import re
import sys


def part1(lines):
    values = map(lambda r: re.findall("\\d", r), lines)
    return sum(int(v[0] + v[-1]) for v in values if v)


def part2(lines):
    helper = {
        "one": "o1e",
        "two": "t2",
        "three": "t3e",
        "four": "4",
        "five": "5e",
        "six": "6",
        "seven": "7",
        "eight": "e8t",
        "nine": "9e",
        "zero": "0o",
    }

    for i in range(len(lines)):
        for word, number in helper.items():
            lines[i] = lines[i].replace(word, number)
    return part1(lines)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
