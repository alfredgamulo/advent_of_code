import sys

lines = sys.stdin.readlines()


def move(position, step):
    return tuple(map(sum, zip(position, step)))


position = (0, 0)
for line in lines:
    instruction, number = line.split()
    number = int(number)
    if instruction == "up":
        position = move(position, (0, -number))
    if instruction == "down":
        position = move(position, (0, number))
    if instruction == "forward":
        position = move(position, (number, 0))

print("Part 1:", position[0] * position[1])

position = (0, 0, 0)
for line in lines:
    instruction, number = line.split()
    number = int(number)
    if instruction == "up":
        position = move(position, (0, 0, -number))
    if instruction == "down":
        position = move(position, (0, 0, number))
    if instruction == "forward":
        position = (
            position[0] + number,
            position[1] + number * position[2],
            position[2],
        )

print("Part 2:", position[0] * position[1])
