import sys
from collections import defaultdict
from contextlib import suppress


def parse(lines):
    reqs = defaultdict(list)
    steps = set()
    for line in lines:
        s = line.split(" ")
        a, b = (s[1], s[7])
        steps.add(a)
        steps.add(b)
        reqs[b].append(a)

    steps = sorted(list(steps))
    return steps, reqs


def part1(lines):
    steps, reqs = parse(lines)

    complete = []
    while True:
        if len(complete) == len(steps):
            break
        for s in steps:
            if s not in complete and not reqs[s]:
                complete.append(s)
                for r in reqs.values():
                    with suppress(ValueError):
                        r.remove(s)
                break

    return "".join(complete)


def part2(lines):
    steps, reqs = parse(lines)
    base_time = 60
    available_workers = 5
    time = 0
    workers = {}
    complete = []
    while True:
        if len(complete) == len(steps):
            break
        workers = {k: v - 1 for k, v in workers.items()}
        for k, v in workers.items():
            if v == 0:
                complete.append(k)
                for r in reqs.values():
                    with suppress(ValueError):
                        r.remove(k)
        for c in complete:
            with suppress(KeyError):
                del workers[c]

        for s in steps:
            if (
                s not in complete
                and not reqs[s]
                and s not in workers
                and len(workers) < available_workers
            ):
                workers[s] = ord(s) - 64 + base_time
        time += 1

    return time - 1


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
