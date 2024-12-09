import sys
from collections import deque
from pathlib import Path


def part1(lines):
    disk = deque()
    for i, c in enumerate(lines[0]):
        push = None
        if i % 2 == 0:
            push = int(i) // 2
        disk += [push] * int(c)
    new_disk = []
    while disk:
        push = disk.popleft()
        while push == None and disk:
            push = disk.pop()
        if push is not None:
            new_disk.append(push)
    disk = new_disk
    p1 = 0
    for i, d in enumerate(disk):
        p1 += i * d
    return p1


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", None)
