import sys
from functools import cache
from pathlib import Path


@cache
def blink(stone, count):
    if count == 0:
        return 1
    match stone:
        case("0"):
            return blink("1", count - 1)
        case(s) if len(stone) % 2 == 0:
            return blink(str(int(s[0:len(s) // 2])), count - 1) + blink(str(int(s[len(s) // 2:])), count - 1)
        case _:
            return blink(str(int(stone) * 2024), count - 1)


def solve(stones, count):
    return sum(blink(stone, count) for stone in stones)


if __name__ == "__main__":
    stones = (Path(sys.argv[1]).read_text().splitlines()[0].split())
    print("Part 1:", solve(stones, 25))
    print("Part 2:", solve(stones, 75))
