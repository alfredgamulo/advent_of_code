import re
import sys
from dataclasses import dataclass
from functools import cache


@dataclass
class Valve:
    name: str
    rate: int
    tunnels: list


data = {}


def part1():
    @cache
    def one(time, current, visited):
        if time < 1:
            return 0
        pressure = 0
        if current not in visited and data[current].rate > 0:
            pressure = max(
                pressure,
                one(time - 1, current, tuple(list(visited) + [current]))
                + data[current].rate * (time - 1),
            )
        for valve in data[current].tunnels:
            pressure = max(pressure, one(time - 1, valve, visited))
        return pressure

    return one(30, "AA", ())


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    for line in lines:
        valves = re.findall(r"[A-Z]{2}", line)
        rate = re.findall(r"\d+", line)
        data[valves[0]] = Valve(valves[0], int(rate[0]), valves[1:])

    print("Part 1:", part1())
