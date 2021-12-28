import sys

lines = sys.stdin.readlines()

code = 0
mem = 0
for line in lines:
    line = line.strip()
    code += len(line)
    mem += len(eval(line))

print("Part 1:", code - mem)

extra = 0
for line in lines:
    line = line.strip()
    extra += 2 + line.count("\\") + line.count('"')

print("Part 2:", extra)
