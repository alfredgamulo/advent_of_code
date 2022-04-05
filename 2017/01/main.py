import sys


def part1(line):
    numbers = [int(n) for n in line]
    numbers.append(numbers[0])
    sum = 0
    for i, j in zip(numbers, numbers[1:]):
        if i == j:
            sum += i
    return sum


def part2(line):
    numbers = [int(n) for n in line]
    sum = 0
    for i, j in zip(
        numbers, numbers[(len(numbers) // 2) :] + numbers[: len(numbers) // 2]
    ):
        if i == j:
            sum += i
    return sum


if __name__ == "__main__":
    line = sys.stdin.read().strip()

    print("Part 1:", part1(line))
    print("Part 2:", part2(line))
