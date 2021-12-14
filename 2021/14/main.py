import sys
from collections import defaultdict

lines = map(str.strip, sys.stdin.read().split("\n\n"))
template = next(lines)
rules = {r.split(" -> ")[0]: r.split(" -> ")[1] for r in next(lines).split("\n")}


def run(steps):
    counter = defaultdict(int)
    pairs = defaultdict(int)
    for a, b in zip(template, template[1:]):
        pairs[a + b] += 1

    for _ in range(steps):
        newpairs = defaultdict(int)
        for k, v in pairs.items():
            if v > 0:
                newpairs[k[0] + rules[k]] += v
                newpairs[rules[k] + k[1]] += v
                counter[rules[k]] += v
        pairs = newpairs

    return max(counter.values()) - min(counter.values()) - 1


print("Part 1:", run(10))
print("Part 2:", run(40))
