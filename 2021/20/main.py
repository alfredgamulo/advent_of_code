import sys

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
            image.add((i, j))

for s in range(1, 3):
    output = set()
    for i in range(0 - s, lenx + s):
        for j in range(0 - s, leny + s):
            b = 0
            for e in range(len(bit_lookup)):
                x, y = i + bit_lookup[e][0], j + bit_lookup[e][1]
                if (x, y) in image:
                    b += 1 << e
            if algorithm[b] == "#":
                output.add((i, j))
    image = output

print(len(image))
