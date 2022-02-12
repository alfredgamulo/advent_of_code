import sys
from collections import defaultdict


def part1(bots):
    outputs = defaultdict(int)
    while bots:
        new_bots = defaultdict(list)
        for bot, chips in bots.items():
            if len(chips) == 2:
                a, i, b, j = instructions[bot]
                if 61 in chips and 17 in chips:
                    print("Part 1:", bot)
                if a == "bot":
                    new_bots[i].append(min(chips))
                elif a == "output":
                    outputs[i] = min(chips)
                if b == "bot":
                    new_bots[j].append(max(chips))
                elif b == "output":
                    outputs[j] = max(chips)
            else:
                new_bots[bot].extend(chips)
        bots = new_bots
    return outputs


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    bots = defaultdict(list)
    instructions = defaultdict(tuple)

    for line in lines:
        match line.split():
            case ["value", n, "goes", "to", "bot", x]:
                bots[int(x)].append(int(n))
            case ["bot", x, "gives", "low", "to", a, i, "and", "high", "to", b, j]:
                instructions[int(x)] = (a, int(i), b, int(j))

    outputs = part1(bots)
    print("Part 2:", outputs[0] * outputs[1] * outputs[2])
