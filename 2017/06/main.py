import sys


def solve(lines):
    seen = set()
    past = []
    last_line = None
    while tuple(lines) not in seen:
        seen.add(tuple(lines))
        past.append(tuple(lines))
        # find index of max value in list
        index_max = max(range(len(lines)), key=lines.__getitem__)
        boxes = lines[index_max]
        lines[index_max] = 0
        i = index_max + 1
        for _ in range(boxes):
            lines[i % len(lines)] += 1
            i += 1
        last_line = tuple(lines)
    print("Part 1:", len(seen))
    print("Part 2:", len(past) - past.index(last_line))


if __name__ == "__main__":
    lines = list(map(int, sys.stdin.read().split()))

    solve(lines)
