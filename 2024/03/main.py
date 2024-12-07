import re
import sys
from pathlib import Path


def mul(a, b):
    return a * b


def part1(lines):
    ans = 0
    for line in lines:
        for m in re.finditer(r"mul\(\d+,\d+\)", line):
            ans += eval(m.group())
    return ans


def part2(lines):
    ans = 0
    enabled = True
    for line in lines:
        for m in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            match m.group():
                case("do()"):
                    enabled = True
                case("don't()"):
                    enabled = False
                case found:
                    if enabled:
                        ans += eval(found)
    return ans


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
