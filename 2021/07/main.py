import sys

crabs = list(map(int, sys.stdin.readline().strip().split(",")))

crab_positions = [0]*(max(crabs)+1)
for f in crabs:
    crab_positions[f] += 1

fuels = []
for i in range(len(crab_positions)):
    fuel = [(abs(j - i)*cj) for j, cj in enumerate(crab_positions)]
    fuels.append(sum(fuel))

print("Part 1:", min(fuels))

fuels = []
for i in range(len(crab_positions)):
    fuel = [(sum(range(1, abs(j - i)+1))*cj) for j, cj in enumerate(crab_positions)]
    fuels.append(sum(fuel))

print("Part 2:", min(fuels))