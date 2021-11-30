class Computer:
    """
    Intcode Computer
    """

    def __init__(self, file, inputs):
        self.file = file
        self.program = self.read_input(self.file)
        self.program.extend([0] * len(self.program) * 100)
        self.relative_base = 0
        self.inputs = inputs
        self.outputs = []

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
                if not self.inputs:
                    return False
                i = int(self.inputs.pop(0))
                print("input:", i)
                if param_modes == 2:
                    self.program[self.program[pos + 1] + self.relative_base] = i
                else:
                    self.program[self.program[pos + 1]] = i
                pos += 2
            elif opcode == 4:
                o = self.get_parameters(1, param_modes, pos)
                self.outputs.append(o)
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
        # print("\nHalting...")
        return True


def part1():
    computer = Computer("input", [1])
    print(computer.run())
    print(computer.outputs)


part1()


def part1():
    computer = Computer("input", [2])
    print(computer.run())
    print(computer.outputs)


part1()
