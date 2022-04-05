import sys


def part1(lines):
    valid = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            valid += 1
    return valid


def part2(lines):
    valid = 0
    for line in lines:
        words = line.split()
        if len(words) != len(set(words)):
            continue
        unique = set()
        for w in words:
            chars = sorted(list(w))
            unique.add("".join(chars))
        if len(words) == len(unique):
            valid += 1

    return valid


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
