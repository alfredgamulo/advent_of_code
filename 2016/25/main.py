import sys


def part1(original_lines):
    a = 0
    while True:
        count = 0
        i = 0
        a += 1
        lines = original_lines.copy()
        registers = {"a": a, "b": 0, "c": 0, "d": 0}
        outs = []
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
                            try:
                                i += x != 0 and registers[y] or 1
                            except Exception:
                                i += x != 0 and int(y) or 1
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
                case ("out", x):
                    outs.append(registers[x])
                    i += 1
                    count += 1
                    if count > 50:
                        # print(a, outs, flush=True)
                        if outs == [
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                            1,
                            0,
                        ]:
                            print("Part 1:", a)
                            exit()
                        break


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))
    print("Part 1:", part1(lines.copy()), flush=True)
