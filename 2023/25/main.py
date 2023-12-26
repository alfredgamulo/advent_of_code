import sys
from itertools import combinations
from pathlib import Path

import networkx as nx


def part1():
    for source, sink in combinations(g.nodes(), 2):
        cut_value, (left, right) = nx.minimum_cut(g, source, sink)
        if cut_value == 3:
            return len(left) * len(right)


if __name__ == "__main__":
    g = nx.Graph()
    for line in Path(sys.argv[1]).read_text().splitlines():
        component, connections = line.split(": ")
        for connection in connections.split(" "):
            g.add_edge(component, connection, capacity=1)
    print("Part 1:", part1())
    print("Part 2: Merry Christmas!")
