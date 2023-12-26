import re
import sys
from itertools import combinations
from pathlib import Path

import z3


def slope_intercept(vector):  # return m and b
    x, y, _, dx, dy, _ = vector
    return dy / dx, -x * (dy / dx) + y


def intersection(m1, b1, m2, b2):
    if m1 == m2:
        return None, None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


def check(origin, velocity, intersect):
    return not (
        (velocity > 0 and intersect < origin) or (velocity < 0 and intersect > origin)
    )


def part1():
    total = 0
    for one, two in combinations(stones, 2):
        x, y = intersection(*slope_intercept(one), *slope_intercept(two))
        if not (x and y):
            continue
        if search[0] <= x <= search[1] and search[0] <= y <= search[1]:
            if all(
                check(o, v, i)
                for o, v, i in [
                    (one[0], one[3], x),
                    (one[1], one[4], y),
                    (two[0], two[3], x),
                    (two[1], two[4], y),
                ]
            ):
                total += 1
    return total


def part2():
    px, py, pz, vx, vy, vz = z3.Ints("px py pz vx vy vz")
    times = [z3.Int("t" + str(i)) for i in range(4)]
    solver = z3.Solver()
    for i, (x, y, z, dx, dy, dz) in enumerate(stones[:4]):
        solver.add(px + vx * times[i] == x + dx * times[i])
        solver.add(py + vy * times[i] == y + dy * times[i])
        solver.add(pz + vz * times[i] == z + dz * times[i])
    solver.check()
    answer = solver.model().evaluate(px + py + pz)
    return answer.as_long()


if __name__ == "__main__":
    stones = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        x, y, z, dx, dy, dz = map(int, re.findall("-?\\d+", line))
        stones.append([x, y, z, dx, dy, dz])
    if sys.argv[1] == "input":
        search = (200_000_000_000_000, 400_000_000_000_000)
    else:
        search = (7, 27)
    print("Part 1:", part1())
    print("Part 2:", part2())
