import sys
from collections import deque
from itertools import product


def get_val(graph, tup):
    return graph[tup[0]][tup[1]]


def solve(graph, start, end):
    graphcoords = set(product(range(len(graph)), range(len(graph[0]))))
    for coords in graphcoords:
        if start == graph[coords[0]][coords[1]]:
            s = coords
    adjacencies = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set([s])
    moveque = deque([[s]])
    graph[s[0]] = graph[s[0]].replace("E", "z")
    while moveque:
        points = moveque.popleft()
        for a in adjacencies:
            new = (points[-1][0] + a[0], points[-1][1] + a[1])
            if new in graphcoords and new not in visited:
                if get_val(graph, new) == end:
                    if get_val(graph, points[-1]) in ("b", "a"):
                        return len(points)
                else:
                    if ord(get_val(graph, points[-1])) - ord(get_val(graph, new)) <= 1:
                        visited.add(new)
                        moveque.append(points[:] + [new])


if __name__ == "__main__":
    graph = sys.stdin.read().splitlines()

    print("Part 1:", solve(graph[:], "E", "S"))
    print("Part 2:", solve(graph[:], "E", "a"))
