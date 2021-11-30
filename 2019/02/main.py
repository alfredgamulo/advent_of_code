def read_input(file):
    program = []
    with open(file) as f:
        program = list(map(int, f.readline().split(",")))
    return program


def program_runner1(program):
    pos = 0
    print("Starting...")
    while program[pos] != 99:
        print(".", end="")
        if program[pos] == 1:
            program[program[pos + 3]] = (
                program[program[pos + 1]] + program[program[pos + 2]]
            )
            pos += 4
        elif program[pos] == 2:
            program[program[pos + 3]] = (
                program[program[pos + 1]] * program[program[pos + 2]]
            )
            pos += 4
        else:
            print("Unknown opcode")
            return program
    print("\nHalting...")
    return program


def part1():
    program = read_input("input")
    print(program)
    output = program_runner1(program)
    return output


print(part1())


def part2():
    original = read_input("input")
    program = list(original)
    for x in range(0, 100):
        for y in range(0, 100):
            print("Attempting part 2 with:", x, y)
            program[1] = x
            program[2] = y
            output = program_runner1(program)
            if output[0] == 19690720:
                print("found!")
                print(100 * output[1] + output[2])
                return output
            else:
                program = list(original)


print(part2())
