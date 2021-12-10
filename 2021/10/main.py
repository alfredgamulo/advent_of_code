import sys
from collections import deque

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}
syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}

part1 = 0
part2 = []
for line in map(str.strip, sys.stdin.readlines()):
    d = deque()
    for c in line:
        if chunks.get(c):
            d.append(c)
        elif c != chunks[d.pop()]:
            part1 += syntax_points[c]
            break
    else:
        score = 0
        while d:
            if chunks.get(x := d.pop()):
                score = score * 5 + autocomplete_points[chunks[x]]
            else:
                d.pop()
        part2.append(score)

print("Part 1:", part1)
print("Part 2:", sorted(part2)[len(part2) // 2])
