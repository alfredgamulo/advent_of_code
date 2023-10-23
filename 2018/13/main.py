import sys
from itertools import count, cycle

intersection_turns = {
    "<": "v<^",
    "^": "<^>",
    ">": "^>v",
    "v": ">v<",
}

curve_turns = {
    ("<", "/"): "v",
    ("<", "\\"): "^",
    ("^", "/"): ">",
    ("^", "\\"): "<",
    (">", "/"): "^",
    (">", "\\"): "v",
    ("v", "/"): "<",
    ("v", "\\"): ">",
}

movement = {
    "<": (-1, 0),
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
}


def solve(tracks, carts):
    for tick in count():
        occupied = set([(x, y) for x, y, _, _ in carts])
        carts.sort(key=lambda x: (x[1], x[0]))
        for t in range(len(carts)):
            x, y, direction, option = carts[t]
            occupied.remove((x, y))
            move = movement[direction]
            x, y = x + move[0], y + move[1]
            if tracks[(x, y)] in ("/", "\\"):
                direction = curve_turns[(direction, tracks[(x, y)])]
            elif tracks[(x, y)] == "+":
                direction = intersection_turns[direction][next(option)]
            carts[t] = (x, y, direction, option)
            if (x, y) in occupied:
                return (x, y, tick)
            occupied.add((x, y))


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    tracks = {}
    carts = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] in ("/", "\\", "-", "|", "+"):
                tracks[(x, y)] = lines[y][x]
            elif lines[y][x] in ("<", ">"):
                tracks[(x, y)] = "|"
                carts.append((x, y, lines[y][x], cycle(range(3))))
            elif lines[y][x] in ("^", "v"):
                tracks[(x, y)] = "-"
                carts.append((x, y, lines[y][x], cycle(range(3))))

    print("Part 1:", solve(tracks, carts))
