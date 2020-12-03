forest = []

with open("input") as f:
    for line in f.readlines():
        forest.append(line.strip())

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
    ]

multiplied = 1

for slope in slopes:
    x = slope[0]
    y = slope[1]
    posx = 0
    posy = 0
    trees = 0
    
    for line in forest:
        if posy % y == 0:
            if line[posx] == '#':
                trees += 1
            posx = (posx + x) % len(line)
        posy += 1
    
    print(slope, trees)
    
    multiplied *= trees

print(multiplied)
