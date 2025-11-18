import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from itertools import (batched, chain, combinations, count, groupby,
                       permutations, product, zip_longest)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter

import numpy as np


def part1(lines):
    # Parse the input
    foods = []
    all_ingredients = set()
    all_allergens = set()

    for line in lines:
        parts = line.split(" (contains ")
        ingredients = set(parts[0].split())
        allergens = set(parts[1].rstrip(")").split(", "))
        foods.append((ingredients, allergens))
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)

    # For each allergen, find which ingredients could possibly contain it
    # An ingredient can contain an allergen only if it appears in ALL foods with that allergen
    possible = {}
    for allergen in all_allergens:
        possible[allergen] = None
        for ingredients, allergens in foods:
            if allergen in allergens:
                if possible[allergen] is None:
                    possible[allergen] = ingredients.copy()
                else:
                    possible[allergen] &= ingredients

    # Find ingredients that cannot contain any allergen
    ingredients_with_allergens = set()
    for allergen in all_allergens:
        ingredients_with_allergens.update(possible[allergen])

    safe_ingredients = all_ingredients - ingredients_with_allergens

    # Count occurrences of safe ingredients
    count = 0
    for ingredients, _ in foods:
        for ingredient in ingredients:
            if ingredient in safe_ingredients:
                count += 1

    return count


def part2(lines):
    # Parse the input
    foods = []
    all_allergens = set()

    for line in lines:
        parts = line.split(" (contains ")
        ingredients = set(parts[0].split())
        allergens = set(parts[1].rstrip(")").split(", "))
        foods.append((ingredients, allergens))
        all_allergens.update(allergens)

    # For each allergen, find which ingredients could possibly contain it
    possible = {}
    for allergen in all_allergens:
        possible[allergen] = None
        for ingredients, allergens in foods:
            if allergen in allergens:
                if possible[allergen] is None:
                    possible[allergen] = ingredients.copy()
                else:
                    possible[allergen] &= ingredients

    # Solve the constraint satisfaction problem
    # Keep eliminating possibilities until each allergen has exactly one ingredient
    allergen_to_ingredient = {}

    while len(allergen_to_ingredient) < len(all_allergens):
        # Find allergens with only one possible ingredient
        for allergen in all_allergens:
            if allergen not in allergen_to_ingredient:
                if len(possible[allergen]) == 1:
                    ingredient = list(possible[allergen])[0]
                    allergen_to_ingredient[allergen] = ingredient

                    # Remove this ingredient from all other allergen possibilities
                    for other_allergen in all_allergens:
                        if other_allergen != allergen:
                            possible[other_allergen].discard(ingredient)

    # Sort by allergen and return the canonical dangerous ingredient list
    result = []
    for allergen in sorted(allergen_to_ingredient.keys()):
        result.append(allergen_to_ingredient[allergen])

    return ",".join(result)


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
