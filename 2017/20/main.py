import sys
from collections import defaultdict

particles = []


def part1(lines):
    global particles

    for id, line in enumerate(lines):
        line = line.replace("<", "(")
        line = line.replace(">", ")")
        namespace = {"p": None, "v": None, "a": None}
        for assignment in line.split(", "):
            exec(assignment, namespace)
        particles.append(
            {"p": namespace["p"], "v": namespace["v"], "a": namespace["a"], "id": id}
        )

    closest = min(
        particles, key=lambda p: abs(p["a"][0]) + abs(p["a"][1]) + abs(p["a"][2])
    )
    return closest["id"]


def part2():
    for _ in range(100):
        positions = defaultdict(list)
        for p in particles:
            p["v"] = (
                p["v"][0] + p["a"][0],
                p["v"][1] + p["a"][1],
                p["v"][2] + p["a"][2],
            )
            p["p"] = (
                p["v"][0] + p["p"][0],
                p["v"][1] + p["p"][1],
                p["v"][2] + p["p"][2],
            )
            positions[p["p"]].append(p)
        for p, v in positions.items():
            if len(v) > 1:
                for o in v:
                    particles.remove(o)

    return len(particles)


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2())
