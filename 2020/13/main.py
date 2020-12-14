import time as timer
start_time = timer.time()
from itertools import combinations

with open("input") as f:
    time = int(f.readline().strip())
    buses = [(i, int(b)) for i, b in enumerate(f.readline().strip().split(',')) if b != "x"]

times = {}
for _,b in buses:
    m = time // b
    times[b]=(b*m+b)

key_min = min(times.keys(), key=(lambda k: times[k]))

print("Part 1:", key_min*(times[key_min]-time))

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

# find bus a time that matches bus b offset
bus_a = None
bus_b = None
for a, b in combinations(buses, 2):
    if a[1] == b[0]:
        bus_a = a
        bus_b = b
        break

magic_number = bus_a[1]*bus_b[1]

# use LCM as upper limit
l = buses[0][1]
for _,b in buses[1:]:
    l = lcm(l, b)

# reindex busses to the common multiple
buses = [(bus[0]-bus_b[0], bus[1]) for bus in buses]

for i in range(magic_number//100000000000000, l, magic_number):
    found = True
    for k, b in buses:
        if (i+k) % b == 0:
            continue
        else:
            found = False
            break
    if found:
        print("Part 2:", i-bus_a[1])
        break

print("--- %s millis ---" % ((timer.time() - start_time)*1000))