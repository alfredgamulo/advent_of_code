import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from fractions import Fraction
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from itertools import (
    batched,
    chain,
    combinations,
    count,
    groupby,
    permutations,
    product,
    zip_longest,
)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter

import numpy as np


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


def cross_product(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    )


def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


def find_normal_vector(trajectories):
    points = [
        (trajectory[0], trajectory[1], trajectory[2]) for trajectory in trajectories
    ]
    # Find a plane that intersects all trajectories
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                # Vector v1 and v2 on the plane formed by three non-collinear points
                v1 = (
                    points[j][0] - points[i][0],
                    points[j][1] - points[i][1],
                    points[j][2] - points[i][2],
                )
                v2 = (
                    points[k][0] - points[i][0],
                    points[k][1] - points[i][1],
                    points[k][2] - points[i][2],
                )

                # Calculate the normal vector using cross product
                normal = cross_product(v1, v2)

                # Check if the normal vector is non-zero
                if any(normal):
                    return normal


def part2():
    vector = find_normal_vector(stones)
    vec = np.array(vector)

    # Initialize an empty list to store the values of t
    t_values = []

    # Loop through each line in the array
    for line in stones:
        # Form the point A and the direction vector dir_vec
        A = np.array(line[:3])
        dir_vec = np.array(line[3:])

        # Calculate the value of t
        t = (vec - A) / dir_vec

        # Append the value of t to the list
        t_values.append(t)

    # Print the values of t
    for i, t in enumerate(t_values):
        print(f"For line {i+1}, t = {t}")


if __name__ == "__main__":
    stones = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        x, y, z, dx, dy, dz = map(int, re.findall("-?\\d+", line))
        stones.append([x, y, z, dx, dy, dz])
    if sys.argv[1] == "input":
        search = (200_000_000_000_000, 400_000_000_000_000)
    else:
        search = (7, 27)
    print(stones)
    print("Part 1:", part1())
    print("Part 2:", part2())
