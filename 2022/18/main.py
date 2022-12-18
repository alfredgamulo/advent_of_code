import sys

adj = set([(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)])


def part1(coords):
    return sum(tuple(map(sum, zip(c, a))) not in coords for c in coords for a in adj)


def part2(coords):
    surfaces = set()
    for c in coords:
        for a in adj:
            n = tuple(map(sum, zip(c, a)))
            if n not in coords:
                surfaces.add(n)

    bubbles = 0

    return len(surfaces) - bubbles


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    coords = set([tuple(map(int, line.split(","))) for line in lines])
    print("Part 1:", part1(coords))
    print("Part 2:", part2(coords))
