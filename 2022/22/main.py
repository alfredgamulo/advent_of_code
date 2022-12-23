import re
import sys

facing_value = {"R": 0, "D": 1, "L": 2, "U": 3}
facing_moves = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
facing_order = list(facing_moves.keys())


def step_generator(dirs):
    for r in re.findall(r"\w\d+", dirs):
        yield r


def cube_wrap(i, j, d):
    if d == "R" and i == 151:  # 1-R
        return 100, 151 - j, "L"
    elif d == "D" and j == 51:  # 1-D
        return 100, 50 + (i - 100), "L"
    elif d == "U" and j == 0 and i > 100:  # 1-U
        return i - 100, 200, "U"
    elif d == "U" and j == 0 and 51 <= i <= 100:  # 2-U
        return 1, 150 + (i - 50), "R"
    elif d == "L" and i == 50 and j < 51:  # 2-L
        return 1, 151 - j, "R"
    elif d == "L" and i == 50 and 51 <= j <= 100:  # 3-L
        return j - 50, 101, "D"
    elif d == "R" and i == 101 and 51 <= j <= 100:  # 3-R
        return 100 + (j - 50), 50, "U"
    elif d == "R" and i == 101 and 101 <= j <= 150:  # 4-R
        return 150, 151 - j, "L"
    elif d == "D" and j == 151:  # 4-D
        return 50, 150 + (i - 50), "L"
    elif d == "L" and i == 0 and 101 <= j <= 150:  # 5-L
        return 51, 151 - j, "R"
    elif d == "U" and j == 100:  # 5-U
        return 51, 50 + i, "R"
    elif d == "L" and i == 0 and j >= 151:  # 6-L
        return 50 + (j - 150), 1, "D"
    elif d == "R" and i == 51:  # 6-R
        return 50 + (j - 150), 150, "U"
    elif d == "D" and j == 201:  # 6-D
        return i + 100, 1, "D"
    else:
        print("Something broke!", i, j, d)


def solve(sections, cube=False):
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
                if not cube:
                    ndir = dir
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
                else:
                    i, j, ndir = cube_wrap(n[1] + 1, n[0] + 1, dir)
                    m = (j - 1, i - 1)
                if m in solid_walls:
                    break
                else:
                    pos = m
                    dir = ndir

    return (1000 * (pos[0] + 1)) + (4 * (pos[1] + 1)) + facing_value[dir]


if __name__ == "__main__":
    sections = sys.stdin.read().split("\n\n")

    print("Part 1:", solve(sections))
    print("Part 2:", solve(sections, True))
