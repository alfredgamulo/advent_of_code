import sys
from itertools import product

# sample -> 1656

matrix = []
for line in map(str.strip, sys.stdin.readlines()):
    matrix.append(list(map(int, list(line))))
li = len(matrix)
lj = len(matrix[0])

# print(matrix)
ns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_flashes(m):
    flashes = 0
    for i, j in product(range(li), range(lj)):
        if m[i][j] > 9:
            m[i][j] = 0
            for n in ns:
                x = i + n[0]
                y = j + n[1]
                if x in range(li) and y in range(lj) and matrix[x][y] > 0:
                    matrix[x][y] += 1
            flashes += 1 + count_flashes(m)
    return flashes


part1 = 0
for step in range(100):
    for i, j in product(range(li), range(lj)):
        matrix[i][j] += 1
    while f := count_flashes(matrix):
        part1 += f

print("Part 1:", part1)

part2 = 0
flashes = 0

while flashes != (li)*(lj):
    for i, j in product(range(li), range(lj)):
        matrix[i][j] += 1
    while f := count_flashes(matrix):
        part2 += 1
        flashes = f
    print(part2)
print((li)*(lj))
print("Part 2:",part2)