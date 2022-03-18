import sys


def is_wall(x, y, fav):
    num = (x*x + 3*x + 2*x*y + y + y*y)+ fav
    return sum(map(int,format(num, "b"))) & 1 == 1

def part1(fav):
    walls = set()
    for y in range(50):
        for x in range(50):
            if x == 31 and y == 39:
                print("X", end="")
                continue
            if is_wall(x, y, fav):
                walls.add((x,y))
                print("▓", end="")
            else:
                print(".", end="")
        print()


def part2():
    pass


if __name__ == "__main__":
    fav = int(sys.stdin.readline())

    print("Part 1:", part1(fav))
    print("Part 2:", part2())
