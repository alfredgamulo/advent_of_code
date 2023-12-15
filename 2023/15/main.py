import re
import sys
from collections import OrderedDict, defaultdict
from contextlib import suppress
from functools import cache, reduce
from pathlib import Path


@cache
def hash(characters):
    return reduce(lambda current, c: (current + ord(c)) * 17 % 256, characters, 0)


def part1(sequence):
    return sum(hash(s) for s in sequence)


def part2(sequence):
    boxes = defaultdict(OrderedDict)
    for label, lens in map(lambda s: re.split("=|-", s), sequence):
        box = hash(label)
        with suppress(ValueError):
            boxes[box][label] = int(lens)
            continue
        with suppress(KeyError):
            del boxes[box][label]

    return sum(
        (box + 1) * slot * length
        for box, lenses in boxes.items()
        for slot, (_, length) in enumerate(lenses.items(), 1)
    )


if __name__ == "__main__":
    sequence = Path(sys.argv[1]).read_text().strip().split(",")
    print("Part 1:", part1(sequence))
    print("Part 2:", part2(sequence))