import sys
from collections import deque
from itertools import product

matrix = []
for line in map(str.strip, sys.stdin.readlines()):
    matrix.append(list(map(int, list(line))))
len_i = len(matrix)
len_j = len(matrix[0])

lows = {}
for i, j in product(range(len_i), range(len_j)):
    if i > 0 and matrix[i][j] >= matrix[i - 1][j]:
        continue
    if j > 0 and matrix[i][j] >= matrix[i][j - 1]:
        continue
    if i < len_i - 1 and matrix[i][j] >= matrix[i + 1][j]:
        continue
    if j < len_j - 1 and matrix[i][j] >= matrix[i][j + 1]:
        continue
    lows[(i, j)] = matrix[i][j]
print("Part 1:", sum(lows.values()) + len(lows.values()))

basins = []
for low in lows.keys():
    d = deque()
    d.append(low)
    v = {low}
    size = 0
    while d:
        i, j = d.popleft()
        if matrix[i][j] == 9:
            continue
        size += 1
        if i > 0 and (p := (i - 1, j)) not in v:
            v.add(p)
            d.append(p)
        if j > 0 and (p := (i, j - 1)) not in v:
            v.add(p)
            d.append(p)
        if i < len_i - 1 and (p := (i + 1, j)) not in v:
            v.add(p)
            d.append(p)
        if j < len_j - 1 and (p := (i, j + 1)) not in v:
            v.add(p)
            d.append(p)
    basins.append(size)
basins.sort()
print("Part 2:", basins[-1] * basins[-2] * basins[-3])
