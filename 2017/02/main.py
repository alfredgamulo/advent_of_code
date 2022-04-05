import sys
from itertools import combinations


def part1(lines):
    checksum = 0
    for line in lines:
        nums = list(map(int, line.split("\t")))
        checksum += max(nums) - min(nums)
    return checksum


def part2(lines):
    checksum = 0
    for line in lines:
        nums = list(map(int, line.split("\t")))
        for i, j in combinations(nums, 2):
            if i % j == 0:
                checksum += i // j
            if j % i == 0:
                checksum += j // i
    return checksum


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
