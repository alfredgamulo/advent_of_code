import sys

data = sys.stdin.read().strip().split("\n\n")
numbers = data[0].split(",")
groups = [d.split("\n") for d in data[1:]]
boards = [b.split() for b in [" ".join(g) for g in groups]]


def play(b, n):
    try:
        i = b.index(n)
        b[i] = False
    except ValueError:
        pass
    if (
        not any(b[:5])
        or not any(b[5:10])
        or not any(b[10:15])
        or not any(b[15:20])
        or not any(b[20:25])
        or not any([b[0], b[5], b[10], b[15], b[20]])
        or not any([b[1], b[6], b[11], b[16], b[21]])
        or not any([b[2], b[7], b[12], b[17], b[22]])
        or not any([b[3], b[8], b[13], b[18], b[23]])
        or not any([b[4], b[9], b[14], b[19], b[24]])
    ):
        return True, b, n
    return False


winners = []
for n in numbers:
    if not boards:
        break
    remove = []
    for i, b in enumerate(boards):
        found = play(b, n)
        if found:
            winners.append(found)
            remove.append(b)
    for r in remove:
        boards.remove(r)

print("Part 1:", sum(map(int, winners[0][1])) * int(winners[0][2]))
print("Part 2:", sum(map(int, winners[-1][1])) * int(winners[-1][2]))
