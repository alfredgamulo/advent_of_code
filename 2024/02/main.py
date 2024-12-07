import sys

from pathlib import Path


def is_safe(line, tolerance=0):
    if line[0] < line[1]:
        line.reverse()
    diffs = list(x - y for (x, y) in zip(line, line[1:]))
    count = 0
    for i in range(len(diffs)):
        d = diffs[i]
        if not 0 < d < 4:
            count += 1
            try:
                diffs[i + 1] = line[i] - line[i+2]
            except:
                ...
    return count <= tolerance


def part1(lines):
    count = 0
    for line in lines:
        count += is_safe(list(map(int, line.split(" "))))
    return count


def part2(lines):
    count = 0
    for line in lines:
        count += is_safe(list(map(int, line.split(" "))), 1)
    return count


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
