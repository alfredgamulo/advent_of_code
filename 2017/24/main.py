import sys


def part1(components):
    def solve(components, bridge, search):
        strength = sum(sum(b) for b in bridge)
        for i, c in enumerate(components):
            if search in c:
                copy = components[:]
                cord = copy.pop(i)
                new_search = cord[(cord.index(search) + 1) % 2]
                strength = max(strength, solve(copy, bridge[:] + [cord], new_search))
        return strength

    return solve(components, [], 0)


def part2(components):
    def solve(components, bridge, search):
        length, strength = len(bridge), sum(sum(b) for b in bridge)
        for i, c in enumerate(components):
            if search in c:
                copy = components[:]
                cord = copy.pop(i)
                new_search = cord[(cord.index(search) + 1) % 2]
                new_length, new_strength = solve(copy, bridge[:] + [cord], new_search)
                if new_length > length:
                    length = new_length
                    strength = new_strength
                if new_length == length:
                    if new_strength > strength:
                        strength = new_strength
        return length, strength

    return solve(components, [], 0)[1]


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    components = [tuple(map(int, line.split("/"))) for line in lines]

    print("Part 1:", part1(components))
    print("Part 2:", part2(components))
