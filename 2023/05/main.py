import sys
from itertools import count
from math import inf

from more_itertools import grouper


def part1(seeds, maps):
    location = inf
    for cursor in seeds:
        for mapping in maps:
            for m in mapping:
                if cursor in m["src"]:
                    diff = cursor - m["src"][0]
                    cursor = m["dst"][diff]
                    break
        location = min(location, cursor)
    return location


def part2(seeds, maps):
    seed_range = []
    for s in grouper(seeds, 2):
        seed_range.append((range(s[0], s[0] + s[1])))

    for location in count():
        cursor = location
        for mapping in maps[-1::-1]:
            for m in mapping:
                if cursor in m["dst"]:
                    diff = cursor - m["dst"][0]
                    cursor = m["src"][diff]
                    break
        if any(cursor in s for s in seed_range):
            return location


if __name__ == "__main__":
    groups = sys.stdin.read().split("\n\n")

    seeds = list(map(int, groups[0].split(":")[1].split()))
    maps = []
    for group in groups[1:]:
        ranges = []
        for g in group.splitlines()[1:]:
            dst, src, rng = map(int, g.split())
            ranges.append(
                {
                    "src": range(src, src + rng),
                    "dst": range(dst, dst + rng),
                }
            )
        maps.append(ranges)

    print("Part 1:", part1(seeds, maps))
    print("Part 2:", part2(seeds, maps))
