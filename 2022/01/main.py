import sys


def part1(inventory):
    most = 0
    for i in inventory:
        most = max(most, sum(i))
    return most


def part2(inventory):
    sorted_inventory = sorted((sum(i) for i in inventory), reverse=True)
    return sum(sorted_inventory[:3])


if __name__ == "__main__":
    inventory = sys.stdin.read().strip().split("\n\n")
    inventory = [list(map(int, i.split("\n"))) for i in inventory if i]

    print("Part 1:", part1(inventory))
    print("Part 2:", part2(inventory))
