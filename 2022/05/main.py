import copy
import string
import sys


def print_tops(stacks):
    tops = ""
    for s in stacks:
        tops += s[-1]
    return tops


def part1(stacks, instructions):
    for i in instructions:
        _, num, _, s1, _, s2 = i.split()
        num, s1, s2 = int(num), int(s1) - 1, int(s2) - 1
        for _ in range(num):
            stacks[s2].append(stacks[s1].pop())
    return print_tops(stacks)


def part2(stacks, instructions):
    for i in instructions:
        _, num, _, s1, _, s2 = i.split()
        num, s1, s2 = int(num), int(s1) - 1, int(s2) - 1
        stacks[s2].extend(stacks[s1][len(stacks[s1]) - num :])
        del stacks[s1][len(stacks[s1]) - num :]
    return print_tops(stacks)


if __name__ == "__main__":
    sections = sys.stdin.read().split("\n\n")
    diagram = sections[0].splitlines()
    instructions = sections[1].splitlines()
    stacks = []
    for i in range(1, len(diagram[-1]), 4):
        temp = []
        for j in range(len(diagram) - 1):
            if diagram[j][i] in string.ascii_uppercase:
                temp.insert(0, diagram[j][i])
        stacks.append(temp)

    print("Part 1:", part1(copy.deepcopy(stacks), instructions))
    print("Part 2:", part2(copy.deepcopy(stacks), instructions))
