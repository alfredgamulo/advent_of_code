import sys
from collections import deque
from itertools import product


def find_targets(graph):
    S = None
    E = None
    for x, y in product(range(len(graph)), range(len(graph[0]))):
        if not S and graph[x][y] == "S":
            S = (x, y)
        if not E and graph[x][y] == "E":
            E = (x, y)
        if S and E:
            return S, E


def get_val(graph, tup):
    return graph[tup[0]][tup[1]]


def part1(graph):
    S, E = find_targets(graph)
    graphcoords = set(product(range(len(graph)), range(len(graph[0]))))
    adjacencies = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set([S])
    moveque = deque([[S]])
    while moveque:
        points = moveque.popleft()
        for a in adjacencies:
            new = (points[-1][0] + a[0], points[-1][1] + a[1])
            if new in graphcoords and new not in visited:
                if get_val(graph, new) == "E":
                    if get_val(graph, points[-1]) == "z":
                        return len(points)
                else:
                    if (
                        ord(get_val(graph, new)) - ord(get_val(graph, points[-1])) <= 1
                        or get_val(graph, points[-1]) == "S"
                    ):
                        visited.add(new)
                        moveque.append(points[:] + [new])


def part2():
    pass


if __name__ == "__main__":
    graph = sys.stdin.read().splitlines()

    print("Part 1:", part1(graph))
    print("Part 2:", part2())
