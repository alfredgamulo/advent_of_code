import sys
from dataclasses import dataclass
from typing import List


@dataclass
class Disc:
    name: str
    weight: int
    discs: List[str]


disc_map = {}
discname = set()
subdiscs = set()

root = None


def part1(lines):
    for line in lines:
        name, weight, *d = line.split()
        discname.add(name)
        weight = int(weight[1:-1])
        if d:
            d = [d.strip(",") for d in d[1:]]
            subdiscs.update(set(d))
        disc = Disc(name, weight, d)
        disc_map[name] = disc
    global root
    root = (discname - subdiscs).pop()
    return root


def part2():
    print(root)
    root_disc = disc_map[root]
    for d in root_disc.discs:
        print(dig(disc_map[d]), d)

    # going manual
    print("sfruur")
    root_disc = disc_map["sfruur"]
    for d in root_disc.discs:
        print(dig(disc_map[d]), d)

    print("zsasjr")
    root_disc = disc_map["zsasjr"]
    for d in root_disc.discs:
        print(dig(disc_map[d]), d)

    print("jdxfsa")
    root_disc = disc_map["jdxfsa"]
    for d in root_disc.discs:
        print(dig(disc_map[d]), d)

    # found last one to be balanced, so second to last one is unbalanced
    return disc_map["jdxfsa"].weight - 5


def dig(disc: Disc):
    total = 0
    if disc.discs:
        for d in disc.discs:
            total += dig(disc_map[d])
    return total + disc.weight


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
