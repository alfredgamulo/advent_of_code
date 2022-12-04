import re
import sys

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    count1 = 0
    count2 = 0
    for line in lines:
        x1, x2, y1, y2 = map(int, re.split("-|,", line))
        count1 += (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2)
        count2 += x1 <= y2 and y1 <= x2

    print("Part 1:", count1)
    print("Part 2:", count2)
