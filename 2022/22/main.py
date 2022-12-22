import re
import sys

facing_value = {"R": 0, "D": 1, "L": 2, "U": 3}
facing_moves = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
facing_order = list(facing_moves.keys())


def step_generator(dirs):
    for r in re.findall(r"\w\d+", dirs):
        yield r


def part1(open_tiles, solid_walls, steps, start, max_x, max_y):
    pos, dir = start, "U"
    for s in steps:
        next_dir = 1 if s[0] == "R" else -1
        dir = facing_order[(facing_order.index(dir) + next_dir) % len(facing_order)]
        for _ in range(int(s[1:])):
            n = tuple(map(sum, zip(pos, facing_moves[dir])))
            if n in open_tiles:
                pos = n
            elif n in solid_walls:
                break
            else:
                if dir == "U":
                    m = (max_x, pos[1])
                elif dir == "D":
                    m = (0, pos[1])
                elif dir == "L":
                    m = (pos[0], max_y)
                else:  # dir == "R":
                    m = (pos[0], 0)

                while m not in (open_tiles.union(solid_walls)):
                    m = tuple(map(sum, zip(m, facing_moves[dir])))
                if m in solid_walls:
                    break
                else:
                    pos = m

    return (1000 * (pos[0] + 1)) + (4 * (pos[1] + 1)) + facing_value[dir]


def part2():
    pass


if __name__ == "__main__":
    sections = sys.stdin.read().split("\n\n")
    maze = sections[0].splitlines()
    dirs = sections[1]

    start, max_x, max_y = None, len(maze) - 1, 0
    open_tiles, solid_walls = set(), set()
    for x, m in enumerate(maze):
        for y, c in enumerate(m):
            max_y = max(y, max_y)
            match c:
                case (" "):
                    ...
                case ("."):
                    if not start:
                        start = (x, y)
                    open_tiles.add((x, y))
                case ("#"):
                    solid_walls.add((x, y))
            if not start and c != " ":
                start = (x, y)

    steps = step_generator("R" + dirs)

    print("Part 1:", part1(open_tiles, solid_walls, steps, start, max_x, max_y))
    print("Part 2:", part2())
