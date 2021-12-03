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

oxygen = lines[:]
for n in range(bits):
    if len(oxygen) == 1:
        break
    oc = sum(o[n] == "1" for o in oxygen)
    g = "1" if oc >= len(oxygen) / 2 else "0"
    oxygen = [o for o in oxygen if o[n] == g]

co2 = lines[:]
for n in range(bits):
    if len(co2) == 1:
        break
    cc = sum(c[n] == "1" for c in co2)
    e = "0" if cc >= len(co2) / 2 else "1"
    co2 = [c for c in co2 if c[n] == e]

print("Part 2:", int(oxygen[0], 2) * int(co2[0], 2))