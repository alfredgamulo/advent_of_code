import sys
from collections import defaultdict

lines = map(str.strip, sys.stdin.read().split("\n\n"))
template = next(lines)
rules = dict(r for r in [r.split(" -> ") for r in next(lines).split("\n")])


def run(steps):
    pairs = defaultdict(int)
    for a, b in zip(template, template[1:]):
        pairs[a + b] += 1

    for _ in range(steps):
        newpairs = defaultdict(int)
        for k, v in pairs.items():
            newpairs[k[0] + rules[k]] += v
            newpairs[rules[k] + k[1]] += v
        pairs = newpairs

    counter = defaultdict(int)
    for k, v in pairs.items():
        counter[k[0]] += v
        counter[k[1]] += v

    return (max(counter.values()) - min(counter.values()) + 1) // 2


print("Part 1:", run(10))
print("Part 2:", run(40))
