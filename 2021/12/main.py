import sys
from collections import defaultdict

edges = defaultdict(list)
for line in map(str.strip, sys.stdin.readlines()):
    (x, y) = line.split("-")
    edges[x].append(y)
    edges[y].append(x)


def find_paths(paths=[], path=[], start="start", limit=1):
    count = 0
    for n in edges[start]:
        if n == "start" or n.islower() and path.count(n) >= limit:
            continue
        if n == "end":
            count += 1
        else:
            count += find_paths(
                paths=paths,
                path=path + [n],
                start=n,
                limit=1 if n.islower() and n in path else limit,
            )
    return count


print("Part 1:", find_paths(paths=[], path=["start"]))
print("Part 2:", find_paths(paths=[], path=["start"], limit=2))
