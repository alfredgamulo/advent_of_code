import sys

lines = sys.stdin.readlines()
cases = [line.split(" | ") for line in lines]
cases = [(input.split(), display.split()) for input, display in cases]
segment_map = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def get_connector_map(input):
    cm = {}
    ced = (
        (set(input[9]) - set(input[6]))
        .union(set(input[9]) - set(input[7]))
        .union(set(input[9]) - set(input[8]))
    )
    cm["a"] = set(input[1]) - set(input[0])
    cm["e"] = ced - set(input[2])
    cm["d"] = ced - set(input[0]) - cm["e"]
    cm["c"] = ced - cm["e"] - cm["d"]
    cm["f"] = set(input[0]) - cm["c"]
    cm["g"] = set(input[9]) - set(input[2]) - cm["a"] - cm["e"]
    cm["b"] = set(input[9]) - set(input[1]) - cm["d"] - cm["e"] - cm["g"]
    return cm


part1 = 0
part2 = 0
for c in cases:
    input = sorted(c[0], key=len)
    connector_map = get_connector_map(input)
    translate_map = {min(v): k for k, v in connector_map.items()}
    number = ""
    for d in c[1]:
        if len(d) in (2, 3, 4, 7):
            part1 += 1
        t = "".join(sorted("".join(min(translate_map[v]) for v in list(d))))
        number += segment_map[t]
    part2 += int(number)

print("Part 1:", part1)
print("Part 2:", part2)
