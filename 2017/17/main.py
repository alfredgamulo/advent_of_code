import sys
from itertools import cycle, islice


def part1(steps):
    buffer = [0]
    for i in range(1, 2018):
        # funky circlular inserts
        buffer = list(islice(cycle(buffer), steps + i))[-i:] + [i]
    return buffer[0]


def part2(steps):
    buffer_len = 1
    index = 0
    target = None
    for c in range(1, 50000000):
        pointer = (index + steps) % buffer_len + 1
        buffer_len += 1
        if pointer == 1:
            target = c
        index = pointer
    return target


if __name__ == "__main__":
    steps = int(sys.stdin.readline())

    print("Part 1:", part1(steps))
    print("Part 2:", part2(steps))
