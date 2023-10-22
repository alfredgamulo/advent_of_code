import os
import re
import sys
import time
from collections import defaultdict, deque

adjacency = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def biggest_island(grid):
    visited = set()
    stack = deque()
    island_size = defaultdict(int)
    for x, y in grid:
        stack.append((x, y, (x, y)))  # x, y, origin point

    while stack:
        x, y, origin = stack.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        island_size[origin] += 1
        for a, b in adjacency:
            if (x + a, y + b) not in visited and (x + a, y + b) in grid:
                stack.appendleft((x + a, y + b, origin))

    v = list(island_size.values())
    return max(v)


def min_x(points):
    return min(points, key=lambda x: x[0])[0]


def max_x(points):
    return max(points, key=lambda x: x[0])[0]


def min_y(points):
    return min(points, key=lambda x: x[1])[1]


def max_y(points):
    return max(points, key=lambda x: x[1])[1]


def solve(positions, velocities):
    counter = 0
    while True:
        counter += 1
        for i in range(len(positions)):
            positions[i] = (
                positions[i][0] + velocities[i][0],
                positions[i][1] + velocities[i][1],
            )
        points = set(positions)
        if biggest_island(points) > 8:
            os.system("cls" if os.name == "nt" else "printf '\033c'")
            for y in range(min_y(points), max_y(points) + 1):
                for x in range(min_x(points), max_x(points) + 1):
                    if (x, y) in points:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print("", flush=True)
            print("time: ", counter, flush=True)
            time.sleep(3)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    positions, velocities = [], []
    for line in lines:
        p1, p2, v1, v2 = list(map(int, re.findall(r"[-]?\d+", line)))
        positions.append((p1, p2))
        velocities.append((v1, v2))

    solve(positions, velocities)
