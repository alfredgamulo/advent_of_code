import sys

lines = sys.stdin.readlines()
bits = len(lines[0].strip())
half = len(lines) / 2
gamma = ""
for n in range(bits):
    count = sum(line[n] == "1" for line in lines)
    gamma += "1" if count > half else "0"
gamma = int(gamma, 2)
epsilon = gamma ^ int("1" * bits, 2)

print("Part 1:", gamma * epsilon)

oxygen = lines[:]
carbon = lines[:]
for n in range(bits):
    if len(oxygen) > 1:
        count = sum(o[n] == "1" for o in oxygen)
        g = "1" if count >= len(oxygen) / 2 else "0"
        oxygen = [o for o in oxygen if o[n] == g]
    if len(carbon) > 1:
        count = sum(c[n] == "1" for c in carbon)
        e = "0" if count >= len(carbon) / 2 else "1"
        carbon = [c for c in carbon if c[n] == e]

print("Part 2:", int(oxygen[0], 2) * int(carbon[0], 2))
