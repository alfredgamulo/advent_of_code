import networkx as nx

G = nx.DiGraph()

with open("input") as f:
    for line in f.readlines():
        if "no other" in line:
            continue
        outside, inside = list(map(str.strip, line.split("contain")))
        out_node = " ".join(outside.split()[:-1])
        in_list = list(map(str.strip, inside.split(",")))
        in_nodes = dict((" ".join(s.split()[1:-1]), s[0]) for s in in_list)

        for k, v in in_nodes.items():
            G.add_edge(out_node, k, count=int(v))

# part 1
print("part 1:", len(nx.ancestors(G, "shiny gold")))

# part 2
def curse(bag, prev):
    tally = 0
    for s in G.successors(bag):
        count = G.get_edge_data(bag, s)["count"]
        tally += count + count * curse(s, count)
    return tally


print("part 2:", curse("shiny gold", 1))
