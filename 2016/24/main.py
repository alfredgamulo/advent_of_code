import math
import sys
from collections import deque
from itertools import combinations, permutations


# pairwise breadth first search
def bfs(passages, p1, p2):
    stack = deque()
    visited = set()
    stack.append((p1, 0))
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        pos, dist = stack.popleft()
        if pos == p2:
            return dist
        if pos in visited:
            continue
        visited.add(pos)
        for x, y in neighbors:
            if (pos[0] + x, pos[1] + y) in passages:
                stack.append(((pos[0] + x, pos[1] + y), dist + 1))


def solve(lines):
    passage = set()
    poi = dict()
    for row, line in enumerate(lines):
        for col, character in enumerate(line):
            if character != "#":
                passage.add((row, col))
                if character.isnumeric():
                    poi[int(character)] = (row, col)

    poi_distances = dict()
    for p1, p2 in combinations(poi.keys(), 2):
        distance = bfs(passage, poi[p1], poi[p2])
        poi_distances[(p1, p2)] = distance
        poi_distances[(p2, p1)] = distance

    part1 = math.inf
    part2 = math.inf
    for attempt in permutations(sorted(list(poi.keys()))[1:]):
        a = 0
        distance = 0
        for b in attempt:
            distance += poi_distances[(a, b)]
            a = b
        part1 = min(distance, part1)
        part2 = min(distance + poi_distances[(a, 0)], part2)
    print("Part 1:", part1)
    print("Part 0:", part2)


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    solve(lines)
