import sys
from itertools import product

matrix = []
for line in map(str.strip, sys.stdin.readlines()):
    matrix.append(list(map(int, list(line))))
li = len(matrix)
lj = len(matrix[0])

ns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_flashes(m):
    flashes = 0
    for i, j in product(range(li), range(lj)):
        if m[i][j] <= 9:
            continue
        m[i][j] = 0
        for n in ns:
            x = i + n[0]
            y = j + n[1]
            if x in range(li) and y in range(lj) and m[x][y] > 0:
                m[x][y] += 1
        flashes += 1 + count_flashes(m)
    return flashes


f100 = 0
days = 0
flashes = 0
while flashes != li * lj:
    for i, j in product(range(li), range(lj)):
        matrix[i][j] += 1
    flashes = count_flashes(matrix)
    if days < 100:
        f100 += flashes
    days += 1

print("Part 1:", f100)
print("Part 2:", days)
