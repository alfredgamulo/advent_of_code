import sys
from math import ceil, sqrt

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""

# https://math.stackexchange.com/questions/163080/on-a-two-dimensional-grid-is-there-a-formula-i-can-use-to-spiral-coordinates-in
# ulam spiral coordinates


def spiral(n):
    k = ceil((sqrt(n) - 1) / 2)
    t = 2 * k + 1
    m = t**2
    t = t - 1
    if n >= m - t:
        return k - (m - n), -k
    else:
        m = m - t
    if n >= m - t:
        return -k, -k + (m - n)
    else:
        m = m - t
    if n >= m - t:
        return -k + (m - n), k
    else:
        return k, k - (m - n - t)


def part1(number):
    coord = spiral(number)
    return abs(coord[0]) + abs(coord[1])


def part2(number):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    matrix = {}
    matrix[(0, 0)] = 1

    i = 1
    while True:
        i += 1
        a, b = spiral(i)
        value = 0
        for x, y in neighbors:
            value += matrix.get((a + x, b + y), 0)
        matrix[(a, b)] = value
        if value > number:
            return value


if __name__ == "__main__":
    number = int(sys.stdin.readline())

    print("Part 1:", part1(number))
    print("Part 2:", part2(number))
