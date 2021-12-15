import sys

lines = sys.stdin.readlines()

nice = 0
for line in lines:
    if (
        line.count("a")
        + line.count("e")
        + line.count("i")
        + line.count("o")
        + line.count("u")
        < 3
    ):
        continue
    if sum(a == b for a, b in zip(line, line[1:])) < 1:
        continue
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        continue
    nice += 1

print("Part 1:", nice)

nice = 0
for line in lines:
    pairs = False
    for a, b in zip(line, line[1:]):
        if line.count(a + b) > 1:
            pairs = True
    if not pairs:
        continue
    if sum(a == c for a, b, c in zip(line, line[1:], line[2:])) < 1:
        continue
    nice += 1

print("Part 2:", nice)
