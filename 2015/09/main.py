import sys
from pprint import PrettyPrinter
from itertools import permutations

pp = PrettyPrinter()

places = set()
lookup = {}
for line in sys.stdin.readlines():
    source, _, destination, _, distance = line.strip().split()
    distance = int(distance)
    places.add(source)
    places.add(destination)
    lookup[(source, destination)] = distance
    lookup[(destination, source)] = distance


ROUTES = {}
count = 0
shortest = sys.maxsize
longest = 0
for p in permutations(list(places)):
    distance = sum(map(lambda x: lookup[(x[0], x[1])], zip(p, p[1:])))
    shortest = min(shortest, distance)
    longest = max(longest, distance)

print("Part 1:", shortest)
print("Part 2:", longest)
