import string
import sys
from collections import defaultdict


def solve(coords):
    min_x = min(coords, key=lambda tup: tup[0])
    max_x = max(coords, key=lambda tup: tup[0])
    min_y = min(coords, key=lambda tup: tup[1])
    max_y = max(coords, key=lambda tup: tup[1])
    # create the alphabet references
    points = {}
    for i,c in enumerate(coords):
        points[string.ascii_letters[i]] = c

    # produce distance map
    graph = defaultdict(lambda: ("",float('inf')))
    for p,c in points.items():
        for x in range(min_x[0]-1, max_x[0]+2):
            for y in range(min_y[1]-1, max_y[1]+2):
                d = abs(x-c[0])+abs(y-c[1])
                if graph[(x,y)][1] > d:
                    graph[(x,y)] = (p, d)
                elif graph[(x,y)][1] == d:
                    graph[(x,y)] = (".", d)

    # count the points for letters
    counter = defaultdict(int)
    for g in graph.values():
        counter[g[0]] += 1

    # remove infinites
    for x in range(min_x[0]-1, max_x[0]+2):
        counter.pop(graph[(x, min_y[1]-1)][0], None)
        counter.pop(graph[(x, max_y[1]+1)][0], None)
    for y in range(min_y[1]-1, max_y[1]+2):
        counter.pop(graph[(min_x[0]-1, y)][0], None)
        counter.pop(graph[(max_x[0]+1, y)][0], None)

    print("Part 1:", max(counter.values()))

    safe_region = 0

    for (x,y) in graph.keys():
        m = 0
        for (a,b) in coords:
            m += abs(x-a) + abs(y-b)
        if m<10000:
            safe_region+=1

    print("Part 2:", safe_region)

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    coords = [tuple(map(int, s.split(", "))) for s in lines]
    solve(coords)
