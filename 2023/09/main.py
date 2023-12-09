import sys
from pathlib import Path


def solve(sequence):
    if not any(sequence):
        return 0
    new_number = solve(list(s2 - s1 for s1, s2 in zip(sequence, sequence[1:])))
    return sequence[-1] + new_number


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()

    print("Part 1:", sum(solve(list(map(int, line.split()))) for line in lines))
    print("Part 2:", sum(solve(list(map(int, line.split()))[::-1]) for line in lines))
