import sys


def solve(line, rows):
    safe_tiles = 0
    for _ in range(rows):
        safe_tiles += sum("." == t for t in line)
        newline = (line[:2] == "^^" or line[:2] == ".^") and "^" or "."
        for x, y, z in zip(line, line[1:], line[2:]):
            if x == y != z or x != y == z:
                newline += "^"
            else:
                newline += "."
        newline += (line[-2:] == "^^" or line[-2:] == "^.") and "^" or "."
        line = newline
    return safe_tiles


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    print("Part 1:", solve(line, 40))
    print("Part 2:", solve(line, 400000))
