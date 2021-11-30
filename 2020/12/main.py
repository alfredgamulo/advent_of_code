import time

start_time = time.time()

with open("input") as f:
    actions = [(a[0], int(a[1:])) for a in f.read().splitlines()]

cardinal = ["N", "E", "S", "W"]
face = 1
l_turn = {90: 3, 180: 2, 270: 1, 360: 0}
r_turn = {90: 1, 180: 2, 270: 3, 360: 0}

coords = []
pos = (0, 0)

for a in actions:
    op = a[0]
    dist = a[1]
    if op == "N":
        pos = (pos[0], pos[1] + dist)
    elif op == "S":
        pos = (pos[0], pos[1] - dist)
    elif op == "E":
        pos = (pos[0] + dist, pos[1])
    elif op == "W":
        pos = (pos[0] - dist, pos[1])
    elif op == "L":
        face = (face + l_turn[dist]) % 4
        continue
    elif op == "R":
        face = (face + r_turn[dist]) % 4
        continue
    elif op == "F":
        d = cardinal[face]
        if d == "N":
            pos = (pos[0], pos[1] + dist)
        elif d == "S":
            pos = (pos[0], pos[1] - dist)
        elif d == "E":
            pos = (pos[0] + dist, pos[1])
        elif d == "W":
            pos = (pos[0] - dist, pos[1])

    coords.append(pos)

print("Part 1:", (abs(coords[-1][0]) + abs(coords[-1][1])))

coords = []
pos = (0, 0)
waypoint = (10, 1)

for a in actions:
    op = a[0]
    dist = a[1]

    if op == "N":
        waypoint = (waypoint[0], waypoint[1] + dist)
    elif op == "S":
        waypoint = (waypoint[0], waypoint[1] - dist)
    elif op == "E":
        waypoint = (waypoint[0] + dist, waypoint[1])
    elif op == "W":
        waypoint = (waypoint[0] - dist, waypoint[1])
    elif op == "L":
        if dist == 90:
            waypoint = (waypoint[1] * -1, waypoint[0])
        elif dist == 180:
            waypoint = (waypoint[0] * -1, waypoint[1] * -1)
        elif dist == 270:
            waypoint = (waypoint[1], waypoint[0] * -1)
    elif op == "R":
        if dist == 90:
            waypoint = (waypoint[1], waypoint[0] * -1)
        elif dist == 180:
            waypoint = (waypoint[0] * -1, waypoint[1] * -1)
        elif dist == 270:
            waypoint = (waypoint[1] * -1, waypoint[0])
    elif op == "F":
        pos = (pos[0] + (waypoint[0] * dist), pos[1] + (waypoint[1] * dist))
        coords.append(pos)

print("Part 2:", (abs(coords[-1][0]) + abs(coords[-1][1])))

print("--- %s millis ---" % ((time.time() - start_time) * 1000))
