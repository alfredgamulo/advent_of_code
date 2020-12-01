def get_input():
    entries = []
    with open("input") as f:
        for line in f.readlines():
            entries.append(int(line.strip()))
    return sorted(entries)


def part1():
    entries = get_input()
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            x = entries[i]
            y = entries[j]
            if x + y == 2020:
                return x * y
            if x + y > 2020:
                break


print(part1())


def part2():
    entries = get_input()
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            x = entries[i]
            y = entries[j]
            if x + y < 2020:
                for k in range(j+1, len(entries)):
                    z = entries[k]
                    if x + y + z == 2020:
                        return x * y * z
                    if x + y + z > 2020:
                        break
            if x + y > 2020:
                break


print(part2())
