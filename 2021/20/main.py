import sys
from itertools import product
from pprint import PrettyPrinter
from itertools import chain

pp = PrettyPrinter(indent=2)

algorithm, image = sys.stdin.read().split("\n\n")
algorithm = algorithm.strip()

image = [list(s) for s in image.strip().split()]


def enhance(image, steps):
    for s in range(1, steps + 1):
        print(s, flush=True)
        output = []
        for i in range(0 - s, len(image) + s):
            line = []
            for j in range(0 - s, len(image[0]) + s):
                lookup = ""
                for x, y in product((-1, 0, 1), (-1, 0, 1)):
                    try:
                        if (
                            i + x >= 0
                            and i + x <= len(image)
                            and (j + y >= 0 and j + y <= len(image[0]))
                        ):
                            lookup += image[i + x][j + y]
                        else:
                            lookup += (
                                "#" if ((algorithm[0] == "#") and s % 2 == 0) else "."
                            )
                    except IndexError:
                        lookup += "#" if ((algorithm[0] == "#") and s % 2 == 0) else "."

                line.append(
                    algorithm[
                        int("".join(["1" if l == "#" else "0" for l in lookup]), 2)
                    ]
                )
            output.append(line)
        image = output
    return sum(c == "#" for c in chain.from_iterable(image))


# print("Part 1:", enhance(image, 2))
print("Part 2:", enhance(image, 50))
