import string
import sys
from functools import cache
from itertools import count

moves = None


@cache
def dance(programs):
    programs = list(programs)
    for move in moves:
        if "s" in move:
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]
            pass
        if "x" in move:
            a, b = map(int, move[1:].split("/"))
            programs[a], programs[b] = programs[b], programs[a]
        if "p" in move:
            a, b = move[1:].split("/")
            a = programs.index(a)
            b = programs.index(b)
            programs[a], programs[b] = programs[b], programs[a]
    return "".join(programs)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    moves = tuple(lines[0].strip().split(","))
    programs = string.ascii_letters[:16]
    programs = dance(programs)

    print("Part 1:", "".join(programs))

    programs = string.ascii_letters[:16]
    for c in count(1):
        programs = dance(programs)
        if programs == string.ascii_letters[:16]:
            break
    for _ in range(1000000000 % c):
        programs = dance(programs)

    print("Part 2:", "".join(programs))
