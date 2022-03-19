import hashlib
import re
import sys
from collections import deque


def part1(data):
    dq = deque()
    for num in range(1001):
        md5 = hashlib.md5((data + str(num)).encode()).hexdigest()
        dq.append(md5)

    regex = "([a-z\\d])\\1\\1"
    p = re.compile(regex)

    index = 0
    count = 0
    while True:
        check = dq.popleft()
        if match := re.search(p, check):
            g = match.group()[0]
            validate = f"{g}{g}{g}{g}{g}"
            v = re.compile(validate)
            for d in dq:
                if re.search(v, d):
                    count += 1
                    break
        dq.append(hashlib.md5((data + str(num := num + 1)).encode()).hexdigest())
        if count >= 64:
            break
        index += 1
    return index


def stretch(hash):
    for _ in range(2016):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash


def part2(data):
    dq = deque()
    for num in range(1001):
        md5 = hashlib.md5((data + str(num)).encode()).hexdigest()
        md5 = stretch(md5)
        dq.append(md5)

    regex = "([a-z\\d])\\1\\1"
    p = re.compile(regex)

    index = 0
    count = 0
    while True:
        check = dq.popleft()
        if match := re.search(p, check):
            g = match.group()[0]
            validate = f"{g}{g}{g}{g}{g}"
            v = re.compile(validate)
            for d in dq:
                if re.search(v, d):
                    count += 1
                    break
        dq.append(stretch(hashlib.md5((data + str(num := num + 1)).encode()).hexdigest()))
        if count >= 64:
            break
        index += 1
    return index


if __name__ == "__main__":
    data = sys.stdin.readline().strip()

    # print("Part 1:", part1(data))
    print("Part 2:", part2(data))
