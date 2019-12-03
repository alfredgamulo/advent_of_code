def read_input(file):
    with open(file) as f:
        wire1 = f.readline().strip().split(',')
        wire2 = f.readline().strip().split(',')
    return wire1, wire2


def get_coords(wire):
    coords = []
    pos = (0,0)
    for w in wire:
        op = w[0]
        dist = int(w[1:])
        for i in range(dist):
            if op == 'U':
                pos = (pos[0]+1, pos[1])
            elif op == 'D':
                pos = (pos[0]-1, pos[1])
            elif op == 'L':
                pos = (pos[0], pos[1]-1)
            elif op == 'R':
                pos = (pos[0], pos[1]+1)
            else:
                print("PROBLEM:", w, op, dist)
                exit()
            coords.append(pos)
    return coords


def part1():
    wire1, wire2 = read_input("input")
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = set(coords1).intersection(set(coords2))
    closest_intersection = float('inf')
    for i in intersections:
        distance = abs(i[0])+abs(i[1])
        if distance < closest_intersection:
            closest_intersection = distance
    return(closest_intersection)
    

print(part1())


def part2():
    wire1, wire2 = read_input("input")
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = set(coords1).intersection(set(coords2))
    total_steps = []
    for i in intersections:
        steps1 = coords1.index(i)
        steps2 = coords2.index(i)
        total_steps.append(steps1+steps2+2) # 2 is the offset added because we didn't include origin
    return(min(total_steps))


print(part2())