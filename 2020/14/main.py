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
            mask = line.split('=')[1].strip()

            # Part 1:
            mask_1 = sum([2**i for i,x in enumerate(mask[::-1]) if x == "1"])
            mask_0 = sum([2**i for i,x in enumerate(mask[::-1]) if x == "0"])
            # Part 2:
            mask_x = [2**i for i,x in enumerate(mask[::-1]) if x == "X"]
        else:
            nums = list(map(int,re.findall(r'\d+', line)))
            mem = nums[0]
            val = nums[1]

            # Part 1:
            result = val | mask_1 # apply mask 1
            result = (result | mask_0) - mask_0 # apply mask 0
            memory1[mem] = result

            # Part 2:
            mem_0 = mem | mask_1
            mems = [mem_0]
            for x in mask_x:
                mems.extend(list(m ^ x for m in mems))
            for m in mems:
                memory2[m] = val

print("Part 1:", sum(memory1.values()))
print("Part 2:", sum(memory2.values()))
print("--- %s millis ---" % ((timer.time() - start_time)*1000))