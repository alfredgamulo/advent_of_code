import sys

instructions = sys.stdin.readline().strip().split(", ")

turn = {
    "N": {"L": "W", "R": "E"},
    "E": {"L": "N", "R": "S"},
    "W": {"L": "S", "R": "N"},
    "S": {"L": "E", "R": "W"},
}

move = {
    "N": lambda coord, n: [(coord[0], coord[1] + c) for c in range(1, n + 1)],
    "E": lambda coord, n: [(coord[0] + c, coord[1]) for c in range(1, n + 1)],
    "W": lambda coord, n: [(coord[0] - c, coord[1]) for c in range(1, n + 1)],
    "S": lambda coord, n: [(coord[0], coord[1] - c) for c in range(1, n + 1)],
}


def part1():
    coord = [0, 0]
    direction = "N"
    for instruction in instructions:
        i, *n = list(instruction)
        n = int("".join(n))
        direction = turn[direction][i]
        coords = move[direction](coord, n)
        coord = coords[-1]
    return coord


coord = part1()
print("Part 1:", sum((abs(coord[0]), abs(coord[1]))))


def part2():
    coord = [0, 0]
    direction = "N"
    visited = set()
    for instruction in instructions:
        i, *n = list(instruction)
        n = int("".join(n))
        direction = turn[direction][i]
        coords = move[direction](coord, n)
        if visited.intersection(coords):
            return visited.intersection(coords).pop()
        visited.update(coords)
        coord = coords[-1]


coord = part2()
print("Part 2:", sum((abs(coord[0]), abs(coord[1]))))
