import sys

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    x = y = 0
    max_distance = 0
    for direction in lines[0].strip().split(","):
        match direction:
            case ("n"):
                y += 1
            case ("ne"):
                x += 1
            case ("se"):
                y -= 1
                x += 1
            case ("s"):
                y -= 1
            case ("sw"):
                y -= 1
            case ("nw"):
                y += 1
                x -= 1
        max_distance = max(max_distance, abs(x + y))
    print("Part 1:", abs(x + y))
    print("Part 2:", max_distance)
