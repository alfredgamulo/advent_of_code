import sys
from collections import deque
from pathlib import Path

if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
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
    print("".join(map(str, disk)))
    p1 = 0
    for i, d in enumerate(disk):
        p1 += i * d

    print("Part 1:", p1)
    print("Part 2:", None)

# 6154086908998 too low
# 6154096669449
#
