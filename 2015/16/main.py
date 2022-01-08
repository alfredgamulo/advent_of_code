import sys

match1 = {
    "children" : lambda x: x == 3,
    "cats" : lambda x: x == 7,
    "samoyeds" : lambda x: x == 2,
    "pomeranians" : lambda x: x == 3,
    "akitas" : lambda x: x == 0,
    "vizslas" : lambda x: x == 0,
    "goldfish" : lambda x: x == 5,
    "trees" : lambda x: x == 3,
    "cars" : lambda x: x == 2,
    "perfumes" : lambda x: x == 1,
}

match2 = {
    "children" : lambda x: x == 3,
    "cats" : lambda x: x > 7,
    "samoyeds" : lambda x: x == 2,
    "pomeranians" : lambda x: x < 3,
    "akitas" : lambda x: x == 0,
    "vizslas" : lambda x: x == 0,
    "goldfish" : lambda x: x < 5,
    "trees" : lambda x: x > 3,
    "cars" : lambda x: x == 2,
    "perfumes" : lambda x: x == 1,
}

for line in sys.stdin.readlines():
    _, id, k1, v1, k2, v2, k3, v3 = line.split()
    k1 = k1.strip(":")
    v1 = int(v1.strip(","))
    k2 = k2.strip(":")
    v2 = int(v2.strip(","))
    k3 = k3.strip(":")
    v3 = int(v3.strip(","))
    if (
        match1[k1](v1) and
        match1[k2](v2) and
        match1[k3](v3)
    ):
        print("Part 1:", id.strip(":"))
    if (
        match2[k1](v1) and
        match2[k2](v2) and
        match2[k3](v3)
    ):
        print("Part 2:", id.strip(":"))

        
