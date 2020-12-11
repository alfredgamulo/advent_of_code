import time
start_time = time.time()

with open("input") as f:
    area = f.read().splitlines()

rows = len(area)
cols = len(area[0])

neighbors = (
    (-1,-1),
    (-1, 0),
    (-1,+1),
    ( 0,-1),
    ( 0,+1),
    (+1,-1),
    (+1, 0),
    (+1,+1)
)

rules = {
    ".": 0,
    "L": 0,
    "#": 1
}

def part1(area):
    changed = True

    while changed:
        new = []
        changed = False
        for r in range(rows):
            new_row = []
            for c in range(cols):
                l = area[r][c]
                if l == ".":
                    new_row.append(".")
                    continue
                s = sum([rules[area[r+x][c+y]] for (x, y) in neighbors if rows > r+x >= 0 and cols > c+y >= 0])
                if l == "L" and s == 0:
                    changed = True
                    new_row.append("#")
                elif l == "#" and s >= 4:
                    changed = True
                    new_row.append("L")
                else:
                    new_row.append(l)
            new.append("".join(new_row))
        area = new

    count = 0
    for r in range(rows):
        count += sum(1 for c in area[r] if c == "#")
    return count

def part2(area):
    changed = True
    
    while changed:
        new = []
        changed = False

        for r in range(rows):
            new_row = []
            for c in range(cols):
                l = area[r][c]
                if l == ".":
                    new_row.append(".")
                    continue
                s = 0
                for (x, y) in neighbors:
                    dx = x
                    dy = y
                    while rows > r+dx >= 0 and cols > c+dy >= 0 and area[r+dx][c+dy] == ".":
                        dx += x
                        dy += y
                    if rows > r+dx >= 0 and cols > c+dy >= 0:
                        s += rules[area[r+dx][c+dy]]
                if l == "L" and s == 0:
                    changed = True
                    new_row.append("#")
                elif l == "#" and s >= 5:
                    changed = True
                    new_row.append("L")
                else:
                    new_row.append(l)
            new.append("".join(new_row))
        area = new

    count = 0
    for r in range(rows):
        count += sum(1 for c in area[r] if c == "#")
    return count

print("Part 1:", part1(area))
print("Part 2:", part2(area))
print("--- %s millis ---" % ((time.time() - start_time)*1000))