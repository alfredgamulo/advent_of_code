import hashlib
import sys
from collections import deque


def branch(dir, coord):
    opens = ["b", "c", "d", "e", "f"]
    up, down, left, right = hashlib.md5((line + dir).encode()).hexdigest()[:4]
    ret = []
    if up in opens and coord[0] - 1 >= 0:
        ret.append(((dir + "U"), sum_coords([coord, [-1, 0]])))
    if down in opens and coord[0] + 1 <= 3:
        ret.append(((dir + "D"), sum_coords([coord, [1, 0]])))
    if left in opens and coord[1] - 1 >= 0:
        ret.append(((dir + "L"), sum_coords([coord, [0, -1]])))
    if right in opens and coord[1] + 1 <= 3:
        ret.append(((dir + "R"), sum_coords([coord, [0, 1]])))
    return ret


def sum_coords(coords):
    return [sum(i) for i in zip(*coords)]


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    opt = deque()
    opt.append(("", [0, 0]))
    founds = []
    while opt:
        dir, coord = opt.popleft()
        if coord == [3, 3]:
            founds.append(dir)
        else:
            opt.extend(branch(dir, coord))
    print("Part 1:", sorted(founds, key=len)[0])
    print("Part 2:", len(sorted(founds, key=len)[-1]))
