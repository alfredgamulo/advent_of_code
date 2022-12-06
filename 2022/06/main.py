import sys
from collections import deque


def detect(data, size):
    stream = deque(maxlen=size)
    for i, v in enumerate(data):
        stream.append(v)
        if len(set(stream)) == size:
            return i + 1
    return -1


if __name__ == "__main__":
    data = sys.stdin.read().strip()

    print("Part 1:", detect(data, 4))
    print("Part 2:", detect(data, 14))
