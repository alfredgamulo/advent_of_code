import time as timer

start_time = timer.time()

from functools import reduce
from itertools import combinations

with open("input") as f:
    time = int(f.readline().strip())
    buses = [
        (i, int(b)) for i, b in enumerate(f.readline().strip().split(",")) if b != "x"
    ]

print(buses)

times = {}
for _, b in buses:
    m = time // b
    times[b] = b * m + b

key_min = min(times.keys(), key=(lambda k: times[k]))

print("Part 1:", key_min * (times[key_min] - time))

# Use Chinese Remainder Theorem: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


# A shortcut for this: `mod_inverse = pow(div, -1, t)`
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


n = [b[1] for b in buses]  # bus IDs
a = [b[1] - b[0] for b in buses]  # remainders

print("Part 2:", chinese_remainder(n, a))

print("--- %s millis ---" % ((timer.time() - start_time) * 1000))
