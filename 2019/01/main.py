def calc1(module):
    fuel = (module // 3) - 2
    return fuel if fuel > 0 else 0


def part1():
    fuel = 0
    with open("input") as f:
        for line in f.readlines():
            module = int(line.strip())
            fuel = fuel + calc1(module)
    return fuel


print(part1())


def calc2(module):
    fuel = calc1(module)
    more_fuel = fuel
    while more_fuel > 0:
        more_fuel = calc1(more_fuel)
        fuel = fuel + more_fuel
    return fuel


def part2():
    fuel = 0
    with open("input") as f:
        for line in f.readlines():
            module = int(line.strip())
            fuel = fuel + calc2(module)
    return fuel


print(part2())
