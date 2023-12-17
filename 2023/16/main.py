import re
import sys
from collections import deque
from itertools import chain
from pathlib import Path


def parse(lines):
    mirrors = {}
    for x, line in enumerate(lines):
        for m in re.finditer("[^.]", line):
            mirrors[x, m.span()[0]] = m.group()
    return mirrors, len(lines), len(lines[0])


lookup = {
    "\\": lambda m: [(m[1], m[0])],
    "/": lambda m: [(-m[1], -m[0])],
    "-": lambda m: [m] if m[1] else [(0, -1), (0, 1)],
    "|": lambda m: [m] if m[0] else [(-1, 0), (1, 0)],
}


def solve(start=((0, 0), (0, 1))):
    beams = deque((start,))
    visit = set()
    while beams and (beam := beams.popleft()) and (pos := beam[0]) and (mov := beam[1]):
        if not ((0 <= pos[0] < max_x) and (0 <= pos[1] < max_y)) or beam in visit:
            continue
        visit.add(beam)
        if pos in mirrors and (new_movs := lookup[mirrors[pos]](mov)):
            beams.extend([(tuple(sum(x) for x in zip(pos, nm)), nm) for nm in new_movs])
        else:
            beams.append((tuple(sum(x) for x in zip(pos, mov)), mov))
    return len({pos for pos, _ in visit})


def part2():
    return max(
        chain(
            *chain(
                [solve(((x, 0), (0, 1))), solve(((x, max_y - 1), (0, -1)))]
                for x in range(max_x)
            ),
            *chain(
                [solve(((0, y), (1, 0))), solve(((max_x - 1, y), (-1, 0)))]
                for y in range(max_y)
            ),
        )
    )


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    mirrors, max_x, max_y = parse(lines)
    print("Part 1:", solve())
    print("Part 2:", part2())
