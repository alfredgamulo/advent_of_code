import sys
from collections import deque

adj = set([(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)])


def part1(coords):
    return sum(tuple(map(sum, zip(c, a))) not in coords for c in coords for a in adj)


def part2(coords):
    max_x, max_y, max_z = 0, 0, 0
    for c in coords:
        max_x, max_y, max_z = (
            max(max_x, c[0] + 1),
            max(max_y, c[1] + 1),
            max(max_z, c[2] + 1),
        )

    stack = deque([(0, 0, 0)])
    visit = set()
    res = 0
    while stack:
        current = stack.popleft()
        for a in adj:
            if (p := tuple(map(sum, zip(current, a)))) in coords:
                res += 1
            elif (
                p not in visit
                and (-1 <= p[0] <= max_x)
                and (-1 <= p[1] <= max_y)
                and (-1 <= p[2] <= max_z)
            ):
                stack.append(p)
                visit.add(p)
    return res


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    coords = set([tuple(map(int, line.split(","))) for line in lines])
    print("Part 1:", part1(coords))
    print("Part 2:", part2(coords))
