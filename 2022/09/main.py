import sys


def follow(H, T):
    dx = H[0] - T[0]
    dy = H[1] - T[1]
    if abs(dx) >= 2 or abs(dy) >= 2:
        return (T[0] + sign(dx), T[1] + sign(dy))
    return T


def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1


def solve(lines, knots):
    rope = [(0, 0)] * knots
    visited = set()
    lookup = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    for line in lines:
        direction, distance = line.split()
        distance = int(distance)
        for _ in range(distance):
            rope[0] = tuple(map(lambda i, j: i + j, rope[0], lookup[direction]))
            for i in range(1, len(rope)):
                rope[i] = follow(rope[i - 1], rope[i])
            visited.add(rope[-1])

    return len(visited)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", solve(lines, 2))
    print("Part 2:", solve(lines, 10))
