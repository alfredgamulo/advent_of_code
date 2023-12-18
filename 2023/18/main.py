import sys
from pathlib import Path


def solve(func):
    curr, trench, perimeter = (0, 0), [], 0
    for line in lines:
        d, v = func(line)
        trench.append((curr, curr := (curr[0] + d[0] * v, curr[1] + d[1] * v)))
        perimeter += int(v)
    area = sum((a * d) - (c * b) for ((a, b), (c, d)) in trench)  # shoelace
    interior = int((0.5 * abs(area)) - (perimeter / 2) + 1)  # Pick's
    return perimeter + interior


def part1():
    return solve(lambda line: (dv := line.split()) and (dirs[dv[0]], int(dv[1])))


def part2():
    return solve(
        lambda line: (h := line.split()[-1][2:-1])
        and (dirs["RDLU"[int(h[-1])]], int(h[:-1], 16))
    )


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
    for p in "12":
        print(f"Part {p}:", locals()[f"part{p}"]())
