player = [100, 7, 3]
player = [100, 9, 0]
boss = [100, 8, 2]

while player[0] > 0 and boss[0] > 0:
    damage = boss[1] - player[2]
    damage = damage > 1 and damage or 1
    player[0] -= damage
    damage = player[1] - boss[2]
    damage = damage > 1 and damage or 1
    boss[0] -= damage

    print(player)
    print(boss)
    print("----")

if player[0] >= boss[0]:
    print("Player wins")
else:
    print("Boss wins")

# Part 1: 91
# Part 2: 158
