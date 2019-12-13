import os


class Computer():
    """
    Intcode Computer
    """

    def __init__(self, file):
        self.file = file
        self.program = self.read_input(self.file)
        self.program.extend([0]*len(self.program)*100)
        self.relative_base = 0
        self.ball_x = 0
        self.padd_x = 0

    def read_input(self, file):
        program = []
        with open(file) as f:
            program = list(map(int, f.readline().split(',')))
        return program

    def get_parameters(self, num, param_modes, pos):
        ret = []
        for n in range(num):
            mode = param_modes % 10
            if mode == 0: # position mode
                ret.append(self.program[self.program[pos+1]])
            elif mode == 1: # immediate mode
                ret.append(self.program[pos+1])
            elif mode == 2: # relative mode
                ret.append(self.program[self.program[pos+1]+self.relative_base])
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
                    self.program[self.program[pos+3]+self.relative_base] = a + b
                else:
                    self.program[self.program[pos+3]] = a + b
                pos += 4
            elif opcode == 2:
                a, b = self.get_parameters(2, param_modes, pos)
                if param_modes // 100 == 2:
                    self.program[self.program[pos+3]+self.relative_base] = a * b
                else:
                    self.program[self.program[pos+3]] = a * b
                pos += 4
            elif opcode == 3:
                i = 0
                if self.ball_x < self.padd_x:
                    i = -1
                if self.ball_x > self.padd_x:
                    i = 1
                # print("input:", i)
                if param_modes == 2:
                    self.program[self.program[pos+1]+self.relative_base] = i
                else:
                    self.program[self.program[pos+1]] = i
                pos += 2
            elif opcode == 4:
                o = self.get_parameters(1, param_modes, pos)
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
                    self.program[self.program[pos+3]+self.relative_base] = c
                else:
                    self.program[self.program[pos+3]] = c
                pos += 4
            elif opcode == 8:
                a, b = self.get_parameters(2, param_modes, pos)
                if a == b:
                    c = 1
                else:
                    c = 0
                if param_modes // 100 == 2:
                    self.program[self.program[pos+3]+self.relative_base] = c
                else:
                    self.program[self.program[pos+3]] = c
                pos += 4
            elif opcode == 9:
                a = self.get_parameters(1, param_modes, pos)
                self.relative_base = self.relative_base + a
                pos += 2
            else:
                print("Unknown opcode:", self.program[pos])
                exit()
        return "Halt"


def part1():
    computer = Computer("input")
    gen = computer.run()

    output = []
    while True:
        try:
            output.append(next(gen))
        except StopIteration as e:
            break
    
    n = 3
    tiles = [output[i*n:(i+1)*n] for i in range((len(output)+(n-1))//n)]
    #print(tiles)
    block_tiles = len(list(filter(lambda t: t[2] == 2, tiles)))
    return block_tiles


print("Part 1:", part1())


def part2():
    computer = Computer("input")
    computer.program[0] = 2
    gen = computer.run()
    
    output = {}
    score = 0
    p = False
    while True:
        try:
            x = next(gen)
            y = next(gen)
            b = next(gen)
            
            if x == -1 and y == 0:
                score = b
            else:
                if b == 0:
                    b = " "
                elif b == 1:
                    b = "X"
                elif b == 2:
                    b = "-"
                elif b == 3:
                    p = True
                    b = "="
                    computer.padd_x = x
                elif b == 4:
                    p = True
                    b = "o"
                    computer.ball_x = x
                output[(x,y)] = b
            
            if p:
                p = False
                # clear screen and print game
                os.system('clear')
                print("Score:", score)
                for y in range(50):
                    for x in range(50):
                        if (x,y) in output:
                            b = output[(x,y)]
                            print(b, end="")
                        else:
                            print(" ", end="")
                    print()
        except StopIteration as e:
            break
    return score

print("Part 2:", part2())
