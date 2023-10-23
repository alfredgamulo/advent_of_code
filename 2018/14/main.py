import sys


def part1(magic_number):
    elf0, elf1 = 0, 1
    recipes = [3, 7]
    while len(recipes) < magic_number + 10:
        score0 = recipes[elf0]
        score1 = recipes[elf1]
        combined_score = str(score0 + score1)
        for c in combined_score:
            recipes.append(int(c))
        elf0 = (elf0 + 1 + score0) % len(recipes)
        elf1 = (elf1 + 1 + score1) % len(recipes)
    return "".join(map(str, recipes[magic_number : magic_number + 10]))


def part2(magic_number):
    elf0, elf1 = 0, 1
    recipes = [3, 7]
    while True:
        score0 = recipes[elf0]
        score1 = recipes[elf1]
        combined_score = str(score0 + score1)
        for c in combined_score:
            recipes.append(int(c))
            if (
                len(recipes) >= len(magic_number)
                and "".join(map(str, recipes[-(len(magic_number)) :])) == magic_number
            ):
                return len(recipes[: -(len(magic_number))])

        elf0 = (elf0 + 1 + score0) % len(recipes)
        elf1 = (elf1 + 1 + score1) % len(recipes)


if __name__ == "__main__":
    magic_number = int(sys.stdin.read())

    print("sample:", part1(9))
    print("sample:", part1(5))
    print("sample:", part1(18))
    print("sample:", part1(2018))
    print("Part 1:", part1(magic_number))
    print("sample:", part2("51589"))
    print("sample:", part2("01245"))
    print("sample:", part2("92510"))
    print("sample:", part2("59414"))
    print("Part 2:", part2(str(magic_number)))
