import sys


def work(point, plots, overlap):
    if point in plots:
        overlap.add(point)
    plots.add(point)


p1_plots = set()
p2_plots = set()
p1_overlap = set()
p2_overlap = set()
for line in map(lambda l: l.strip().split(" -> "), sys.stdin.readlines()):
    x1, y1 = map(int, line[0].split(","))
    x2, y2 = map(int, line[1].split(","))
    if x1 == x2:
        for p in range(min(y1, y2), max(y1, y2) + 1):
            point = (x1, p)
            work(point, p1_plots, p1_overlap)
            work(point, p2_plots, p2_overlap)
    elif y1 == y2:
        for p in range(min(x1, x2), max(x1, x2) + 1):
            point = (p, y1)
            work(point, p1_plots, p1_overlap)
            work(point, p2_plots, p2_overlap)
    else:
        slope = (y2 - y1) / (x2 - x1)
        b = y1 - x1 * slope
        for p in range(min(x1, x2), max(x1, x2) + 1):
            point = (p, (slope * p + b) // 1)
            work(point, p2_plots, p2_overlap)

print("Part 1:", len(p1_overlap))
print("Part 2:", len(p2_overlap))
