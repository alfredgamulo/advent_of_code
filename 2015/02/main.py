import sys

lines = sys.stdin.readlines()

paper = 0
ribbon = 0
for size in lines:
    a, b, c = map(int, size.split("x"))
    paper += 2 * a * b + 2 * a * c + 2 * b * c + (a * b * c) // max(a, b, c)
    ribbon += 2 * (a + b + c) - (2 * max(a, b, c)) + a * b * c

print("Part 1:", paper)
print("Part 1:", ribbon)
