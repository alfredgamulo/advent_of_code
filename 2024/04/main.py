import sys
from collections import defaultdict
from pathlib import Path


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


def part1(lines):
    rows = list(map(lambda s: "".join(s), groups(lines, lambda x, y: y)))
    cols = list(map(lambda s: "".join(s), groups(lines, lambda x, y: x)))
    dia1 = list(map(lambda s: "".join(s), groups(lines, lambda x, y: x + y)))
    dia2 = list(map(lambda s: "".join(s), groups(lines, lambda x, y: x - y)))
    search = rows + cols + dia1 + dia2
    return sum(s.count("XMAS") + s.count("SAMX") for s in search)


def part2(lines):
    ans = 0
    for x in range(1, len(lines) - 1):
        for y in range(1, len(lines[0]) - 1):
            if lines[x][y] == "A":
                x1 = lines[x - 1][y - 1] + lines[x + 1][y + 1]
                x2 = lines[x - 1][y + 1] + lines[x + 1][y - 1]
                if x1 in ("SM", "MS") and x2 in ("SM", "MS"):
                    ans += 1
    return ans


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    lines = list(map(list, lines))
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
