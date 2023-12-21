import sys
from collections import defaultdict, deque
from contextlib import suppress
from math import prod
from pathlib import Path


def parse(lines):
    modules = {}
    for line in lines:
        module, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        match module[0]:
            case "%":
                modules[module[1:]] = [0, destinations]
            case "&":
                modules[module[1:]] = [defaultdict(int), destinations]
            case "b":
                modules[module] = (destinations,)
    for module in modules:
        destinations = modules[module][-1]
        for d in destinations:
            with suppress(TypeError, KeyError):
                modules[d][0][module] = 0
    return modules


def solve(modules, button_presses, track=None):
    lows, highs = 0, 0
    for i in range(1, button_presses + 1):
        pulses = deque(["broadcaster"])
        while pulses and (cursor := pulses.popleft()) and (module := modules[cursor]):
            match module:
                case (int(), list()):  # %
                    signal = module[0]
                case (dict(), list()):  # &
                    signal = [1, 0][all(module[0].values())]
                case (list(),):  # broadcaster
                    signal = 0
            for destination in module[-1]:
                highs += signal
                lows += not signal
                try:
                    modules[destination][0][cursor] = signal
                    pulses.append(destination)
                except TypeError:
                    if not signal:
                        modules[destination][0] = [1, 0][modules[destination][0]]
                        pulses.append(destination)
                except KeyError:
                    ...  # rx/output
            with suppress(TypeError, KeyError):
                if not track[cursor] and signal:
                    track[cursor] = i
    return (button_presses + lows) * highs


def part1():
    modules = parse(Path(sys.argv[1]).read_text().splitlines())
    return solve(modules, 1000)


def part2():
    modules = parse(Path(sys.argv[1]).read_text().splitlines())
    focus = next(filter(lambda n: "rx" in modules[n][-1], modules))
    track = list(filter(lambda n: focus in modules[n][-1], modules))
    track = {t: 0 for t in track}
    solve(modules, 10000, track)
    return prod(track.values())


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
