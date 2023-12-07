import sys
from collections import Counter
from functools import cmp_to_key


def val(left, right):
    return (left - right) // abs(left - right)


def cmp(left, lcount, right, rcount, order):
    if len(lcount) == len(rcount):
        if lcount.most_common()[0][1] == rcount.most_common()[0][1]:
            for lchar, rchar in zip(left, right):
                if lchar != rchar:
                    return val(order.index(rchar), order.index(lchar))
        return val(lcount.most_common()[0][1], rcount.most_common()[0][1])
    return val(len(rcount), len(lcount))


def cmp_wrapper1(left, right):
    left, right = left.split()[0], right.split()[0]
    return cmp(left, Counter(left), right, Counter(right), "AKQJT98765432")


def cmp_wrapper2(left, right):
    left, right = left.split()[0], right.split()[0]
    lcount, rcount = Counter(left.replace("J", "")), Counter(right.replace("J", ""))
    if lcount:
        lcount[lcount.most_common(1)[0][0]] += left.count("J")
    else:  # all J
        lcount = Counter(left)
    if rcount:
        rcount[rcount.most_common(1)[0][0]] += right.count("J")
    else:  # all J
        rcount = Counter(right)
    return cmp(left, lcount, right, rcount, "AKQT98765432J")


def solve(lines, cmp):
    return sum(
        rank * int(line.split()[1])
        for rank, line in enumerate(sorted(lines, key=cmp_to_key(cmp)), 1)
    )


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    print("Part 1:", solve(lines, cmp_wrapper1))
    print("Part 2:", solve(lines, cmp_wrapper2))
