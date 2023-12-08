import re
import sys
from functools import reduce
from itertools import cycle


def solve(instructions, network, cursor, end):
    for step, instruction in enumerate(cycle(instructions), 1):
        cursor = network[cursor]["LR".index(instruction)]
        if re.match(end, cursor):
            return step


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        instructions, maps = f.read().split("\n\n")
    network = {}
    for m in maps.splitlines():
        nodes = re.findall("[0-9A-Z]+", m)
        network[nodes[0]] = (nodes[1], nodes[2])

    part1 = solve(instructions, network, "AAA", "ZZZ")
    part2 = reduce(
        lcm,
        (
            solve(instructions, network, cursor, "..Z")
            for cursor in [node for node in network if node.endswith("A")]
        ),
    )

    print("Part 1:", part1)
    print("Part 2:", part2)
