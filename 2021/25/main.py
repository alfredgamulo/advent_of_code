import sys


cucumbers = [list(c) for c in (map(str.strip, sys.stdin.readlines()))]


part1 = 0
stopped = False
while not stopped:
    part1 += 1
    moved = set()
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[0])):
            if (
                cucumbers[i][j] == ">"
                and cucumbers[i][(j + 1) % len(cucumbers[0])] == "."
                and (i, j) not in moved
                and (i, (j + 1) % len(cucumbers[0])) not in moved
            ):
                cucumbers[i][j] = "."
                cucumbers[i][(j + 1) % len(cucumbers[0])] = ">"
                moved.add((i, j))
                moved.add((i, (j + 1) % len(cucumbers[0])))
    stopped = not moved
    moved = set()
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[0])):
            if (
                cucumbers[i][j] == "v"
                and cucumbers[(i + 1) % len(cucumbers)][j] == "."
                and (i, j) not in moved
                and ((i + 1) % len(cucumbers), j) not in moved
            ):
                cucumbers[i][j] = "."
                cucumbers[(i + 1) % len(cucumbers)][j] = "v"
                moved.add((i, j))
                moved.add(((i + 1) % len(cucumbers), j))
    stopped = stopped and not moved

print("Part 1:", part1)
