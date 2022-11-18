import sys
from collections import deque
from itertools import cycle


def part1(lines):
    print(list(lines))

    # populate the network
    network = {}
    for row, line in enumerate(lines):
        for column, character in enumerate(line[:-1]):

            if character != " ":
                print(row, column, character)
                network[(row, column)] = character

    # find the root
    position = None
    for c in range(len(line)):
        if network.get((0, c)) == "|":
            position = (0, c)

    adjs = {"cols": ((0, -1), (0, 1)), "rows": ((-1, 0), (1, 0))}
    lins = {"cols": "|", "rows": "-"}
    toggle = cycle(("rows", "cols"))
    direction = next(toggle)
    print(direction)

    stack = deque([position])
    visited = set()
    letters = []
    while stack:
        pos = stack.popleft()
        visited.add(pos)
        pass


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
