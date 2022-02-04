import re
import sys
from itertools import groupby

addresses = list(map(str.strip, sys.stdin.readlines()))


def abba(s):
    groups = [(k, len(list(v))) for k, v in groupby(s)]
    for i, v in enumerate(groups):
        if (
            v[1] == 2
            and i > 0
            and i < len(groups) - 1
            and groups[i - 1][0] != v[0]
            and groups[i + 1][0] != v[0]
            and groups[i - 1][0] == groups[i + 1][0]
        ):
            return True
    return False


def tls(sequences):
    yes = sequences[::2]
    nos = sequences[1::2]
    return any(filter(abba, yes)) and not any(filter(abba, nos))


def aba(s):
    found = []
    for i, v in enumerate(s):
        if i > 0 and i < len(s) - 1 and s[i - 1] != v and s[i - 1] == s[i + 1]:
            found.append(s[i - 1 : i + 2])
    return found


def ssl(sequences):
    yes = sequences[::2]
    nos = sequences[1::2]
    abas = []
    for y in yes:
        abas.extend(aba(y))
    if not abas:
        return False
    for each in abas:
        bab = "".join([each[1], each[0], each[1]])
        for n in nos:
            if bab in n:
                return True


part1 = 0
part2 = 0
for ip in addresses:
    sequences = re.split("\[|\]", ip)
    if tls(sequences):
        part1 += 1
    if ssl(sequences):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
