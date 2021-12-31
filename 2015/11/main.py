import sys
from itertools import groupby


password = sys.stdin.read().strip()


def inc(line, index):
    c = ord(line[index]) + 1
    if c > ord("z"):
        line = inc(line, index - 1)
        c = ord("a")
    r = line[:index] + chr(c)
    if index < -1:
        r += line[index + 1 :]

    return r


def new(password):
    while password := inc(password, -1):
        if not any(
            ord(a) == ord(b) - 1 == ord(c) - 2
            for a, b, c in zip(password, password[1:], password[2:])
        ):
            continue
        if set(password).intersection({"i", "o", "l"}):
            continue
        if sum(list(len(list(v)) >= 2 for _, v in groupby(password))) < 2:
            continue
        break
    return password


print("Part 1:", password := new(password))
print("Part 2:", new(password))
