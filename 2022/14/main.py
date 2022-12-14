import sys
from itertools import count, product


def get_cave(lines):
    formation = set()
    lowest_pt = 0
    for line in lines:
        shape = [eval(coord) for coord in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(shape, shape[1:]):
            xs = list(range(min(x1, x2), max(x1, x2) + 1))
            ys = list(range(min(y1, y2), max(y1, y2) + 1))
            for x, y in product(xs, ys):
                formation.add((x, y))
                lowest_pt = max(lowest_pt, y)
    return formation, lowest_pt


def part1(lines):
    formation, lowest_pt = get_cave(lines)
    start, down, left, right = (500, 0), (0, 1), (-1, 1), (1, 1)
    for c in count():
        sand = start
        blocked = False
        while not blocked:
            while (newsand := tuple(map(sum, zip(sand, down)))) not in formation:
                sand = newsand
                if sand[1] > lowest_pt:
                    return c
            blocked = True
            if (newsand := tuple(map(sum, zip(sand, left)))) not in formation:
                sand = newsand
                blocked = False
            elif (newsand := tuple(map(sum, zip(sand, right)))) not in formation:
                sand = newsand
                blocked = False
        formation.add(sand)


def part2(lines):
    formation, lowest_pt = get_cave(lines)
    start, down, left, right = (500, 0), (0, 1), (-1, 1), (1, 1)
    for c in count():
        sand = start
        blocked = False
        while not blocked:
            while (newsand := tuple(map(sum, zip(sand, down)))) not in formation:
                sand = newsand
                if sand[1] > lowest_pt:
                    break
            if sand[1] > lowest_pt:
                break
            blocked = True
            if (newsand := tuple(map(sum, zip(sand, left)))) not in formation:
                sand = newsand
                blocked = False
            elif (newsand := tuple(map(sum, zip(sand, right)))) not in formation:
                sand = newsand
                blocked = False
            if sand[1] > lowest_pt:
                break
        if sand == start:
            return c + 1
        formation.add(sand)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
