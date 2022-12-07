import sys
from collections import defaultdict
from pathlib import Path


def run(lines):
    path = Path()
    filesizes = {}
    for line in lines:
        match line.split():
            case ("$", "cd", dir):
                path = path.joinpath(dir).resolve()
            case ("$", "ls"):
                ...
            case ("dir", dir):
                ...
            case (num, file):
                f = path.joinpath(file)
                filesizes[f] = int(num)

    dir_sizes = defaultdict(int)
    for f, v in filesizes.items():
        paths = str(f).split("/")[:-1]
        for i in range(1, len(paths) + 1):
            dir_sizes["/".join(paths[:i])] += v

    p1_target = 100000  # magic number
    print("Part 1:", sum(v for v in dir_sizes.values() if v <= p1_target))

    p2_target = 30000000 - (70000000 - dir_sizes[""])  # magic numbers
    for v in sorted(dir_sizes.values()):
        if v > p2_target:
            print("Part 2:", v)
            break


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    run(lines)
