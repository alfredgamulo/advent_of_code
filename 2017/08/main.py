import sys

registers = {}


def part1(lines):
    global registers
    for line in lines:
        r1, op, a1, _, r2, cond, a2 = line.split()
        r2 = registers.get(r2, 0)

        if eval(f"{r2} {cond} {a2}"):
            if op == "inc":
                registers[r1] = registers.get(r1, 0) + int(a1)
            else:
                registers[r1] = registers.get(r1, 0) - int(a1)
    largest = max(registers, key=registers.get)
    return largest, registers.get(largest)


def part2():
    pass


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
