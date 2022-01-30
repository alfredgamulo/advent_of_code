import sys

lines = sys.stdin.readlines()


def solve(keypadkeypad, position):
    k_range = range(0, len(keypad))
    code = ""
    for line in lines:
        for instruction in line:
            match instruction:
                case "U":
                    np = [position[0] - 1, position[1]]
                case "L":
                    np = [position[0], position[1] - 1]
                case "R":
                    np = [position[0], position[1] + 1]
                case "D":
                    np = [position[0] + 1, position[1]]
            if np[0] in k_range and np[1] in k_range and keypad[np[0]][np[1]]:
                position = np
        code += keypad[position[0]][position[1]]
    return code


keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

print("Part 1:", solve(keypad, [1, 1]))

keypad = [
    [0, 0, "1", 0, 0],
    [0, "2", "3", "4", 0],
    ["5", "6", "7", "8", "9"],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]

print("Part 2:", solve(keypad, [2, 0]))
