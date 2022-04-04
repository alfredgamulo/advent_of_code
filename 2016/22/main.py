import sys
from itertools import product


def solve(lines):
    nodes = {}
    for line in lines[2:]:
        node, size, used, avail, perc = line.split()
        x, y = node.split("-")[-2:]
        x = int(x[1:])
        y = int(y[1:])
        if int(perc[:-1]) < 90:
            nodes[(x, y)] = {
                "size": int(size[:-1]),
                "used": int(used[:-1]),
                "avail": int(avail[:-1]),
            }

    viable = 0
    for a, b in product(nodes.keys(), nodes.keys()):
        if a == b:
            continue
        if nodes[a]["used"] > 0 and nodes[a]["used"] < nodes[b]["avail"]:
            viable += 1
    print("Part 1:", viable)

    print("Part 2:")
    for y in range(26):
        for x in range(38):
            if (x, y) in nodes.keys():
                if nodes[(x, y)]["used"] == 0:
                    print("_", end="")
                    continue
                print(".", end="")
            else:
                print("#", end="")
        print()


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    solve(lines)
