import sys
from itertools import product

instructions = list(map(str.strip, sys.stdin.readlines()))

x = 50
y = 6
on = set()

for i in instructions:
    on2 = set()
    match i.split():
        case ["rect", sq]:
            for i, j in product(
                range(int(sq.split("x")[0])), range(int(sq.split("x")[1]))
            ):
                on.add((i, j))
        case ["rotate", "row", coord, "by", dist]:
            coord = int(coord[2:])
            dist = int(dist)
            for c in range(x):
                if (c, coord) in on:
                    on2.add((((c + dist) % x), coord))
                    on.remove((c, coord))
        case ["rotate", "column", coord, "by", dist]:
            coord = int(coord[2:])
            dist = int(dist)
            for r in range(y):
                if (coord, r) in on:
                    on2.add(((coord, (r + dist) % y)))
                    on.remove((coord, r))
    on = on.union(on2)

print("Part 1:", len(on))
print("Part 2:")
for i in range(y):
    print()
    for j in range(x):
        if (j, i) in on:
            print("#", end="")
        else:
            print(" ", end="")
