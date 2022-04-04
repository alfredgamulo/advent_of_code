import sys
from itertools import permutations


def part1(lines, password):
    for line in lines:
        match line.split(" "):
            case ("swap", "position", x, "with", "position", y):

                x, y = int(x), int(y)
                temp = password[x]
                password[x] = password[y]
                password[y] = temp
            case ("swap", "letter", x, "with", "letter", y):
                newp = []
                for p in password:
                    if x == p:
                        newp.append(y)
                    elif y == p:
                        newp.append(x)
                    else:
                        newp.append(p)
                password = newp
            case ("rotate", direction, x, "steps"):
                x = int(x)
                if direction == "right":
                    for _ in range(x):
                        newp = list(password[-1])
                        newp.extend(password[:-1])
                        password = newp
                else:
                    for _ in range(x):
                        newp = list(password[1:])
                        newp.extend(password[0])
                        password = newp

            case ("rotate", "based", "on", "position", "of", "letter", x):
                idx = password.index(x)
                for _ in range(idx + 1):
                    newp = list(password[-1])
                    newp.extend(password[:-1])
                    password = newp
                if idx > 3:
                    newp = list(password[-1])
                    newp.extend(password[:-1])
                    password = newp
            case ("reverse", "positions", x, "through", y):
                x, y = int(x), int(y)
                password = password[:x] + password[x : y + 1][::-1] + password[y + 1 :]
            case ("move", "position", x, "to", "position", y):
                x, y = int(x), int(y)
                letter = password[x]
                word = password[:x] + password[x + 1 :]
                password = word[:y] + list(letter) + word[y:]
    return "".join(password)


def part2(lines):
    for p in permutations("abcdefgh"):
        if "fbgdceah" == part1(lines, list(p)):
            return "".join(p)


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1(lines, list("abcdefgh")))
    print("Part 2:", part2(lines))
