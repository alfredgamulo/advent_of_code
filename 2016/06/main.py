import sys
from collections import Counter

messages = list(map(str.strip, sys.stdin.readlines()))

turned = list(zip(*messages))

part1 = ""
part2 = ""
for t in turned:
    c = Counter(t)
    part1 += c.most_common()[0][0]
    part2 += c.most_common()[-1][0]

print("Part 1:", part1)
print("Part 2:", part2)
