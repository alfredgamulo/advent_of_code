import sys
from collections import deque

diagram = {}


def part1(lines):
    global diagram
    for line in lines:
        left, right = map(str.strip, line.split("<->"))
        diagram[int(left)] = list(map(int, right.split(",")))
    target = 0
    targets = deque([target])
    visited = {target}
    while targets:
        t = targets.popleft()
        visited.add(t)
        for r in diagram[t]:
            if r not in visited:
                targets.append(r)
    return len(visited)


def part2():
    group_tracker = set()
    group_count = 0
    for k in diagram.keys():
        targets = deque([k])
        visited = {k}
        while targets:
            t = targets.popleft()
            visited.add(t)
            for r in diagram[t]:
                if r not in visited:
                    targets.append(r)
        if group_tracker.isdisjoint(visited):
            group_tracker = group_tracker.union(visited)
            group_count += 1
    return group_count


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
