import sys
from itertools import batched, count
from math import inf


def loop(maps, cursor, src, dst):
    for mapping in maps:
        for m in mapping:
            if m[src][0] <= cursor < m[src][1]:
                cursor = m[dst][0] + cursor - m[src][0]
                break
    return cursor


def part1(seeds, maps):
    location = inf
    for seed in seeds:
        location = min(location, loop(maps, seed, "src", "dst"))
    return location


def part2(seeds, maps):
    seed_ranges = ((start, start + end) for start, end in batched(seeds, 2))
    for location in count():
        seed = loop(maps[-1::-1], location, "dst", "src")
        if any(start <= seed < end for start, end in seed_ranges):
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
                    "src": (src, src + rng),
                    "dst": (dst, dst + rng),
                }
            )
        maps.append(ranges)
    print("Part 1:", part1(seeds, maps))
    print("Part 2:", part2(seeds, maps))
