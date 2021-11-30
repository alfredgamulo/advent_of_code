class SpaceObject:
    """
    Universal Orbit Map Object
    """

    def __init__(self, name):
        self.name = name
        self.root = None


def read_input(file):
    object_map = {}
    with open(file) as f:
        for line in f.readlines():
            a_name, b_name = line.strip().split(")")
            if a_name not in object_map:
                a_object = SpaceObject(a_name)
                object_map[a_name] = a_object
            if b_name not in object_map:
                b_object = SpaceObject(b_name)
                object_map[b_name] = b_object
            a_object = object_map.get(a_name)
            b_object = object_map.get(b_name)
            b_object.root = a_object
    return object_map


def part1():
    object_map = read_input("input")
    count = 0
    for space_object in object_map.values():
        while space_object.root:
            count += 1
            space_object = space_object.root
    print(count)


part1()


def part2():
    object_map = read_input("input")
    you_set = set()
    san_set = set()
    you = object_map.get("YOU")
    san = object_map.get("SAN")
    while you.root:
        you_set.add(you.root)
        you = you.root
    while san.root:
        san_set.add(san.root)
        san = san.root
    union = you_set.intersection(san_set)
    you_unique = you_set.difference(union)
    san_unique = san_set.difference(union)
    hops = len(you_unique) + len(san_unique)
    print(hops)


part2()
