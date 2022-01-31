import re
import sys
from itertools import groupby

information = sys.stdin.readlines()


def decrypt(e, n):
    p = ""
    for c in e:
        if c == "-":
            p += " "
            continue
        p += chr((((ord(c) - 97) + n) % 26) + 97)
    return p


def part1():
    sum = 0
    for data in information:
        data = re.split("(\d+)", data.strip())
        encrypted_name = data[0][:-1]
        number = int(data[1])

        occurrences = []
        for k, v in groupby([char for char in sorted(encrypted_name) if char != "-"]):
            occurrences.append((k, len(list(v))))
        sorted_occurrences = sorted(occurrences, key=lambda x: x[1], reverse=True)
        checksum = "".join([char for char, _ in sorted_occurrences[:5]])
        if checksum == data[2][1:-1]:
            sum += number
            decrypted = decrypt(encrypted_name, number)
            if "north" in decrypted:
                print("Part 2:", number)
    return sum


print("Part 1:", part1())
