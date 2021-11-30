from collections import Counter

part1 = 0
part2 = 0
with open("input") as f:
    for group in f.read().split("\n\n"):
        members = group.split()
        s = Counter("".join(members))
        part1 += len(s)
        part2 += sum(1 for f in s if s[f] >= len(members))
print(part1)
print(part2)
