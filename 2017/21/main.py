import sys


def rotate2(s):
    return f"{s[1]}{s[4]}/{s[0]}{s[3]}"


def rotate3(s):
    return f"{s[2]}{s[6]}{s[10]}/{s[1]}{s[5]}{s[9]}/{s[0]}{s[4]}{s[8]}"


def mirror3(s):
    return f"{s[2]}{s[1]}{s[0]}/{s[6]}{s[5]}{s[4]}/{s[10]}{s[9]}{s[8]}"


def solve(rules, grid, interactions):
    for _ in range(interactions):
        next_grid = []
        if (len(grid) % 2) == 0:
            for i in range(len(grid) // 2):
                line1, line2, line3 = "", "", ""
                for j in range(len(grid) // 2):
                    lookup = f"{grid[i*2][j*2:(j+1)*2]}/{grid[i*2+1][j*2:(j+1)*2]}"
                    result = rules[lookup].split("/")
                    line1 += result[0]
                    line2 += result[1]
                    line3 += result[2]
                next_grid.append(line1)
                next_grid.append(line2)
                next_grid.append(line3)
            grid = next_grid
        else:
            for i in range(len(grid) // 3):
                line1, line2, line3, line4 = "", "", "", ""
                for j in range(len(grid) // 3):
                    lookup = f"{grid[i*3][j*3:(j+1)*3]}/{grid[i*3+1][j*3:(j+1)*3]}/{grid[i*3+2][j*3:(j+1)*3]}"
                    result = rules[lookup].split("/")
                    line1 += result[0]
                    line2 += result[1]
                    line3 += result[2]
                    line4 += result[3]
                next_grid.append(line1)
                next_grid.append(line2)
                next_grid.append(line3)
                next_grid.append(line4)
            grid = next_grid

    return sum([c == "#" for g in grid for c in g])


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    rules = {}
    for line in lines:
        before, after = line.split(" => ")
        if len(before) == 5:
            rules[before] = after
            b = rotate2(before)
            rules[b] = after
            b = rotate2(b)
            rules[b] = after
            b = rotate2(b)
            rules[b] = after
        else:
            rules[before] = after
            b = rotate3(before)
            rules[b] = after
            b = rotate3(b)
            rules[b] = after
            b = rotate3(b)
            rules[b] = after
            b = mirror3(b)
            rules[b] = after
            b = rotate3(b)
            rules[b] = after
            b = rotate3(b)
            rules[b] = after
            b = rotate3(b)
            rules[b] = after

    start = ".#./..#/###".split("/")
    print("Part 1:", solve(rules, start, 5))
    print("Part 2:", solve(rules, start, 18))
