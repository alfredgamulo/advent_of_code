import sys
from itertools import count

firewall = {}


def part1(lines):
    global firewall
    for line in lines:
        left, right = map(int, line.split(": "))
        firewall[left] = right

    collisions = 0

    for i in range(max(firewall.keys()) + 1):
        if s := firewall.get(i):
            if i % ((s - 1) * 2) == 0:
                collisions += i * s
    return collisions


def part2():
    for delay in count(0):
        caught = False
        for i in range(max(firewall.keys()) + 1):
            if s := firewall.get(i):
                if (i + delay) % ((s - 1) * 2) == 0:
                    caught = True
        if not caught:
            return delay


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
