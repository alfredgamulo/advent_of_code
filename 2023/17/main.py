import sys
from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path


def dijkstra(min_steps, max_steps):
    visited = defaultdict(lambda: float("inf"))
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]
    while heap:
        heat, (x, y, d) = heappop(heap)
        if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            return heat
        if heat > visited[x, y, d]:
            continue
        dx, dy = d
        for next_dx, next_dy in ((-dy, dx), (dy, -dx)):
            next_heat = heat
            for steps in range(1, max_steps + 1):
                next_x, next_y = x + next_dx * steps, y + next_dy * steps
                if next_x in range(len(grid)) and next_y in range(len(grid[0])):
                    next_heat += grid[next_x][next_y]
                    if steps < min_steps:
                        continue
                    vector = (next_x, next_y, (next_dx, next_dy))
                    if next_heat < visited[vector]:
                        visited[vector] = next_heat
                        heappush(heap, (next_heat, vector))
    return float("inf")


if __name__ == "__main__":
    grid = [list(map(int, line)) for line in Path(sys.argv[1]).read_text().splitlines()]
    print(f"Part 1: {dijkstra(1, 3)}")
    print(f"Part 2: {dijkstra(4, 10)}")
