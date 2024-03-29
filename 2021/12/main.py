import sys
from collections import defaultdict, deque

edges = defaultdict(set)
for line in map(str.strip, sys.stdin.readlines()):
    (x, y) = line.split("-")
    edges[x].add(y)
    edges[y].add(x)


def recursion(path=["start"], limit=1):
    count = 0
    for n in edges[path[-1]]:
        if n == "start" or n.islower() and path.count(n) >= limit:
            continue
        if n == "end":
            count += 1
        else:
            count += recursion(
                path=path + [n],
                limit=1 if n.islower() and n in path else limit,
            )
    return count


print("recursion:")
print("Part 1:", recursion())
print("Part 2:", recursion(limit=2))


def no_recursion(limit=1):
    queue = deque([(["start"], limit)])
    count = 0
    while queue:
        (path, limit) = queue.popleft()
        for n in edges[path[-1]]:
            if n == "start" or n.islower() and path.count(n) >= limit:
                continue
            if n == "end":
                count += 1
            else:
                queue.append((path + [n], 1 if n.islower() and n in path else limit))
    return count


print("queue:")
print("Part 1:", no_recursion())
print("Part 2:", no_recursion(limit=2))
