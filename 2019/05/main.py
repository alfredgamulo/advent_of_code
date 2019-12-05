def read_input(file):
    program = []
    with open(file) as f:
        program = list(map(int, f.readline().split(',')))
    return program


def program_runner1(program):
    pos = 0
    print("Starting...")
    while program[pos] != 99:
        opcode = program[pos] % 100
        param_modes = program[pos] // 100
        if opcode == 1:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            program[program[pos+3]] = a + b
            pos += 4
        elif opcode == 2:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            program[program[pos+3]] = a * b
            pos += 4
        elif opcode == 3:
            i = int(input("input:"))
            program[program[pos+1]] = i
            pos += 2
        elif opcode == 4:
            if param_modes % 10 == 0:
                o = program[program[pos+1]]
            else: 
                o = program[pos+1]
            print("output:", o)
            pos += 2
            if o != 0:
                if program[pos] != 99:
                    print("error")
                    exit()
                return o
        elif opcode == 5:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            if a != 0:
                pos = b
            else: 
                pos += 3
        elif opcode == 6:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            if a == 0:
                pos = b
            else:
                pos += 3
        elif opcode == 7:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            if a < b:
                c = 1
            else: 
                c = 0
            program[program[pos+3]] = c
            pos += 4
        elif opcode == 8:
            a_mode = param_modes % 10
            if a_mode == 0:
                a = program[program[pos+1]]
            else:
                a = program[pos+1]
            b_mode = param_modes // 10
            if b_mode == 0:
                b = program[program[pos+2]]
            else:
                b = program[pos+2]
            if a == b:
                c = 1
            else: 
                c = 0
            program[program[pos+3]] = c
            pos += 4
            
        else:
            print("Unknown opcode:", program[pos])
            return program
    print("\nHalting...")
    return program
            
                
def part1():
    program = read_input("input")
    print(program)
    output = program_runner1(program)
    return output
    

print("Part 1:", part1())


def part2():
    program = read_input("input")
    print(program)
    output = program_runner1(program)
    return output
                

print("Part 2:", part2())
