import sys

lines = sys.stdin.readlines()


def move(position, step):
    return tuple(map(sum, zip(position, step)))


position = (0, 0)
for line in lines:
    instruction, number = line.split()
    operate = {
        "up": lambda n: move(position, (0, -n)),
        "down": lambda n: move(position, (0, n)),
        "forward": lambda n: move(position, (n, 0)),
    }
    position = operate[instruction](int(number))

print("Part 1:", position[0] * position[1])

position = (0, 0, 0)
for line in lines:
    instruction, number = line.split()
    operate = {
        "up": lambda n: move(position, (0, 0, -n)),
        "down": lambda n: move(position, (0, 0, n)),
        "forward": lambda n: (
            position[0] + n,
            position[1] + n * position[2],
            position[2],
        ),
    }
    position = operate[instruction](int(number))

print("Part 2:", position[0] * position[1])
