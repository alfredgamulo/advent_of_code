import sys
from collections import deque
from itertools import product


def solve(graph, start, end):
    graphcoords = set(product(range(len(graph)), range(len(graph[0]))))
    for (r, c) in graphcoords:
        if start == graph[r][c]:
            visited = set([(r, c)])
            moveque = deque([[(r, c)]])
            graph[r] = graph[r].replace("E", "z")
    while moveque:
        points = moveque.popleft()
        r, c = points[-1]
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = (r + i, c + j)
            if (x, y) in graphcoords and (x, y) not in visited:
                if graph[x][y] == end:
                    if graph[r][c] in ("b", "a"):
                        return len(points)
                else:
                    if ord(graph[r][c]) - ord(graph[x][y]) <= 1:
                        visited.add((x, y))
                        moveque.append(points[:] + [(x, y)])


if __name__ == "__main__":
    graph = sys.stdin.read().splitlines()

    print("Part 1:", solve(graph[:], "E", "S"))
    print("Part 2:", solve(graph[:], "E", "a"))
