import sys
from collections import deque


def solve(players, points):
    scores = [0] * players
    ring = deque([0])

    for marble in range(1, points + 1):
        if marble % 23:
            ring.rotate(-2)
            ring.appendleft(marble)
        else:
            ring.rotate(7)
            worth = marble
            second = ring.popleft()
            worth += second
            scores[marble % players] += worth

    return max(scores)


if __name__ == "__main__":
    players, *_, points, _ = sys.stdin.read().split(" ")
    players, points = int(players), int(points)

    print("Part 1:", solve(players, points))
    print("Part 2:", solve(players, points * 100))
