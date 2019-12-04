INPUT = "172851-675869"


def fits1(number, lower, upper):
    str_n = str(number)

    # It is a six-digit number.
    if len(str_n) != 6: 
        # print(f"{number} Not a six-digit number.")
        return False

    # The value is within the range given in your puzzle input.
    if number < lower or number > upper:
        # print(f"{number} Not between {lower} and {upper}")
        return False

    # Going from left to right, the digits never decrease
    for i in range(len(str_n)-1):
        if str_n[i] > str_n[i+1]:
            # print(f"{number} Digits decrease")
            return False

    # Two adjacent digits are the same
    pairs = list(zip(str_n, str_n[1:]))
    for x, y in pairs:
        if x == y:
            return True
    # print(f"{number} No adjacent matches")
    
    # Conditions unmet
    return False


def part1():
    lower, upper = list(map(int, INPUT.split("-")))
    matches = []
    for i in range(lower, upper):
        if fits1(i, lower, upper):
            matches.append(i)
    # print("Matches:", matches)
    return matches


print("Part 1:", len(part1()))


def fits2(number):
    str_n = str(number)
    triplets = set()
    for x, y, z in list(zip(str_n, str_n[1:], str_n[2:])):
       if x == y == z:
           triplets.add(x)
    for x, y in list(zip(str_n, str_n[1:])):
        if x == y and x not in triplets:
            return True
    return False


def part2():
    matches = part1()
    matches2 = []
    for m in matches:
        if fits2(m):
            matches2.append(m)
    # print("Matches2:", matches2)
    return matches2


print("Part 2:", len(part2()))
