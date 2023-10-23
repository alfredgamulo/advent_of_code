import sys


def generate_power_levels(serial):
    power_levels = {}
    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial
            power_level *= rack_id
            power_level //= 100
            power_level %= 10
            power_level -= 5
            power_levels[(x, y)] = power_level
    return power_levels


def solve(power_levels, max_size):
    coords = None
    power = 0
    for size in range(2, max_size + 1):
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                total = 0
                for a in range(x, x + size):
                    for b in range(y, y + size):
                        total += power_levels[(a, b)]
                if total > power:
                    power = total
                    coords = (x, y, size)
    return coords


if __name__ == "__main__":
    serial = int(sys.stdin.read())

    power_levels = generate_power_levels(serial)

    print("Part 1:", solve(power_levels, 3))
    print("Part 2:", solve(power_levels, 20))
