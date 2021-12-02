import sys

lines = sys.stdin.readlines()

position = (0, 0)

for line in lines:
    instruction, distance = line.split()
    distance = int(distance)
    if instruction == "forward":
        position = tuple(x + y for x, y in zip(position, (distance, 0)))
    if instruction == "down":
        position = tuple(x + y for x, y in zip(position, (0, distance)))
    if instruction == "up":
        position = tuple(x + y for x, y in zip(position, (0, -distance)))

print("Part 1:", position[0] * position[1])

position = (0, 0, 0)

for line in lines:
    instruction, distance = line.split()
    distance = int(distance)
    if instruction == "forward":
        position = (
            position[0] + distance,
            position[1] + (distance * position[2]),
            position[2],
        )
    if instruction == "down":
        position = tuple(x + y for x, y in zip(position, (0, 0, distance)))
    if instruction == "up":
        position = tuple(x + y for x, y in zip(position, (0, 0, -distance)))

print("Part 2:", position[0] * position[1])
