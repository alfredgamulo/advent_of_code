import sys


def part1(lines, rows, cols):
    visible = set()

    # row (left->right) down
    for r in range(rows):
        height = -1
        for c in range(cols):
            if int(lines[r][c]) > height:
                visible.add((r, c))
                height = int(lines[r][c])
    # row (right->left) down
    for r in range(rows):
        height = -1
        for c in range(cols - 1, -1, -1):
            if int(lines[r][c]) > height:
                visible.add((r, c))
                height = int(lines[r][c])
    # col (up->down) right
    for c in range(cols):
        height = -1
        for r in range(rows):
            if int(lines[r][c]) > height:
                visible.add((r, c))
                height = int(lines[r][c])
    # col (down->up) right
    for c in range(cols):
        height = -1
        for r in range(rows - 1, -1, -1):
            if int(lines[r][c]) > height:
                visible.add((r, c))
                height = int(lines[r][c])

    return len(visible)


def part2(lines, rows, cols):
    max_val = 0
    for x in range(rows):
        for y in range(cols):
            height = int(lines[x][y])
            up_value = 0
            for r in range(x - 1, -1, -1):
                if int(lines[r][y]) <= height:
                    up_value += 1
                if int(lines[r][y]) == height:
                    break
            down_value = 0
            for r in range(x + 1, rows):
                if int(lines[r][y]) <= height:
                    down_value += 1
                if int(lines[r][y]) == height:
                    break
            left_value = 0
            for c in range(y - 1, -1, -1):
                if int(lines[x][c]) <= height:
                    left_value += 1
                if int(lines[x][c]) == height:
                    break
            right_value = 0
            for c in range(y + 1, cols):
                if int(lines[x][c]) <= height:
                    right_value += 1
                if int(lines[x][c]) == height:
                    break
            value = left_value * right_value * up_value * down_value
            max_val = max(value, max_val)
    return max_val


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])
    print("Part 1:", part1(lines, rows, cols))
    print("Part 2:", part2(lines, rows, cols))
