import sys

player1, player2 = map(lambda s: int(s.split(":")[-1].strip()), sys.stdin.readlines())

# print(player1, player2)
counter = 0

def die(sides):
    number = 0
    global counter
    while True:
        counter += 1
        number = (number) % sides + 1
        yield number 

def move(position):
    while True:
        position = position % 10 + 1
        yield position

roll = die(100)
move1 = move(player1)
move2 = move(player2)
score1 = 0
score2 = 0
while True:
    spaces = next(roll) + next(roll) + next(roll)
    for m in range(spaces):
        score = next(move1)
    score1 += score
    if score1 >= 1000:
        break

    spaces = next(roll) + next(roll) + next(roll)
    for m in range(spaces):
        score = next(move2)
    score2 += score
    if score2 >= 1000:
        break

print("Part 1:", min(score1, score2)*counter)