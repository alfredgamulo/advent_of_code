import sys
from collections import deque
from math import ceil, floor


def part1(line):
    elfs = list(range(1, int(line) + 1))
    while len(elfs) > 1:
        skip = False
        nelfs = deque()
        for e in elfs:
            if not skip:
                nelfs.append(e)
            skip = not skip
        if len(elfs) & 1 == 1:
            nelfs.popleft()
        elfs = nelfs

    return elfs


def part2(line):
    elfs = dict.fromkeys(range(1, int(line) + 1))
    pointer = 1
    while len(elfs) > 1:
        lelfs = list(elfs)
        index = lelfs.index(pointer)
        try:
            half = floor(len(lelfs)/2)
            del elfs[lelfs[index + half]]
        except:
            half = ceil(len(lelfs)/2)
            del elfs[lelfs[index - half]]
        try:
            pointer = lelfs[index+1]
        except:
            pointer = list(elfs.keys())[0]
    return elfs

if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    print("Part 1:", part1(line))
    print("Part 2:", part2(line))
