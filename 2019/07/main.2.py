from itertools import permutations


class Computer():
    """
    Intcode Computer
    """

    def __init__(self, file, signals):
        self.file = file
        self.program = self.read_input(self.file)
        self.signals = signals
        self.output = []

    def read_input(self, file):
        program = []
        with open(file) as f:
            program = list(map(int, f.readline().split(',')))
        return program

    def get_parameters(self, num, param_modes, pos):
        ret = []
        for n in range(num):
            mode = param_modes % 10
            if mode == 0:
                ret.append(self.program[self.program[pos+1]])
            else:
                ret.append(self.program[pos+1])
            param_modes = param_modes // 10
            pos += 1
        return ret

    def run(self):
        pos = 0
        # print("Starting...")
        while self.program[pos] != 99:
            opcode = self.program[pos] % 100
            param_modes = self.program[pos] // 100
            if opcode == 1:
                a, b = self.get_parameters(2, param_modes, pos)
                self.program[self.program[pos+3]] = a + b
                pos += 4
            elif opcode == 2:
                a, b = self.get_parameters(2, param_modes, pos)
                self.program[self.program[pos+3]] = a * b
                pos += 4
            elif opcode == 3:
                if not self.signals:
                    return False
                i = int(self.signals.pop(0))
                # print("input:", i)
                self.program[self.program[pos+1]] = i
                pos += 2
            elif opcode == 4:
                o = self.get_parameters(1, param_modes, pos)[0]
                # print("output:", o)
                self.output.append(o)
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
                self.program[self.program[pos+3]] = c
                pos += 4
            elif opcode == 8:
                a, b = self.get_parameters(2, param_modes, pos)
                if a == b:
                    c = 1
                else:
                    c = 0
                self.program[self.program[pos+3]] = c
                pos += 4

            else:
                print("Unknown opcode:", self.program[pos])
                exit()
        # print("\nHalting...")
        return True


def part2():
    max_output = 0
    maximum_p = None
    signal = 0
    for p in permutations([5, 6, 7, 8, 9]):
        signals = {
            0: [p[0], 0],
            1: [p[1]],
            2: [p[2]],
            3: [p[3]],
            4: [p[4]]
        }
        final = False
        while not final:
            file = "input"
            for i in range(5):
                computer = Computer(file, signals[i][:])
                ret = computer.run()
                signals[(i+1) % 5].append(computer.output[-1])
                if i == 4 and ret:
                    final = True
                    signal = computer.output[-1]
            
        if signal > max_output:
            max_output = signal
            maximum_p = p
    
    print("maximum signal output:", max_output)
    print("config", maximum_p)


part2()
