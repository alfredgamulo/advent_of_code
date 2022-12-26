def A(value):
    if value == 0:
        return 1, 1, "B"
    else:
        return 0, -1, "C"


def B(value):
    if value == 0:
        return 1, -1, "A"
    else:
        return 1, 1, "C"


def C(value):
    if value == 0:
        return 1, 1, "A"
    else:
        return 0, -1, "D"


def D(value):
    if value == 0:
        return 1, -1, "E"
    else:
        return 1, -1, "C"


def E(value):
    if value == 0:
        return 1, 1, "F"
    else:
        return 1, 1, "A"


def F(value):
    if value == 0:
        return 1, 1, "A"
    else:
        return 1, 1, "E"


if __name__ == "__main__":
    cursor = 0
    state = "A"
    ones = set()
    for _ in range(12134527):
        value = int(cursor in ones)
        write, move, new_state = locals()[state](value)
        if write == 0:
            ones.remove(cursor)
        else:
            ones.add(cursor)
        cursor += move
        state = new_state
    print("Solution:", len(ones))
