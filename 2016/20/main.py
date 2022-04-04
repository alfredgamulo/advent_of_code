import sys


def part1(lines):
    lowest = 0
    while True:
        temp_lowest = lowest
        for line in lines:
            x, y = list(map(int, line.split("-")))
            if lowest >= x and lowest <= y:
                lowest = y + 1
        if temp_lowest == lowest:
            return lowest


def part2(lines):
    lowest = 0
    highest = 2**32 - 1
    count = 0
    while True:
        temp_lowest = lowest
        for line in lines:
            x, y = list(map(int, line.split("-")))
            if lowest >= x and lowest <= y:
                lowest = y + 1
        if temp_lowest == lowest:
            count += 1
            lowest += 1
        if lowest == highest + 1:
            return count


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
