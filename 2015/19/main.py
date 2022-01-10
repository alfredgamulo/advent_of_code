import sys
import re
from collections import defaultdict

input = sys.stdin.read().split("\n\n")

replacements = defaultdict(set)
for line in input[0].split("\n"):
    a, _, b = line.split()
    replacements[a].add(b)

calibration = input[1].strip()


def part1():
    molecules = set()
    for k, V in replacements.items():
        for v in V:
            for finding in re.finditer(k, calibration):
                molecules.add(
                    calibration[: finding.span()[0]]
                    + v
                    + calibration[finding.span()[1] :]
                )
    return len(molecules)


print("Part 1:", part1())


def part2():
    global calibration
    c = calibration[:]
    c = str.replace(c, "Rn", "(")
    c = str.replace(c, "Y", ",")
    c = str.replace(c, "Ar", ")")
    return sum(map(str.isupper, c)) - sum(map(lambda x: x == ",", c)) - 1


print("Part 1:", part2())
