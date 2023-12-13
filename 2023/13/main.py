import sys
from pathlib import Path


def find(pattern, tolerance=0):
    for i in range(1, len(pattern)):
        if tolerance == sum(
            c != d
            for a, b in zip(pattern[i - 1 :: -1], pattern[i:])
            for c, d in zip(a, b)
        ):
            return i
    return False


def solve(patterns, tolerance=0):
    return sum(
        (100 * find(pattern, tolerance)) or find(list(zip(*pattern)), tolerance)
        for pattern in patterns
    )


if __name__ == "__main__":
    patterns = list(map(str.split, Path(sys.argv[1]).read_text().split("\n\n")))
    print("Part 1:", solve(patterns))
    print("Part 2:", solve(patterns, 1))
