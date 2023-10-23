import sys
from collections import deque


def solve(pots, rules, rounds):
    for i in range(rounds):
        new_pots = set()
        buffer = deque(".....")
        for p in range(min(pots) - 2, max(pots) + 3):
            buffer.popleft()
            if (p + 2) in pots:
                buffer.append("#")
            else:
                buffer.append(".")

            if "".join(buffer) in rules:
                new_pots.add(p)
        print(i + 1, "\t", sum(new_pots), "\tdiff:", sum(new_pots) - sum(pots))
        pots = new_pots

    return sum(pots)


if __name__ == "__main__":
    sections = sys.stdin.read().split("\n\n")

    initial_state = sections[0].split(": ")[1]
    pots = set([i for i, p in enumerate(initial_state) if p == "#"])

    rules = set()
    for r in sections[1].splitlines():
        k, v = r.split(" => ")
        if v == "#":
            rules.add(k)

    print("Part 1:", solve(pots, rules, 200))
    # Stabilizes, check diffs in output
    print("Part 2:", 10390 + 73 * (50000000000 - 118))
