import random
import networkx


class Computer:
    """
    Intcode Computer
    """

    def __init__(self, file):
        self.file = file
        self.program = self.read_input(self.file)
        self.program.extend([0] * len(self.program) * 100)
        self.relative_base = 0

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
                i = yield
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
    computer = Computer("input")
    gen = computer.run()
    next(gen)
    path = []
    pos = (0, 0)
    ci = 0
    path.append(pos)
    graph = networkx.Graph()
    graph.add_node(pos)
    oxygen = None
    commands = (1, 4, 2, 3)
    while True:
        try:
            command = commands[ci]

            new_pos = None
            if command == 1:
                new_pos = (pos[0], pos[1] - 1)
            if command == 4:
                new_pos = (pos[0] + 1, pos[1])
            if command == 2:
                new_pos = (pos[0], pos[1] + 1)
            if command == 3:
                new_pos = (pos[0] - 1, pos[1])
            if new_pos in path:
                path = path[: path.index(new_pos)]

            feedback = gen.send(command)
            next(gen)

            if feedback == 0:
                ci = (ci - 1 + len(commands)) % len(commands)
            else:
                graph.add_node(new_pos)
                graph.add_edge(pos, new_pos)
                pos = new_pos
                path.append(pos)
                ci = (ci + 1) % len(commands)
                if feedback == 2:
                    oxygen = pos
                    break
        except StopIteration as e:
            break

    for y in range(-25, 25):
        for x in range(-25, 25):
            if (x, y) in path:
                if x == y == 0:
                    print("S", end="")
                    continue
                if (x, y) == oxygen:
                    print("E", end="")
                    continue
                print("\u2593", end="")
            elif (x, y) in graph:
                print("\u2591", end="")
            else:
                print(" ", end="")
        print()

    return len(path) - 1, networkx.eccentricity(graph, v=oxygen)


run = main()
print(f"Part 1: {run[0]} Part 2: {run[1]}")
