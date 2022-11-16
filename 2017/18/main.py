import sys


def part1(lines):
    registers = {}
    pointer = 0
    sound = None
    receive = None
    while instruction := lines[pointer]:
        registers.setdefault(instruction.split()[1], 0)
        match instruction.split():
            case ("snd", x):
                sound = registers.get(x, None)
                pointer += 1
            case ("set", x, y):
                registers[x] = registers.get(y) or int(y)
                pointer += 1
            case ("add", x, y):
                registers[x] += registers.get(y) or int(y)
                pointer += 1
            case ("mul", x, y):
                registers[x] *= registers.get(y) or int(y)
                pointer += 1
            case ("mod", x, y):
                registers[x] = registers[x] % (registers.get(y) or int(y))
                pointer += 1
            case ("rcv", x):
                if registers[x] != 0:
                    receive = sound
                    return receive
                pointer += 1
            case ("jgz", x, y):
                if registers[x] > 0:
                    pointer += int(y)
                else:
                    pointer += 1
        if 0 > pointer or pointer >= len(lines):
            break
    return receive


def part2():
    pass


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
