import queue
import string
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

instructions = None


def program(program_number, qthis, qthat):
    global instructions
    registers = defaultdict(int)
    registers["p"] = program_number

    sound = None  # for part 1

    pointer = 0
    count = 0

    def read(value):
        if value in string.ascii_lowercase:
            return registers[value]
        return int(value)

    while 0 <= pointer < len(instructions):
        instruction = instructions[pointer]

        match instruction.split():
            case ("snd", x):
                sound = read(x)
                if qthat:
                    qthat.put(read(x))
                count += 1
            case ("set", x, y):
                registers[x] = read(y)
            case ("add", x, y):
                registers[x] += read(y)
            case ("mul", x, y):
                registers[x] *= read(y)
            case ("mod", x, y):
                registers[x] = registers[x] % (read(y))
            case ("rcv", x):
                if qthis:
                    try:
                        r = qthis.get(timeout=1)
                        registers[x] = r
                    except queue.Empty:
                        return count
                else:
                    if registers[x] != 0:
                        return sound
            case ("jgz", x, y):
                if read(x) > 0:
                    pointer += read(y) - 1
        pointer += 1
    return count


def part1():
    return program(0, None, None)


def part2():
    pool = ThreadPoolExecutor(2)

    q0 = queue.Queue()
    q1 = queue.Queue()

    pool.submit(program, 0, q0, q1)
    return pool.submit(program, 1, q1, q0).result()


if __name__ == "__main__":
    instructions = list(map(str.strip, sys.stdin.readlines()))

    print("Part 1:", part1())
    print("Part 2:", part2())
