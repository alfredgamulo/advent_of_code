import sys
from collections import defaultdict

line = sys.stdin.read().strip()

moves = {"^": (1, 0), "v": (-1, 0), ">": (0, 1), "<": (0, -1)}

houses = defaultdict(int)
position = (0, 0)
houses[position] = 1
for l in line:
    houses[(moves[l][0] + position[0], moves[l][1] + position[1])] += 1
    position = (moves[l][0] + position[0], moves[l][1] + position[1])

print("Part 1:", sum(h >= 1 for h in houses.values()))

houses = defaultdict(int)
position = (0, 0)
houses[position] = 2
for l in line[1::2]:
    houses[(moves[l][0] + position[0], moves[l][1] + position[1])] += 1
    position = (moves[l][0] + position[0], moves[l][1] + position[1])

position = (0, 0)
for l in line[::2]:
    houses[(moves[l][0] + position[0], moves[l][1] + position[1])] += 1
    position = (moves[l][0] + position[0], moves[l][1] + position[1])

print("Part 2:", sum(h >= 1 for h in houses.values()))
