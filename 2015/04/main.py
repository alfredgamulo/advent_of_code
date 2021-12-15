import sys
import hashlib
from concurrent import futures

key = sys.stdin.readline().strip()


def mine(match):
    num = 0
    while True:
        md5 = hashlib.md5((key + str(num)).encode()).hexdigest()
        if md5[: len(match)] == match:
            break
        num += 1
    return num


print("Part 1:", mine("00000"))
print("Part 2:", mine("000000"))
