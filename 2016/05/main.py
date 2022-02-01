import hashlib
import sys

door_id = sys.stdin.read().strip()


def part1():
    num = 0
    password = ""
    while len(password) < 8:
        md5 = hashlib.md5((door_id + str(num)).encode()).hexdigest()
        if md5[:5] == "00000":
            password += md5[5]
        num += 1
    return password


print("Part 1:", part1())


def part2():
    num = 0
    password = [0, 0, 0, 0, 0, 0, 0, 0]
    while not all(password):
        md5 = hashlib.md5((door_id + str(num)).encode()).hexdigest()
        try:
            if md5[:5] == "00000" and not password[int(md5[5])]:
                password[int(md5[5])] = md5[6]
        except Exception:
            pass
        num += 1
    return "".join(password)


print("Part 2:", part2())
