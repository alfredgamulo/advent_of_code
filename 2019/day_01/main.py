import math


def calc(num):
    fuel = math.floor(num/3) - 2
    return fuel if fuel > 0 else 0
    

def part1():
    fuel = 0
    with open("input") as f:
        for line in f.readlines():
            num = int(line.strip())
            fuel = fuel + calc(num)
    return fuel


print(part1())


def part2():
    fuel = part1()
    more_fuel = fuel
    while more_fuel > 0:
        print(".."+str(more_fuel))
        more_fuel = calc(more_fuel)
        fuel = fuel + more_fuel
        
    return fuel


print(part2())