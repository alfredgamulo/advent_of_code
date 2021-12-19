import sys
from collections import defaultdict
from pprint import PrettyPrinter
from itertools import combinations, permutations

pp = PrettyPrinter(indent=2)

# Ingest the information
lines = sys.stdin.read().split("\n\n")
scanner_data = defaultdict(dict)
for i, line in enumerate(lines):
    data = line.strip().split("\n")
    for j, probes in enumerate(data[1:]):
        scanner_data[i][j] = tuple(map(int, probes.split(",")))
# Don't touch ^
# pp.pprint(scanner_data)


probe_difference_map = defaultdict(dict)
for s, probes in scanner_data.items():
    for i, j in permutations(range(len(probes)), 2):
        x, y, z = (
            abs(probes[i][0] - probes[j][0]),
            abs(probes[i][1] - probes[j][1]),
            abs(probes[i][2] - probes[j][2]),
        )
        probe_difference_map[s][(x, y, z)] = (i, j)
# pp.pprint(probe_difference_map[0])

scanner_probe_intersection = defaultdict(dict)
for i, j in combinations(range(len(scanner_data)+1), 2):
    common_probes = set(probe_difference_map[i].keys()).intersection(
        probe_difference_map[j].keys()
    )
    if common_probes:
        scanner_probe_intersection[(i, j)] = common_probes

# pp.pprint(scanner_probe_intersection)
