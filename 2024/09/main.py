import sys
from collections import deque
from pathlib import Path

if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    disk = deque()
    for i, c in enumerate(lines[0]):
        for _ in range(int(c)):
            push = "."
            if i % 2 == 0:
                push = int(i) // 2
            disk.append(push)
    for i in range(len(disk)):
        try:
            d = disk[i]
            if d != ".":
                continue
            popped = disk.pop()
            while popped == ".":
                popped = disk.pop()
            disk[i] = popped
        except IndexError:
            break
    print("".join(map(str, disk)))
    p1 = 0
    for i, d in enumerate(disk):
        p1 += i * d

    print("Part 1:", p1)
    print("Part 2:", None)

# 6154086908998 too low
