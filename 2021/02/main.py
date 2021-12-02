import sys

lines = sys.stdin.readlines()


def adjust(position, step):
    return tuple(map(sum, zip(position, step)))


def travel(position, operations):
    for line in lines:
        instruction, number = line.split()
        position = operations[instruction](position, int(number))
    return position[0] * position[1]


operations = {
    "up": lambda p, n: adjust(p, (0, -n)),
    "down": lambda p, n: adjust(p, (0, n)),
    "forward": lambda p, n: adjust(p, (n, 0)),
}
print("Part 1:", travel((0, 0), operations))

operations = {
    "up": lambda p, n: adjust(p, (0, 0, -n)),
    "down": lambda p, n: adjust(p, (0, 0, n)),
    "forward": lambda p, n: (
        p[0] + n,
        p[1] + n * p[2],
        p[2],
    ),
}
print("Part 2:", travel((0, 0, 0), operations))
