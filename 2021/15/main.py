import sys
from collections import deque, defaultdict

cave = []
for line in map(str.strip, sys.stdin.readlines()):
    cave.append(list(map(int, list(line))))


def solve(cave):
    li = len(cave)
    lj = len(cave[0])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dijkstra = defaultdict(tuple)  # coord -> (risk, previous)
    visited = set()
    start = (0, 0)
    dijkstra[start] = (0, None)
    dq = deque([start])
    while dq:
        pos = dq.popleft()
        pos_neighbors = [
            (pos[0] + i, pos[1] + j)
            for i, j in neighbors
            if ((pos[0] + i in range(li)) and (pos[1] + j in range(lj)))
        ]
        for n in pos_neighbors:
            if dijkstra.get(n):
                if dijkstra[n][0] > dijkstra[pos][0] + cave[n[0]][n[1]]:
                    dijkstra[n] = (dijkstra[pos][0] + cave[n[0]][n[1]], pos)
                    dq.append(n)
            elif n not in visited:
                visited.add(n)
                dijkstra[n] = (dijkstra[pos][0] + cave[n[0]][n[1]], pos)
                dq.append(n)
    return dijkstra[(li - 1, lj - 1)][0]


print("Part 1:", solve(cave))

bcave = []
for line in cave:
    bigline = line[:]
    for m in range(4):
        bigline.extend([(l + m) % 9 + 1 for l in line])
    bcave.append(bigline)

for _ in range(4):
    for i in range(len(cave)):
        bcave.append(
            [(l + 1) % 10 if l < 9 else 1 for l in bcave[len(bcave) - len(cave)]]
        )


print("Part 2:", solve(bcave))
