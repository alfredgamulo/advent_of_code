import sys
from itertools import product

# 5179
algorithm, image_string = sys.stdin.read().split("\n\n")
image_string = [list(s) for s in image_string.strip().split()]
lenx = len(image_string)
leny = len(image_string[0])

bit_lookup = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, 0),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]

image = set()
for i in range(len(image_string)):
    for j in range(len(image_string[i])):
        if image_string[i][j] == "#":
            image.add((i + 1, j + 1))

toggle = -1
for _ in range(2):
    output = set()
    lenx += 2
    leny += 2
    for i, j in product(range(0, lenx), range(0, leny)):
        b = 0
        for e in range(len(bit_lookup)):
            x, y = i + bit_lookup[e][0], j + bit_lookup[e][1]
            if (x, y) in image or (
                algorithm[0] == "#"
                and (toggle:= ~toggle)
                and (x <= 0 or x >= lenx  or y <= 0 or y >= leny)
            ):
                b += 1 << e
        if algorithm[b] == "#":
            output.add((i + 1, j + 1))
    image = output

print("Part 1:", len(image))
