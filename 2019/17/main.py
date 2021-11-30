class Computer:
    """
    Intcode Computer
    """

    def __init__(self, file):
        self.file = file
        self.program = self.read_input(self.file)
        self.program.extend([0] * len(self.program) * 100)
        self.relative_base = 0
        self.instructions = []

    def read_input(self, file):
        program = []
        with open(file) as f:
            program = list(map(int, f.readline().split(",")))
        return program

    def get_parameters(self, num, param_modes, pos):
        ret = []
        for n in range(num):
            mode = param_modes % 10
            if mode == 0:  # position mode
                ret.append(self.program[self.program[pos + 1]])
            elif mode == 1:  # immediate mode
                ret.append(self.program[pos + 1])
            elif mode == 2:  # relative mode
                ret.append(self.program[self.program[pos + 1] + self.relative_base])
            param_modes = param_modes // 10
            pos += 1
        if len(ret) == 1:
            return ret[0]
        return ret

    def run(self):
        pos = 0
        print("Starting...")
        while self.program[pos] != 99:
            opcode = self.program[pos] % 100
            param_modes = self.program[pos] // 100
            if opcode == 1:
                a, b = self.get_parameters(2, param_modes, pos)
                if param_modes // 100 == 2:
                    self.program[self.program[pos + 3] + self.relative_base] = a + b
                else:
                    self.program[self.program[pos + 3]] = a + b
                pos += 4
            elif opcode == 2:
                a, b = self.get_parameters(2, param_modes, pos)
                if param_modes // 100 == 2:
                    self.program[self.program[pos + 3] + self.relative_base] = a * b
                else:
                    self.program[self.program[pos + 3]] = a * b
                pos += 4
            elif opcode == 3:
                i = self.instructions.pop(0)
                # print("input:", i)
                if param_modes == 2:
                    self.program[self.program[pos + 1] + self.relative_base] = i
                else:
                    self.program[self.program[pos + 1]] = i
                pos += 2
            elif opcode == 4:
                o = int(self.get_parameters(1, param_modes, pos))
                # print("output:", o)
                yield o
                pos += 2
            elif opcode == 5:
                a, b = self.get_parameters(2, param_modes, pos)
                if a != 0:
                    pos = b
                else:
                    pos += 3
            elif opcode == 6:
                a, b = self.get_parameters(2, param_modes, pos)
                if a == 0:
                    pos = b
                else:
                    pos += 3
            elif opcode == 7:
                a, b = self.get_parameters(2, param_modes, pos)
                if a < b:
                    c = 1
                else:
                    c = 0
                if param_modes // 100 == 2:
                    self.program[self.program[pos + 3] + self.relative_base] = c
                else:
                    self.program[self.program[pos + 3]] = c
                pos += 4
            elif opcode == 8:
                a, b = self.get_parameters(2, param_modes, pos)
                if a == b:
                    c = 1
                else:
                    c = 0
                if param_modes // 100 == 2:
                    self.program[self.program[pos + 3] + self.relative_base] = c
                else:
                    self.program[self.program[pos + 3]] = c
                pos += 4
            elif opcode == 9:
                a = self.get_parameters(1, param_modes, pos)
                self.relative_base = self.relative_base + a
                pos += 2
            else:
                print("Unknown opcode:", self.program[pos])
                exit()
        return "Halt"


def main():
    # PART 1:
    computer = Computer("input")
    computer.program[0] = 2

    gen = computer.run()
    output = []
    while True:
        try:
            o = next(gen)
            output.append(o)
            if output[-1] == 10 and output[-2] == 10:
                break
        except StopIteration:
            break

    arr = [[]]
    for c in output:
        if c == 10:
            arr.append([])
            continue
        arr[len(arr) - 1].append(chr(c))

    arr.pop(len(arr) - 1)
    arr.pop(len(arr) - 1)

    ans = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(arr[y][x], end="")
            if (
                1 < y
                and y < (len(arr) - 2)
                and 1 < x
                and x < (len(arr[y]) - 2)
                and arr[y][x] == "#"
                and arr[y - 1][x] == "#"
                and arr[y + 1][x] == "#"
                and arr[y][x - 1] == "#"
                and arr[y][x + 1] == "#"
            ):
                ans = ans + (x * y)
        print()
    print(ans)

    # PART 2:
    # This was really messy because the inputs and outputs weren't very clear.
    # Mostly manual fidgeting leading to messy spaghetti code with no re-use
    M = [x for x in "A,A,B,C,B,C,B,C,B,A"]
    M.append("\n")
    A = [x for x in "R,10,L,12,R,6"]
    A.append("\n")
    B = [x for x in "R,6,R,10,R,12,R,6"]
    B.append("\n")
    C = [x for x in "R,10,L,12,L,12"]
    C.append("\n")
    D = [x for x in ""]
    D.append("\n")
    I = [x for x in "N"]
    I.append("\n")

    instructions = M + A + B + C + D + I
    instructions = list(map(ord, instructions))
    print(instructions)
    computer.instructions = instructions

    output = []
    while True:
        try:
            o = next(gen)
            output.append(o)
            if output[-1] == 10 and output[-2] == 10:
                break
        except StopIteration:
            break
    print("".join(list(map(chr, output))))  # Testing the program input/output query

    output = []
    while True:
        try:
            o = next(gen)
            output.append(o)
            if output[-1] == 10 and output[-2] == 10:
                break
        except StopIteration:
            break

    arr = [[]]
    for c in output:
        if c == 10:
            arr.append([])
            continue
        arr[len(arr) - 1].append(chr(c))

    arr.pop(len(arr) - 1)
    arr.pop(len(arr) - 1)

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(arr[y][x], end="")
        print()

    print(next(gen))


main()
