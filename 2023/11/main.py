import sys
from itertools import combinations, product
from pathlib import Path


def solve(graph, expansion):
    xs, ys = set(range(len(graph))), set(range(len(graph[0])))
    galaxies = [
        (
            (x + (sum(x > dx for dx in xs) * (expansion - 1))),
            (y + (sum(y > dy for dy in ys) * (expansion - 1))),
        )
        for x, y in [
            (xs.discard(x) or x, ys.discard(y) or y)
            for x, y in product(range(len(graph)), range(len(graph[0])))
            if graph[x][y] == "#"
        ]
    ]
    return sum(abs(c - d) for a, b in combinations(galaxies, 2) for c, d in zip(a, b))


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print("Part 1:", solve(lines, 2))
    print("Part 2:", solve(lines, 1_000_000))
