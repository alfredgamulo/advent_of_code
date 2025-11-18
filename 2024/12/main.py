import sys
from collections import deque
from pathlib import Path


def solve(coords):
    """Calculate perimeter and number of sides for a region"""
    # Part 1: Count perimeter (edges touching non-region cells)
    perimeter = 0
    for x, y in coords:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (x + dx, y + dy) not in coords:
                perimeter += 1

    # Part 2: Count sides by grouping edges
    # A side is a maximal sequence of collinear boundary edges
    visited_edges = set()
    sides = 0

    for x, y in coords:
        # Check each direction for a boundary edge
        for direction, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in coords:  # This is a boundary edge
                edge_key = (x, y, direction)
                if edge_key not in visited_edges:
                    # Start a new side by tracing connected edges in this direction
                    sides += 1
                    queue = [edge_key]

                    while queue:
                        cx, cy, cd = queue.pop(0)
                        if (cx, cy, cd) in visited_edges:
                            continue
                        visited_edges.add((cx, cy, cd))

                        # Get the perpendicular directions (along the edge)
                        if cd in [0, 1]:  # Left/right edge (vertical edge)
                            # Move along y-axis
                            perp_dirs = [(0, -1), (0, 1)]
                        else:  # Top/bottom edge (horizontal edge)
                            # Move along x-axis
                            perp_dirs = [(-1, 0), (1, 0)]

                        # Check neighbors in perpendicular direction
                        for pdx, pdy in perp_dirs:
                            next_x, next_y = cx + pdx, cy + pdy
                            if (next_x, next_y) in coords:
                                # Check if this neighbor has the same boundary edge
                                check_x, check_y = next_x + dx, next_y + dy
                                if (check_x, check_y) not in coords:
                                    next_edge = (next_x, next_y, cd)
                                    if next_edge not in visited_edges:
                                        queue.append(next_edge)

    return perimeter, sides


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    regions = list()
    visited = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x, y) in visited:
                continue
            new_region = set()
            search = deque([(x, y)])
            visited.add((x, y))
            while search:
                sx, sy = search.popleft()
                new_region.add((sx, sy))
                # Check all 4 neighbors
                for nx, ny in [(sx - 1, sy), (sx + 1, sy), (sx, sy - 1), (sx, sy + 1)]:
                    if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                        if (nx, ny) not in visited and lines[ny][nx] == c:
                            visited.add((nx, ny))
                            search.append((nx, ny))
            regions.append(new_region)

    p1 = 0
    p2 = 0
    for r in regions:
        perimeter, sides = solve(r)
        p1 += len(r) * perimeter
        p2 += len(r) * sides

    print("Part 1:", p1)
    print("Part 2:", p2)
