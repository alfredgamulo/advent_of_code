import collections


def read_input(file):
    field = []
    with open(file) as f:
        for y, line in enumerate(f.readlines()):
            for x, l in enumerate(line):
                if l == "#":
                    field.append((x, y))
    return field


def main():
    field = read_input("input")

    vectors = {}  # map: field => slope, direction[True|False]
    slopes = {}
    for f in field:
        for i in range(field.index(f) + 1, len(field)):
            g = field[i]

            try:
                slope = (g[1] - f[1]) / (f[0] - g[0])
            except ZeroDivisionError:
                slope = float("inf")

            if f[0] != g[0]:
                direction = f[0] < g[0]
            else:
                direction = f[1] < g[1]

            vectors.setdefault(f, set())
            vectors[f].add((slope, direction))

            vectors.setdefault(g, set())
            vectors[g].add((slope, not direction))

            slopes.setdefault(f, {})
            slopes[f].setdefault(slope, [])
            slopes[f][slope].append(g)
            slopes.setdefault(g, {})
            slopes[g].setdefault(slope, [])
            slopes[g][slope].append(f)

    # Part 1
    a_loc = None
    a_count = 0
    for k, v in vectors.items():
        if len(v) > a_count:
            a_count = len(v)
            a_loc = k

    print("Part 1:", a_loc, a_count)

    # Part 2
    od = collections.OrderedDict(sorted(slopes[a_loc].items(), reverse=True))

    # form the sequence of blasts
    # right half
    blast_list = []
    for c in od:
        if c == float("inf"):
            arr = [y for y in od[c] if y[1] < a_loc[1]]
            arr.sort(key=lambda t: t[1])
        else:
            arr = [x for x in od[c] if x[0] > a_loc[0]]
            arr.sort(key=lambda t: t[0])
        if arr:
            blast_list.append(arr)
    # left half
    for c in od:
        if c == float("inf"):
            arr = [y for y in od[c] if y[1] > a_loc[1]]
            arr.sort(key=lambda t: t[1], reverse=True)
        else:
            arr = [x for x in od[c] if x[0] < a_loc[0]]
            arr.sort(key=lambda t: t[0], reverse=True)
        if arr:
            blast_list.append(arr)

    blasted = 0
    while blasted < 200:
        for i, b in enumerate(blast_list):
            if b:
                a = b.pop(0)
                blasted += 1
                if blasted == 200:
                    break

    print("Part 2:", a, 100 * a[0] + a[1])


main()
