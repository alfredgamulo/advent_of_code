import re
import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
from pathlib import Path

# from github_com import fro


def drop_bricks():
    m, k_supports_v, k_supported_by_v = dict(), defaultdict(set), defaultdict(set)

    while bricks:
        z1, z2, x1, x2, y1, y2, brick = heappop(bricks)
        brick_pts = [
            (x, y, z)
            for x in range(x1, x2 + 1)
            for y in range(y1, y2 + 1)
            for z in range(z1, z2 + 1)
        ]
        while True:
            new_brick_pts = [(x, y, z - 1) for x, y, z in brick_pts]
            supporting_bricks = set(
                [m[(x, y, z)] for x, y, z in new_brick_pts if (x, y, z) in m]
            )
            if supporting_bricks or any([z == 0 for _, _, z in new_brick_pts]):
                break
            brick_pts = new_brick_pts
        for x, y, z in brick_pts:
            m[(x, y, z)] = brick
        k_supported_by_v[brick] = supporting_bricks
        for supporting_brick in supporting_bricks:
            k_supports_v[supporting_brick].add(brick)
    return k_supports_v, k_supported_by_v


def part1(k_supports_v, k_supported_by_v):
    return sum(
        all([len(k_supported_by_v[b2]) != 1 for b2 in k_supports_v[b]])
        for b in range(1, total_bricks + 1)
    )


def part2(k_supports_v, k_supported_by_v):
    sum2 = 0
    for b in range(1, total_bricks + 1):
        bricks_moved = set([b])
        bfs = deque(list(k_supports_v[b]))
        while bfs:
            current = bfs.popleft()
            if not all([n in bricks_moved for n in k_supported_by_v[current]]):
                continue
            bricks_moved.add(current)
            bfs.extend(k_supports_v[current])
        sum2 += len(bricks_moved) - 1
    return sum2


if __name__ == "__main__":
    bricks = []
    for line in Path(sys.argv[1]).read_text().splitlines():
        x1, y1, z1, x2, y2, z2 = map(int, re.findall("\\d+", line))
        heappush(bricks, (z1, z2, x1, x2, y1, y2, len(bricks) + 1))
    total_bricks = len(bricks)

    context = drop_bricks()
    print("Part 1:", part1(*context))
    print("Part 2:", part2(*context))
