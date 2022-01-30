import sys

triangles = sys.stdin.readlines()


def part1():
    possible = []
    for triangle in triangles:
        sides = sorted(list(map(int, triangle.split())))
        if sides[0] + sides[1] > sides[2]:
            possible.append(sides)
    return len(possible)


print("Part 1:", part1())


def part2():
    possible = []
    index = 0
    while index + 3 <= len(triangles):
        group = triangles[index : index + 3]
        index += 3
        t = []
        for g in group:
            t.append(g.strip().split())
        for triangle in list(zip(*t)):
            sides = sorted(list(map(int, triangle)))
            if sides[0] + sides[1] > sides[2]:
                possible.append(sides)
    return len(possible)


print("Part 2:", part2())
