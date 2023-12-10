import sys
from collections import deque
from contextlib import suppress
from pathlib import Path


def parse(graph):
    pipe, loop = set(), deque()
    for x, line in enumerate(graph):
        if (y := line.find("S")) >= 0:
            pipe.add((x, y))
            loop.append((x, y))
            with suppress(IndexError):
                l = (x, y - 1) if graph[x][y - 1] in ["-", "L", "F"] else None
                r = (x, y + 1) if graph[x][y + 1] in ["-", "J", "7"] else None
                u = (x - 1, y) if graph[x - 1][y] in ["|", "7", "F"] else None
                d = (x + 1, y) if graph[x + 1][y] in ["|", "L", "J"] else None
            loop.append(list(filter(None, [l, r, u, d]))[1])  # just need 1
            break

    neighbors = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
    }

    while (cursor := loop[-1]) not in pipe:
        pipe.add(cursor)
        lookup = [
            (cursor[0] + n[0], cursor[1] + n[1])
            for n in neighbors[graph[cursor[0]][cursor[1]]]
        ]
        loop.extend([l for l in lookup if l not in pipe])
    return loop


if __name__ == "__main__":
    loop = parse(Path(sys.argv[1]).read_text().splitlines())
    print("Part 1:", len(loop) // 2)
    area = 0.0
    for i in range(len(loop)):
        j = (i + 1) % len(loop)
        area += (loop[i][0] * loop[j][1]) - (loop[j][0] * loop[i][1])
    # shoelace area then inverse Pick's theorem
    interior = int((0.5 * abs(area)) - (len(loop) / 2) + 1)
    print("Part 2:", interior)
