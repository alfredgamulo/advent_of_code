import copy
import re
import sys
from collections import deque
from contextlib import suppress
from math import prod
from pathlib import Path


def part1():
    accepted, namespace = [], {}
    for part in parts:
        for rating in part[1:-1].split(","):
            exec(rating, namespace)
        consider = "in"
        while consider not in "RA":
            workflow = rules[consider]
            for w in workflow:
                with suppress(ValueError):
                    condition, outcome = w.split(":")
                    if eval(condition, namespace):
                        consider = outcome
                        break
                consider = w
        [[], accepted]["RA".index(consider)].append(sum([namespace[c] for c in "xmas"]))
    return sum(accepted)


def part2():
    total = 0
    dq = deque((("in", [[1, 4001], [1, 4001], [1, 4001], [1, 4001]]),))
    while dq and (search := dq.popleft()):
        consider, xmas = search
        if consider in "RA":
            total += [0, prod(h - l for l, h in xmas)]["RA".index(consider)]
            continue
        for w in rules[consider]:
            with suppress(ValueError):
                condition, outcome = w.split(":")
                part, comparator, number = condition[0], condition[1], condition[2:]
                nxmas = copy.deepcopy(xmas)
                update = [
                    max(xmas["xmas".index(part)]["><".index(comparator)], int(number) + 1),
                    min(xmas["xmas".index(part)]["><".index(comparator)], int(number)),
                ]["><".index(comparator)]
                nxmas["xmas".index(part)]["><".index(comparator)] = update
                xmas["xmas".index(part)]["<>".index(comparator)] = update
                dq.append((outcome, nxmas))
                continue
            dq.append((w, xmas))
    return total


if __name__ == "__main__":
    raw_rules, parts = (l.split() for l in Path(sys.argv[1]).read_text().split("\n\n"))
    rules = {(r := re.split("{|,", raw[:-1])) and r[0]: r[1:] for raw in raw_rules}
    print("Part 1:", part1())
    print("Part 2:", part2())
