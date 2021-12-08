import sys

lines = sys.stdin.readlines()
cases = [line.split(" | ") for line in lines]
cases = [(input.split(), display.split()) for input, display in cases]

part1 = 0
for c in cases:
    for display in c[1]:
        if len(display) in (2, 3, 4, 7):
            part1 += 1
print("Part 1", part1)

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
    connector_map = {}
    connector_map["a"] = set(input[1]) - set(input[0])
    ced = (
        (set(input[9]) - set(input[6]))
        .union(set(input[9]) - set(input[7]))
        .union(set(input[9]) - set(input[8]))
    )
    connector_map["e"] = ced - set(input[2])
    connector_map["d"] = ced - set(input[0]) - connector_map["e"]
    connector_map["c"] = ced - connector_map["e"] - connector_map["d"]
    connector_map["g"] = (
        set(input[9]) - set(input[2]) - connector_map["a"] - connector_map["e"]
    )
    connector_map["f"] = set(input[0]) - connector_map["c"]
    connector_map["b"] = (
        set(input[9])
        - set(input[1])
        - connector_map["d"]
        - connector_map["e"]
        - connector_map["g"]
    )
    return connector_map


part2 = 0
for c in cases:
    input = sorted(["".join(sorted(i)) for i in c[0]], key=len)
    display = ["".join(sorted(i)) for i in c[1]]
    connector_map = get_connector_map(input)
    translate_map = {min(v): k for k, v in connector_map.items()}
    number = ""
    for d in display:
        t = "".join(sorted("".join(min(translate_map[v]) for v in list(d))))
        number += segment_map[t]
    part2 += int(number)

print("Part 2:", part2)
