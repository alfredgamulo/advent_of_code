import time as timer

start_time = timer.time()

from collections import defaultdict
import re

# Part 1:
memory1 = defaultdict(int)
mask_1 = None
mask_0 = None
# Part 2:
memory2 = defaultdict(int)
mask_x = None

with open("input") as f:
    for line in f.readlines():
        if line.startswith("mask"):
            mask = [(i, x) for i, x in enumerate(line.split("=")[1].strip()[::-1])]
            # Part 1:
            mask_1 = sum([2 ** i for i, x in mask if x == "1"])
            mask_0 = sum([2 ** i for i, x in mask if x == "0"])
            # Part 2:
            mask_x = [2 ** i for i, x in mask if x == "X"]
        else:
            mem, val = tuple(map(int, re.findall(r"\d+", line)))
            # Part 1:
            memory1[mem] = ((val | mask_1) | mask_0) - mask_0
            # Part 2:
            mems = [mem | mask_1]
            for x in mask_x:
                mems.extend(list(m ^ x for m in mems))
            for m in mems:
                memory2[m] = val

print("Part 1:", sum(memory1.values()))
print("Part 2:", sum(memory2.values()))
print("--- %s millis ---" % ((timer.time() - start_time) * 1000))
