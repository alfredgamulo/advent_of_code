import math
import re
import sys
from dataclasses import dataclass


@dataclass
class Monkey:
    id: int
    items: list
    operation: str
    test: int
    test_t: int
    test_f: int
    inspects: int = 0

    def __lt__(self, other):
        return self.inspects < other.inspects


def parse(monkeys):
    monkey_list = []
    for monkey in monkeys:
        details = monkey.splitlines()
        id = re.findall("\\d", details[0])
        items = list(map(int, re.findall("\\d{1,2}", details[1])))
        operation = details[2][13:]
        test = int(details[3].split()[-1])
        test_t = int(details[4].split()[-1])
        test_f = int(details[5].split()[-1])
        monkey_list.append(Monkey(id, items, operation, test, test_t, test_f))
    return monkey_list


def solve(monkeys, rounds, relief=None):
    monkeys = parse(monkeys)
    if relief:
        reduce = f"val // {relief}"
    else:
        mod = math.prod(m.test for m in monkeys)
        reduce = f"val % {mod}"
    for _ in range(rounds):
        for m in monkeys:
            while m.items:
                item = m.items.pop(0)
                m.inspects += 1
                namespace = {"new": None, "old": item}
                exec(m.operation, namespace)
                worry = eval(reduce, {"val": namespace["new"]})
                n = m.test_t if ((worry % m.test) == 0) else m.test_f
                monkeys[n].items.append(worry)

    return math.prod(m.inspects for m in sorted(monkeys)[-2:])


if __name__ == "__main__":
    monkeys = sys.stdin.read().split("\n\n")

    print("Part 1:", solve(monkeys, 20, 3))
    print("Part 2:", solve(monkeys, 10000))
