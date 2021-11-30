from collections import Counter


part1 = 0
part2 = 0

with open("input") as f:
    for line in f.readlines():
        fields = line.split(" ")
        limits = tuple(map(int, fields[0].split("-")))
        letter = fields[1].strip(":")
        passwd = fields[2]

        c = Counter(passwd)
        if limits[0] <= c[letter] <= limits[1]:
            part1 += 1

        if bool(passwd[limits[0] - 1] == letter) ^ bool(
            passwd[limits[1] - 1] == letter
        ):
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
