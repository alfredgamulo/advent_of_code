#!/usr/bin/env python

import itertools
import networkx as nx
import string

def read_input(file):
    output = []
    with open(file) as f:
        for r in f.readlines():
            output.append(r.strip())
    return output
        

def main(s):
    maze = read_input(s)
    graph = nx.Graph()
    keys = {}
    doors = {}
    start = None
    for y in range(1, len(maze)-1):
        for x in range(1, len(maze[y])-1):
            symbol = maze[y][x]
            pos = (x, y)
            if symbol in string.ascii_uppercase:
                doors[pos] = symbol.lower()
            elif symbol in string.ascii_lowercase:
                keys[pos] = symbol
            elif symbol == "@":
                start = pos
                # keys[pos] = symbol
            if maze[y][x+1] != "#":
                graph.add_edge(pos, (x+1, y))
            if maze[y+1][x] != "#":
                graph.add_edge(pos, (x, y+1))
    for m in maze:
        print(m)

    least_steps = float('inf')
    step_cache = {}
    doors_cache = {}
    for ks in itertools.permutations(keys):
        picked_up_keys = []
        ks = list(ks)
        ks = [start] + ks
        path = []
        viable = True
        dks = set(doors.keys())
        for a, b in zip(ks[:], ks[1:]):
            if (a,b) in step_cache:
                steps = step_cache[(a,b)]
            else:
                steps = nx.bidirectional_shortest_path(graph, a, b)[1:]
                step_cache[(a,b)] = steps
            if (a,b) in doors_cache:
                doors_in_path = doors_cache[(a,b)]
            else:
                doors_in_path = dks.intersection(steps)
                doors_cache[(a,b)] = doors_in_path
            for d in doors_in_path:
                if doors[d] not in picked_up_keys:
                    viable = False
                    break
                else:
                    dks.remove(d)
            if not viable:
                break
            else:
                picked_up_keys.append(keys[b])
                path.extend(steps)
        if viable:
            if len(path) < least_steps:
                least_steps = len(path)
                print("poss", least_steps)

    return least_steps



# for s in ('sample1', 'sample2', 'sample3'):
#     print(s, main(s))


print(main('input'))