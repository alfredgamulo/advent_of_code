import sys

line = sys.stdin.readline().split(",")
x = int(line[1].split()[-1])
y = int(line[2].split()[1][:-1])


def locate(x, y):
    return (
        ((x - 1) * -~(x - 1) >> 1)
        + 1
        + ((x + y - 1) * -~(x + y - 1) >> 1)
        - ((x) * -~(x) >> 1)
    )


current = 20151125
for _ in range(1, locate(x, y)):
    current = current * 252533 % 33554393

print("Part 1:", current)
