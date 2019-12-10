def read_input(file):
    field = []
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, l in enumerate(line):
                if l == "#":
                    field.append((x,y))
    return field


def part1():
    field = read_input("input")
    print(field)
    
    slopes = {} # map: field => slope, direction[True|False]
    for f in field:
        for i in range(field.index(f)+1, len(field)):
            g = field[i]
            try:
                slope = (g[1]-f[1])/(g[0]-f[0])
            except ZeroDivisionError:
                slope = "undefined"
            if f[0] != g[0]:
                direction = f[0] < g[0]
            else:
                direction = f[1] < g[1]
            if f not in slopes:
                slopes[f] = set()
            slopes[f].add((slope, direction))
            if g not in slopes:
                slopes[g] = set()
            slopes[g].add((slope, not direction))
    
    a_count = 0
    for k, v in slopes.items():
        if len(v) > a_count:
            a_count = len(v)
    return a_count


print(part1())