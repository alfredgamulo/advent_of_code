import sys


def perform(registers, lines):
    i = 0
    while i < len(lines):
        match lines[i].split(" "):
            case ("cpy", x, y):
                try:
                    registers[y] = registers[x]
                except Exception:
                    registers[y] = int(x)
                i += 1
            case ("inc", x):
                registers[x] += 1
                i += 1
            case ("dec", x):
                registers[x] -= 1
                i += 1
            case ("jnz", x, y):
                try:
                    i += registers[x] != 0 and registers[y] or 1
                except Exception:
                    try:
                        i += registers[x] != 0 and int(y) or 1
                    except Exception:
                        i += x != 0 and registers[y] or 1
            case ("tgl", x):
                j = i + registers[x]
                try:
                    newl = lines[j]
                except Exception:
                    i += 1
                    continue
                items = newl.split(" ")
                if len(items) == 2:
                    if "inc" in newl:
                        lines[j] = "dec " + lines[j][4:]
                    else:
                        lines[j] = "inc " + lines[j][4:]
                if len(items) == 3:
                    if "jnz" in newl:
                        lines[j] = "cpy " + lines[j][4:]
                    else:
                        lines[j] = "jnz " + lines[j][4:]
                i += 1
    return registers


def part1(lines):
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}

    return perform(registers, lines)


def part2(lines):
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}

    return perform(registers, lines)


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))
    print("Part 1:", part1(lines.copy()), flush=True)
    print("Part 2:", part2(lines.copy()))
