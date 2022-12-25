import sys


def part1(lines):
    dec = 0
    for line in lines:
        for i, c in enumerate(line):
            try:
                c = int(c)
            except ValueError:
                c = -1 if c == "-" else -2
            dec += c * (5 ** (len(line) - (i + 1)))

    res = ""
    while dec > 0:
        if dec % 5 == 3:
            res = "=" + res
            dec += 2
        elif dec % 5 == 4:
            res = "-" + res
            dec += 1
        else:
            res = str(dec % 5) + res
        dec //= 5
    return res


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
