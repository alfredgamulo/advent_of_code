import sys
from math import floor, ceil, perm
from dataclasses import dataclass
from contextlib import suppress
from itertools import combinations, permutations


@dataclass()
class SnailFish:
    number: list

    def __add__(self, other):
        self = SnailFish([self.number, other.number])
        self.reduce()
        return self

    def __str__(self):
        return f"{self.number}"

    def explode(self):
        # find the explosion
        x = None
        y = None
        for i, a in enumerate(self.number):
            if isinstance(a, list):
                for j, b in enumerate(a):
                    if isinstance(b, list):
                        for k, c in enumerate(b):
                            if isinstance(c, list):
                                for l, d in enumerate(c):
                                    if isinstance(d, list):
                                        x, y = d
                                        break
                                else:
                                    continue
                                break
                        else:
                            continue
                        break
                else:
                    continue
                break

        if not x and not y:
            return

        pivot = (i << 3) + (j << 2) + (k << 1) + l

        # add the left:
        for p in range(pivot, -1, -1):
            n = p
            ll = n % 2
            n = n >> 1
            kk = n % 2
            n = n >> 1
            jj = n % 2
            n = n >> 1
            ii = n % 2
            with suppress(TypeError):
                if isinstance(self.number[ii][jj][kk][ll], int):
                    self.number[ii][jj][kk][ll] += x
                    break
            with suppress(TypeError):
                if isinstance(self.number[ii][jj][kk], int):
                    self.number[ii][jj][kk] += x
                    break
            with suppress(TypeError):
                if isinstance(self.number[ii][jj], int):
                    self.number[ii][jj] += x
                    break
            with suppress(TypeError):
                if isinstance(self.number[ii], int):
                    self.number[ii] += x
                    break

        # add the right:
        for p in range(pivot + 1, 16):
            try:
                n = p
                ll = n % 2
                n = n >> 1
                kk = n % 2
                n = n >> 1
                jj = n % 2
                n = n >> 1
                ii = n % 2
                if isinstance(self.number[ii], int):
                    self.number[ii] += y
                    break
                if isinstance(self.number[ii][jj], int):
                    self.number[ii][jj] += y
                    break
                if isinstance(self.number[ii][jj][kk], int):
                    self.number[ii][jj][kk] += y
                    break
                if isinstance(self.number[ii][jj][kk][ll], int):
                    self.number[ii][jj][kk][ll] += y
                    break
                if isinstance(self.number[ii][jj][kk][ll][0], int):
                    self.number[ii][jj][kk][ll][0] += y
                    break
            except:
                pass

        self.number[i][j][k][l] = 0
        return True

    def split(self):
        for i, a in enumerate(self.number):
            if isinstance(a, list):
                for j, b in enumerate(a):
                    if isinstance(b, list):
                        for k, c in enumerate(b):
                            if isinstance(c, list):
                                for l, d in enumerate(c):
                                    if isinstance(d, list):
                                        continue
                                    else:
                                        if d >= 10:
                                            self.number[i][j][k][l] = [
                                                floor(d / 2),
                                                ceil(d / 2),
                                            ]
                                            return True
                                else:
                                    continue
                                break
                            else:
                                if c >= 10:
                                    self.number[i][j][k] = [floor(c / 2), ceil(c / 2)]
                                    return True
                        else:
                            continue
                        break
                    else:
                        if b >= 10:
                            self.number[i][j] = [floor(b / 2), ceil(b / 2)]
                            return True
                else:
                    continue
                break
            else:
                if a >= 10:
                    self.number[i] = [floor(a / 2), ceil(a / 2)]
                    return True

    def reduce(self):
        while self.explode():
            continue
        if self.split():
            self.reduce()

    def magnitude(self):
        def tree_stuff(data):
            if isinstance(data, int):
                return data
            return 3*tree_stuff(data[0])+2*tree_stuff(data[1])
        return tree_stuff(self.number)


if __name__ == "__main__":
    lines = list(map(str.strip, sys.stdin.readlines()))

    sf = SnailFish(eval(lines[0]))
    for line in lines[1:]:
        sf += SnailFish(eval(line))
    print("Part 1:", sf.magnitude())

    part2 = 0
    for a, b in permutations(lines, 2):
        a = SnailFish(eval(a))
        b = SnailFish(eval(b))
        c = a + b
        m = c.magnitude()
        part2 = max(m, part2)

    print("Part 2:", part2)
