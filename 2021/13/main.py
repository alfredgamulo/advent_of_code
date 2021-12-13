import sys
from collections import defaultdict
import pprint

manual = sys.stdin.read().split("\n\n")
dots = {(int(m.split(',')[0]),int(m.split(',')[1])) for m in manual[0].split()}
fold = [f.split()[2] for f in manual[1].strip().split('\n')]

for i,f in enumerate(fold):
    pos, coord = f.split("=")
    pos = ["x", "y"].index(pos)
    new_dots = set()
    for dot in dots:
        new_dot = list(dot)
        new_dot[pos] = int(coord) - abs(int(coord) - dot[pos])
        new_dots.add(tuple(new_dot))
    dots = new_dots
    
    if i == 0:
        print("Part 1:", len(dots))

print("Part 2:")

paper = defaultdict(list)
for i in range(6):
    paper[i] = [" "]*50
for i, dot in enumerate(dots):
    paper[dot[1]][dot[0]] = "#"
for p in paper.values():
    print("".join(p))
