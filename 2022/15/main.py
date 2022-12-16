import re
import sys
from collections import Counter


def parse(lines):
    beacons = []
    sensors = []
    dists = []
    for line in lines:
        sx, sy, bx, by = map(int, (re.findall("-*\\d+", line)))
        beacons.append((bx, by))
        sensors.append((sx, sy))
        dists.append(abs(sx - bx) + abs(sy - by))
    return beacons, sensors, dists


def part1(lines):
    beacons, sensors, dists = parse(lines)
    validate = 2000000  # magic number

    covered = []
    for (sx, sy), dist in zip(sensors, dists):
        if -dist + sy < validate < dist + sy:
            covered.append(
                (-dist + abs((sy - validate)) + sx, dist - abs((sy - validate)) + sx)
            )

    positions = set()
    for c in covered:
        positions.update(list(range(c[0], c[1] + 1)))

    for x, y in set(beacons):
        if y == validate:
            positions.remove(x)

    return len(positions)


def part2(lines):
    _, sensors, dists = parse(lines)
    tries = Counter()
    validate = 4000000  # magic number
    for (sx, sy), dist in zip(sensors, dists):
        dist += 1
        xmin = sx - (dist) if sx - (dist) >= 0 else 0
        xmax = sx + dist + 1 if sx + dist + 1 <= validate else validate
        for nx in range(xmin, xmax):
            ymin = abs(sx - nx) + sy - (dist)
            ymax = dist + sy - abs(sx - nx)
            for ny in (ymin, ymax):
                if (0 <= nx <= validate) and (0 <= ny <= validate):
                    tries.update([(nx, ny)])
    for t, _ in tries.most_common():
        found = False
        for (sx, sy), dist in zip(sensors, dists):
            if (abs(t[0] - sx) + abs(t[1] - sy)) <= dist:
                found = True
                break
        if not found:
            return t[0] * 4000000 + t[1]


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
