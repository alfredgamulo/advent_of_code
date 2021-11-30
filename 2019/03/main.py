def read_input(file):
    with open(file) as f:
        wire1 = f.readline().strip().split(",")
        wire2 = f.readline().strip().split(",")
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = set(coords1).intersection(set(coords2))
    return coords1, coords2, intersections


def get_coords(wire):
    coords = []
    pos = (0, 0)
    for w in wire:
        op = w[0]
        dist = int(w[1:])
        for i in range(dist):
            if op == "U":
                pos = (pos[0] + 1, pos[1])
            elif op == "D":
                pos = (pos[0] - 1, pos[1])
            elif op == "L":
                pos = (pos[0], pos[1] - 1)
            elif op == "R":
                pos = (pos[0], pos[1] + 1)
            else:
                print("PROBLEM:", w, op, dist)
                exit()
            coords.append(pos)
    return coords


def part1():
    coords1, coords2, intersections = read_input("input")
    closest_intersection = float("inf")
    for i in intersections:
        distance = abs(i[0]) + abs(i[1])
        if distance < closest_intersection:
            closest_intersection = distance
    return closest_intersection


print("Part 1:", part1())


def part2():
    coords1, coords2, intersections = read_input("input")
    min_steps = float("inf")
    for i in intersections:
        steps1 = coords1.index(i)
        steps2 = coords2.index(i)
        intersection_steps = (
            steps1 + steps2 + 2
        )  # 2 is the offset added because we didn't include origin
        if intersection_steps < min_steps:
            min_steps = intersection_steps
    return min_steps


print("Part 2:", part2())
