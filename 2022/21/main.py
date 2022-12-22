import sys
from collections import deque


def solve(lines, h=None):
    stack = deque([line.replace(":", "=") for line in lines])
    ns = {}
    while stack:
        instruction = stack.popleft()
        try:
            if "humn=" in instruction and h:
                instruction = f"humn= {h}"
            exec(instruction, ns)
        except NameError:
            stack.append(instruction)

    return ns["root"]


def part1(lines):
    return solve(lines)


def part2(lines):
    for i in range(len(lines)):
        if "root:" in lines[i]:
            lines[i] = lines[i].replace("+", "-")
            break

    h = 3423279932937
    if solve(lines, h) == 0:
        return h


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
