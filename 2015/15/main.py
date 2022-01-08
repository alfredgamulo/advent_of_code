import sys
from collections import defaultdict
from itertools import permutations
from pprint import PrettyPrinter

pp = PrettyPrinter()

lines = sys.stdin.readlines()

ingredients = defaultdict(dict)
for line in lines:
    line = line.strip()
    name, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
    name = name[:-1]
    capacity = int(capacity[:-1])
    durability = int(durability[:-1])
    flavor = int(flavor[:-1])
    texture = int(texture[:-1])
    calories = int(calories)
    ingredients[name] = {
        "capacity": capacity,
        "durability": durability,
        "flavor": flavor,
        "texture": texture,
        "calories": calories,
    }

pp.pprint(ingredients)


def get_highscore(check_calories=False):
    highscore = set()
    for p in permutations(range(1, 101), len(ingredients)):
        if sum(p) != 100:
            continue
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for i, ingredient in enumerate(ingredients):
            capacity += ingredients[ingredient]["capacity"] * p[i]
            durability += ingredients[ingredient]["durability"] * p[i]
            flavor += ingredients[ingredient]["flavor"] * p[i]
            texture += ingredients[ingredient]["texture"] * p[i]
            calories += ingredients[ingredient]["calories"] * p[i]

        if check_calories and calories != check_calories:
            continue
        capacity = max(0, capacity)
        durability = max(0, durability)
        flavor = max(0, flavor)
        texture = max(0, texture)
        highscore.add(capacity * durability * flavor * texture)

    return max(highscore)


print("Part 1:", get_highscore())
print("Part 2:", get_highscore(500))  # 11171160
