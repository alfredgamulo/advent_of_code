"""
This day does is not a general solution for any input, but a decompilation of my specific input as described in the README.
"""


def solver(part1):
    if part1:
        r = list(range(9, 0, -1))
    else:
        r = list(range(1, 10))
    model = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in r:
        if i + 9 - 2 in range(1, 10):
            model[0] = i
            model[13] = i + 9 - 2
            break
    for i in r:
        if i + 1 - 4 in range(1, 10):
            model[1] = i
            model[12] = i + 1 - 4
            break
    for i in r:
        if i + 11 - 16 in range(1, 10):
            model[2] = i
            model[11] = i + 11 - 16
            break
    for i in r:
        if i + 3 - 11 in range(1, 10):
            model[3] = i
            model[4] = i + 3 - 11
            break
    for i in r:
        if i + 5 - 6 in range(1, 10):
            model[5] = i
            model[10] = i + 5 - 6
            break
    for i in r:
        if i + 0 - 6 in range(1, 10):
            model[6] = i
            model[7] = i + 0 - 6
            break
    for i in r:
        if i + 9 - 6 in range(1, 10):
            model[8] = i
            model[9] = i + 9 - 6
            break
    return "".join([str(n) for n in model])
    

print("Part 1:", solver(1))
print("Part 2:", solver(0))
