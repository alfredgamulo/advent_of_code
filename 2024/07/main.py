import re
import sys
from collections import deque
from pathlib import Path


def solvable(target, operands):
    if len(operands) == 1:
        if operands[0] == target:
            return True
        else:
            return False
    if operands[0] > target:
        return False
    one = operands.popleft()
    two = operands.popleft()
    left = solvable(target, deque([one + two] + list(operands)))
    right = solvable(target, deque([one * two] + list(operands)))
    return left or right


def part1(equations):
    ans = 0
    for equation in equations:
        target = equation[0]
        operands = deque(equation[1:])
        s = solvable(target, operands)
        if s:
            ans += target
    return ans


def part2(equations):
    ...


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    equations = [list(map(int, re.findall(r"\d+", line))) for line in lines]
    print("Part 1:", part1(equations))
    print("Part 2:", part2(equations))
