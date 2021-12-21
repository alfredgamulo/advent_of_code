import sys
from collections import defaultdict, Counter, deque
from pprint import PrettyPrinter
from itertools import combinations

pp = PrettyPrinter(indent=2)

lines = sys.stdin.read().split("\n\n")
scanner_data = defaultdict(dict)
for i, line in enumerate(lines):
    data = line.strip().split("\n")
    for j, probes in enumerate(data[1:]):
        scanner_data[i][j] = tuple(map(int, probes.split(",")))

rotations = {
    0: lambda x, y, z: (x, y, z),
    1: lambda x, y, z: (x, -z, y),
    2: lambda x, y, z: (x, -y, -z),
    3: lambda x, y, z: (x, z, -y),
    4: lambda x, y, z: (-x, -y, z),
    5: lambda x, y, z: (-x, -z, -y),
    6: lambda x, y, z: (-x, y, -z),
    7: lambda x, y, z: (-x, z, y),
    8: lambda x, y, z: (y, -x, z),
    9: lambda x, y, z: (y, -z, -x),
    10: lambda x, y, z: (y, x, -z),
    11: lambda x, y, z: (y, z, x),
    12: lambda x, y, z: (-y, x, z),
    13: lambda x, y, z: (-y, -z, x),
    14: lambda x, y, z: (-y, -x, -z),
    15: lambda x, y, z: (-y, z, -x),
    16: lambda x, y, z: (z, y, -x),
    17: lambda x, y, z: (z, x, y),
    18: lambda x, y, z: (z, -y, x),
    19: lambda x, y, z: (z, -x, -y),
    20: lambda x, y, z: (-z, x, -y),
    21: lambda x, y, z: (-z, y, x),
    22: lambda x, y, z: (-z, -x, y),
    23: lambda x, y, z: (-z, -y, -x),
}
known_beacons = Counter()
for beacon in scanner_data[0].values():
    known_beacons[beacon] += 1
known_scanners = {0: (0, 0, 0)}


def find_scanner_match(scanner):
    for r in rotations:
        for k in known_scanners.keys():
            x_diff_counter = Counter()
            y_diff_counter = Counter()
            z_diff_counter = Counter()
            for b in scanner_data[k].values():
                for q in scanner_data[scanner].values():
                    x, y, z = rotations[r](q[0], q[1], q[2])
                    x_diff_counter[b[0] - x] += 1
                    y_diff_counter[b[1] - y] += 1
                    z_diff_counter[b[2] - z] += 1
                if (
                    x_diff_counter.most_common(1)[0][1] >= 12
                    and y_diff_counter.most_common(1)[0][1] >= 12
                    and z_diff_counter.most_common(1)[0][1] >= 12
                ):
                    return {
                        "rotation": r,
                        "x_offset": x_diff_counter.most_common(1)[0][0],
                        "y_offset": y_diff_counter.most_common(1)[0][0],
                        "z_offset": z_diff_counter.most_common(1)[0][0],
                    }


tries = deque(range(1, len(scanner_data)))
while tries:
    t = tries.popleft()
    data = find_scanner_match(t)
    if not data:
        tries.append(t)
        continue
    known_scanners[t] = (data["x_offset"], data["y_offset"], data["z_offset"])
    for i, beacon in scanner_data[t].items():
        x, y, z = rotations[data["rotation"]](beacon[0], beacon[1], beacon[2])
        x += data["x_offset"]
        y += data["y_offset"]
        z += data["z_offset"]
        known_beacons[(x, y, z)] += 1
        scanner_data[t][i] = (x, y, z)

print("Part 1:", len(known_beacons))

part2 = 0
for s1, s2 in combinations(known_scanners.values(), 2):
    manhattan = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2])
    part2 = max(part2, manhattan)

print("Part 2:", part2)
