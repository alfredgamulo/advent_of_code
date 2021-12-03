import sys

lines = sys.stdin.readlines()
bits = len(lines[0].strip())

gamma = ""
for n in range(bits):
    count = sum(line[n] == "1" for line in lines)
    gamma += "1" if count > len(lines) / 2 else "0"

gamma = int(gamma, 2)
epsilon = gamma ^ int("1" * bits, 2)

print("Part 1:", gamma * epsilon)
