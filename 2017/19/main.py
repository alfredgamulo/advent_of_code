import sys
from collections import deque
from itertools import cycle
from string import ascii_uppercase


def solve(lines):
    # populate the network
    network = {}
    for row, line in enumerate(lines):
        for column, character in enumerate(line[:-1]):
            if character != " ":
                network[(row, column)] = character

    # find the root
    position = None
    for c in range(len(line)):
        if network.get((0, c)) == "|":
            position = (0, c)

    adjs = {"horz": ((0, -1), (0, 1)), "vert": ((-1, 0), (1, 0))}
    lins = {"vert": "|", "horz": "-"}
    toggle = cycle(("vert", "horz"))
    direction = next(toggle)

    # Traverse
    stack = deque([position])
    count = 0
    letters = []
    x = 1
    y = 0
    while stack:
        pos = stack.popleft()
        count += 1
        if network[pos] in ascii_uppercase:
            letters.append(network[pos])
        if network[pos] != "+":
            if (pos[0] + x, pos[1] + y) in network:
                stack.append((pos[0] + x, pos[1] + y))
                continue
        else:
            direction = next(toggle)
            for (i, j) in adjs[direction]:
                if (pos[0] + i, pos[1] + j) in network and network[
                    (pos[0] + i, pos[1] + j)
                ] == lins[direction]:
                    x = i
                    y = j
                    stack.append((pos[0] + i, pos[1] + j))

    print("Part 1:", "".join(letters))
    print("Part 2:", count)


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    solve(lines)
