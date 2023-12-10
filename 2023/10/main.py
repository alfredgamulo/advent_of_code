import copy
import os
import re
import string
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from io import StringIO
from itertools import permutations  # noqa
from itertools import batched, chain, combinations, count, cycle, product, zip_longest
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path


def parse(graph):
    pipe = {}
    loop = deque()
    for x, line in enumerate(graph):
        if (y := line.find("S")) >= 0:
            pipe[(x, y)] = "S"
            loop.append((x,y))
            with suppress(IndexError):
                l = (x, y - 1) if graph[x][y - 1] in ["-", "L", "F"] else None
                r = (x, y + 1) if graph[x][y + 1] in ["-", "J", "7"] else None
                u = (x - 1, y) if graph[x - 1][y] in ["|", "7", "F"] else None
                d = (x + 1, y) if graph[x + 1][y] in ["|", "L", "J"] else None
            loop.append(list(filter(None, [l, r, u, d]))[0]) # just need 1
            break

    neighbors = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
    }

    while (cursor:=loop[-1]) not in pipe:
        pipe[cursor] = graph[cursor[0]][cursor[1]]
        lookup = [
            (cursor[0] + n[0], cursor[1] + n[1])
            for n in neighbors[graph[cursor[0]][cursor[1]]]
        ]
        loop.extend([l for l in lookup if l not in pipe])
    return pipe, loop


if __name__ == "__main__":
    graph = Path(sys.argv[1]).read_text().splitlines()
    pipe,loop = parse(graph)

    print("Part 1:", len(pipe) // 2)
    print(len(loop))
    # for x in range(len(graph)):
    #     for y in range(len(graph[0])):
    #         if pipe:=pipes.get((x,y)):
    #             print(pipe, end="")
    #         else:
    #             print(".", end="")
    #     print("\n")
    # print("Part 2:", part2())
