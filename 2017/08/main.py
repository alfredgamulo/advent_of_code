import sys

registers = {}
mval = 0


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    for line in lines:
        r1, op, a1, _, r2, cond, a2 = line.split()
        r2 = registers.get(r2, 0)

        if eval(f"{r2} {cond} {a2}"):
            if op == "inc":
                registers[r1] = registers.get(r1, 0) + int(a1)
            else:
                registers[r1] = registers.get(r1, 0) - int(a1)
            mval = max(registers[r1], mval)
    largest = max(registers, key=registers.get)
    print(largest, registers.get(largest), mval)
