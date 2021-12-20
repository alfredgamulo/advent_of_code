import sys
from collections import defaultdict
from pprint import PrettyPrinter
from itertools import combinations, permutations

pp = PrettyPrinter(indent=2)

# Ingest the information
lines = sys.stdin.read().split("\n\n")
scanner_data = defaultdict(dict)
for i, line in enumerate(lines):
    data = line.strip().split("\n")
    for j, probes in enumerate(data[1:]):
        scanner_data[i][j] = tuple(map(int, probes.split(",")))
# Don't touch ^
# pp.pprint(scanner_data)


"""

z   y
|  /
| /
|/_____ x

y   -z
|  /
| /
|/_____ x

-z   -y
|  /
| /
|/_____ x

-y  z
|  /
| /
|/_____ x

*

z   -y
|  /
| /
|/_____ -x

-y   -z
|  /
| /
|/_____ -x

-z   y
|  /
| /
|/_____ -x

y   z
|  /
| /
|/_____ -x

* 

z   -x
|  /
| /
|/_____ y

-x   -z
|  /
| /
|/_____ y

-z   x
|  /
| /
|/_____ y

x   z
|  /
| /
|/_____ y

*

z   x
|  /
| /
|/_____ -y

x   -z
|  /
| /
|/_____ -y

-z   -x
|  /
| /
|/_____ -y

-x   z
|  /
| /
|/_____ -y

*

-x   y
|  /
| /
|/_____ z

y   x
|  /
| /
|/_____ z

x   -y
|  /
| /
|/_____ z

-y  -x
|  /
| /
|/_____ z

*

-y  x
|  /
| /
|/_____ -z

x  y
|  /
| /
|/_____ -z

y  -x
|  /
| /
|/_____ -z

-x  -y
|  /
| /
|/_____ -z

"""

rotation_options = {
    0: lambda x, y, z: (x, y, z),
    1: lambda x, y, z: (x, -z, y),
    2: lambda x, y, z: (x, -y, -z),
    3: lambda x, y, z: (x, z, -y),
    4: lambda x, y, z: (-x, -y, z),
    5: lambda x, y, z: (-x, -z, -y),
    6: lambda x, y, z: (-x, y, -z),
    7: lambda x, y, z: (-x, z, y),
    8: lambda x, y, z: (y, -x, z),
    9: lambda x, y, z: (y, -z, -x),
    10: lambda x, y, z: (y, x, -z),
    11: lambda x, y, z: (y, z, x),
    12: lambda x, y, z: (-y, x, z),
    13: lambda x, y, z: (-y, -z, x),
    14: lambda x, y, z: (-y, -x, -z),
    15: lambda x, y, z: (-y, z, -x),
    16: lambda x, y, z: (z, y, -x),
    17: lambda x, y, z: (z, x, y),
    18: lambda x, y, z: (z, -y, x),
    19: lambda x, y, z: (z, -x, -y),
    20: lambda x, y, z: (-z, x, -y),
    21: lambda x, y, z: (-z, y, x),
    22: lambda x, y, z: (-z, -x, y),
    23: lambda x, y, z: (-z, -y, -x),
}

def find_scanner_match(scanner1, scanner2):
    print(scanner1, scanner2)
    for o in rotation_options:
        x_diff_counter = defaultdict(int)
        y_diff_counter = defaultdict(int)
        z_diff_counter = defaultdict(int)
        for a, p in scanner_data[scanner1].items():
            for b, q in scanner_data[scanner2].items():
                x, y, z = rotation_options[0](q[0],q[1],q[2])
                x_diff_counter[p[0]-x] += 1
                y_diff_counter[p[1]-y] += 1
                z_diff_counter[p[2]-z] += 1
        if max(x_diff_counter.values()) >= 12 and max(y_diff_counter.values()) >= 12 and max(z_diff_counter.values()) >= 12:
            print("!!!!!!!!!!!!")
            return (scanner1, scanner2, o)

print(find_scanner_match(0,1))

# for i in range(0, len(scanner_data)):
#     print(find_scanner_match(0,i))


