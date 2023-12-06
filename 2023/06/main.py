import re
import sys
from math import prod


def solve(times, dists):
    return prod(
        sum(seconds * (time - seconds) > dist for seconds in range(time + 1))
        for time, dist in zip(times, dists)
    )


def part1(lines):
    times = map(int, re.findall("\\d+", lines[0]))
    dists = map(int, re.findall("\\d+", lines[1]))
    return solve(times, dists)


def part2(lines):
    time = int("".join(re.findall("\\d+", lines[0])))
    dist = int("".join(re.findall("\\d+", lines[1])))
    return solve([time], [dist])


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
