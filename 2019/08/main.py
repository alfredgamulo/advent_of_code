def read_input(file):
    with open(file) as f:
        return f.readline().strip()


def main():
    image = read_input("input")
    W = 25
    H = 6
    L = W * H

    layers = [image[i : i + L] for i in range(0, len(image), L)]

    mins = float("inf")
    for c, l in enumerate(layers):
        if l.count("0") < mins:
            mins = l.count("0")
            ones = l.count("1")
            twos = l.count("2")
            lnum = c
    print("Part 1:", lnum, ones, twos, ones * twos)

    vis = ["3" for i in range(0, L)]

    for l in layers:
        for i, p in enumerate(l):
            if vis[i] == "3" and p != "2":
                vis[i] = p

    vis = "".join(vis)
    print("Part 2:", vis)
    lvis = [vis[i : i + W] for i in range(0, len(vis), W)]
    for l in lvis:
        print(l)


main()
