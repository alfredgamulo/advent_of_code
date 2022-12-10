import sys
from itertools import count

from more_itertools import grouper


def run(lines):
    gen = (line for line in lines)
    x = 1
    addx = False
    capture_times = [20, 60, 100, 140, 180, 220]
    capture_total = 0
    display = ""

    for c in count(1):
        if (c - 1) % 40 in (x - 1, x, x + 1):
            display += "#"
        else:
            display += "."
        if c in capture_times:
            capture_total += x * c
        if addx:
            x += addx
            addx = False
            continue
        try:
            instruction = next(gen).split()
            # print(instruction)
        except StopIteration:
            break
        if instruction[0] == "noop":
            continue
        else:
            addx = int(instruction[1])
    print("Part 1:", capture_total)
    print("Part 2:")
    for g in grouper(display, 40, incomplete="ignore"):
        print("".join(g))


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    run(lines)
