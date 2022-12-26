import sys

next_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left


def part1(infected, position):
    direction = 0  # starts up
    count = 0
    for _ in range(10000):
        if position in infected:
            direction = (direction + 1) % 4
            infected.remove(position)
        else:
            direction = (direction - 1) % 4
            infected.add(position)
            count += 1
        position = tuple(map(sum, zip(position, next_move[direction])))
    return count


def part2(infected, position):
    weakend, flagged = set(), set()
    direction = 0  # starts up
    count = 0
    for _ in range(10000000):
        if position in infected:
            direction = (direction + 1) % 4
            infected.remove(position)
            flagged.add(position)
        elif position in flagged:
            direction = (direction + 2) % 4
            flagged.remove(position)
        elif position in weakend:
            weakend.remove(position)
            infected.add(position)
            count += 1
        else:
            direction = (direction - 1) % 4
            weakend.add(position)
        position = tuple(map(sum, zip(position, next_move[direction])))

    return count


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    mid = len(lines) // 2, len(lines[0]) // 2
    infected = set()
    for r, line in enumerate(lines):
        for c, node in enumerate(line):
            if node == "#":
                infected.add((r, c))

    print("Part 1:", part1(infected.copy(), mid))
    print("Part 2:", part2(infected.copy(), mid))
