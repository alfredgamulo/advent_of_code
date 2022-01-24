import sys
from functools import cache

boss = tuple(map(int, [line.split(": ")[1] for line in sys.stdin.readlines()]))
boss_hp = boss[0]
boss_dmg = boss[1]
my_hp = 50
my_mana = 500

spells = {
    "Missile": {"cost": 53, "damage": 4},
    "Drain": {"cost": 73, "damage": 2, "heal": 2},
    "Shield": {"cost": 113, "duration": 6, "armor": 7},
    "Poison": {"cost": 173, "duration": 6, "dot": 3},
    "Recharge": {"cost": 229, "duration": 5, "mana": 101},
}


@cache
def turn(spell, mana_spent, my_mana, my_hp, boss_hp, shield_left, poison_left, recharge_left, hard_mode):

    if hard_mode:
        my_hp -= 1
        if my_hp <= 0:
            return sys.maxsize

    # status effects
    shield_left -= shield_left > 0 and 1 or 0
    if poison_left:
        boss_hp -= spells["Poison"]["dot"]
        poison_left -= 1
    if recharge_left:
        my_mana += spells["Recharge"]["mana"]
        recharge_left -= 1

    # my turn
    my_mana -= spells[spell]["cost"]
    mana_spent += spells[spell]["cost"]
    if my_mana < 0:
        return sys.maxsize
    match spell:
        case "Shield":
            if shield_left:
                return sys.maxsize
            shield_left = spells[spell]["duration"]
        case "Recharge":
            if recharge_left:
                return sys.maxsize
            recharge_left = spells[spell]["duration"]
        case "Poison":
            if poison_left:
                return sys.maxsize
            poison_left = spells[spell]["duration"]

    my_hp += spells[spell].get("heal", 0)
    boss_hp -= spells[spell].get("damage", 0)

    # boss turn
    my_armor = 0
    if shield_left:
        my_armor = spells["Shield"]["armor"]
        shield_left -= 1
    if recharge_left:
        my_mana += spells["Recharge"]["mana"]
        recharge_left -= 1
    if poison_left:
        boss_hp -= spells["Poison"]["dot"]
        poison_left -= 1

    if boss_hp <= 0:
        return mana_spent
    my_hp -= boss_dmg - my_armor
    if my_hp <= 0:
        return sys.maxsize

    # take next turn
    return min(
        (
            turn(spell, mana_spent, my_mana, my_hp, boss_hp, shield_left, poison_left, recharge_left, hard_mode)
            for spell in spells.keys()
        )
    )

print("Part 1:", min((turn(spell, 0, my_mana, my_hp, boss_hp, 0, 0, 0, False) for spell in spells.keys())))
print("Part 2:", min((turn(spell, 0, my_mana, my_hp, boss_hp, 0, 0, 0, True) for spell in spells.keys())))
