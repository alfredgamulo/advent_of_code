import sys

sequence = sys.stdin.readline().strip()


def part1(sequence):
    i = 0
    uncompressed = []
    while i < len(sequence):
        if sequence[i] not in ("()0123456789x"):
            uncompressed.append(sequence[i])
            i += 1
            continue
        marker = ""
        while ")" not in marker:
            marker += sequence[i]
            i += 1
        left = int(marker.split("x")[0][1:])
        right = int(marker.split("x")[1][:-1])
        for _ in range(right):
            uncompressed.append(sequence[i : i + left])
        i += left
    return len("".join(uncompressed))


print("Part 1:", part1(sequence))


def part2(sequence):
    c = 0
    i = 0
    while i < len(sequence):
        if sequence[i] != "(":
            i += 1
            c += 1
            continue
        marker = ""
        while ")" not in marker:
            marker += sequence[i]
            i += 1
        left = int(marker.split("x")[0][1:])
        right = int(marker.split("x")[1][:-1])
        c += right * part2(sequence[i : i + left])
        i += left
    return c


print("Part 2:", part2(sequence))
