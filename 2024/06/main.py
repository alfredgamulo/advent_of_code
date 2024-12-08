import sys
from pathlib import Path

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def part1(lines, location, obstacles):
    visited = set()
    direction = dirs[0]
    while 0 <= location[0] < len(lines) and 0 <= location[1] < len(lines):
        visited.add(location)
        nxt = location[0] + direction[0], location[1] + direction[1]
        if nxt not in obstacles:
            location = nxt
        else:
            direction = dirs[(dirs.index(direction) + 1) % 4]
    return visited


def part2(lines, location, obstacles, options):
    ans = 0
    start = location
    for option in options:
        location = start
        current_obstacles = obstacles.copy()
        current_obstacles.add(option)
        visited = set()
        direction = dirs[0]
        loop = set()
        while 0 <= location[0] < len(lines) and 0 <= location[1] < len(lines):
            visited.add(location)
            loop.add((location, direction))
            nxt = location[0] + direction[0], location[1] + direction[1]
            if nxt not in current_obstacles:
                location = nxt
            else:
                direction = dirs[(dirs.index(direction) + 1) % 4]
            if (location, direction) in loop:
                ans += 1
                break
        continue
    return ans


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    location = None
    obstacles = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                location = (x, y)
            if c == "#":
                obstacles.add((x, y))
    visited = part1(lines, location, obstacles)
    print("Part 1:", len(visited))
    options = visited
    options.discard(location)
    print("Part 2:", part2(lines, location, obstacles, options))
