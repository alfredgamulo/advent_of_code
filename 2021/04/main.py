import sys

data = sys.stdin.read().strip().split("\n\n")
numbers = data[0].split(",")
groups = [d.split("\n") for d in data[1:]]
boards = [b.split() for b in [" ".join(g) for g in groups]]


def play(b, n):
    try:
        i = b.index(n)
        b[i] = False
        x = i % 5
        y = (i // 5) * 5
    except ValueError:
        return
    if not (any(b[x::5]) and any(b[y : y + 5])):
        return True


winners = []
for n in numbers:
    if not boards:
        break
    remove = []
    for i, b in enumerate(boards):
        if play(b, n):
            winners.append((b, n))
            remove.append(b)
    for b in remove:
        boards.remove(b)

print("Part 1:", sum(map(int, winners[0][0])) * int(winners[0][1]))
print("Part 2:", sum(map(int, winners[-1][0])) * int(winners[-1][1]))
