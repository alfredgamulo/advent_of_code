class Computer:
    """
    Intcode Computer
    """

    def __init__(self, input):
        self.input = input
        self.program = self.read_input(self.input)

    def read_input(self, file):
        program = []
        with open(file) as f:
            program = list(map(int, f.readline().split(",")))
        return program

    def get_parameters(self, num, param_modes, pos):
        ret = []
        for n in range(num):
            mode = param_modes % 10
            if mode == 0:
                ret.append(self.program[self.program[pos + 1]])
            else:
                ret.append(self.program[pos + 1])
            param_modes = param_modes // 10
            pos += 1
        return ret

    def run(self):
        pos = 0
        print("Starting...")
        while self.program[pos] != 99:
            opcode = self.program[pos] % 100
            param_modes = self.program[pos] // 100
            if opcode == 1:
                a, b = self.get_parameters(2, param_modes, pos)
                self.program[self.program[pos + 3]] = a + b
                pos += 4
            elif opcode == 2:
                a, b = self.get_parameters(2, param_modes, pos)
                self.program[self.program[pos + 3]] = a * b
                pos += 4
            elif opcode == 3:
                i = int(input("input:"))
                self.program[self.program[pos + 1]] = i
                pos += 2
            elif opcode == 4:
                o = self.get_parameters(1, param_modes, pos)[0]
                print("output:", o)
                pos += 2
                if o != 0:
                    if self.program[pos] != 99:
                        print("error")
                        exit()
                    # return o
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
                self.program[self.program[pos + 3]] = c
                pos += 4
            elif opcode == 8:
                a, b = self.get_parameters(2, param_modes, pos)
                if a == b:
                    c = 1
                else:
                    c = 0
                self.program[self.program[pos + 3]] = c
                pos += 4

            else:
                print("Unknown opcode:", self.program[pos])
                return self.program
        print("\nHalting...")
        return self.program


computer = Computer("input")
computer.run()
