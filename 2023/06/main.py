import sys
from math import prod


def solve(times, dists):
    return prod(
        sum(seconds * (time - seconds) > dist for seconds in range(time + 1))
        for time, dist in zip(times, dists)
    )


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    times = lines[0].split(":")[1].split()
    dists = lines[1].split(":")[1].split()
    print("Part 1:", solve(map(int, times), map(int, dists)))
    print("Part 2:", solve([int("".join(times))], [int("".join(dists))]))
