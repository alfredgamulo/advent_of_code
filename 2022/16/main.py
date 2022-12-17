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


@cache
def solve(time, current, visited):
    if time < 1:
        return 0
    pressure = 0
    if current not in visited and data[current].rate > 0:
        pressure = max(
            pressure,
            solve(time - 1, current, tuple(list(visited) + [current]))
            + data[current].rate * (time - 1),
        )
    for valve in data[current].tunnels:
        pressure = max(pressure, solve(time - 1, valve, visited))
    return pressure


def part1():
    return solve(30, "AA", ())


def part2():
    return solve(26, "AA", ()) + solve(25, "VQ", ())


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    for line in lines:
        valves = re.findall(r"[A-Z]{2}", line)
        rate = re.findall(r"\d+", line)
        data[valves[0]] = Valve(valves[0], int(rate[0]), valves[1:])

    print("Part 1:", part1())
    print("Part 2:", part2())
