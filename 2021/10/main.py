import sys
from collections import deque

openers = ("(", "[", "{", "<")
matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}

part1 = 0
part2 = []
for line in map(str.strip, sys.stdin.readlines()):
    d = deque()
    for c in line:
        if c in openers:
            d.append(c)
        elif c != matches[d.pop()]:
            part1 += syntax_points[c]
            break
    else:
        score = 0
        while d:
            if (x := d.pop()) in openers:
                score = score * 5 + autocomplete_points[matches[x]]
            else:
                d.pop()
        part2.append(score)

print("Part 1:", part1)
print("Part 2:", sorted(part2)[len(part2) // 2])
