import sys


def solve(line, limit):
    while len(line) < limit:
        a = line
        b = "".join(["0" if x == "1" else "1" for x in line[::-1]])
        line = a + "0" + b
    line = line[:limit]
    checksum = line
    while len(checksum) % 2 == 0:
        new_checksum = ""
        for x, y in zip(checksum[::2], checksum[1::2]):
            new_checksum += "1" if x == y else "0"
        checksum = new_checksum
    return checksum


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    print("Part 1:", solve(line, 272))
    print("Part 2:", solve(line, 35651584))
