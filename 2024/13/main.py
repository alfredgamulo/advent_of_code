import copy
import os
import re
import string
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cache, cmp_to_key, reduce
from heapq import heappop, heappush
from io import StringIO
from itertools import (batched, chain, combinations, count, groupby,
                       permutations, product, zip_longest)
from math import ceil, floor, lcm, prod, sqrt
from pathlib import Path
from pprint import PrettyPrinter



def part1(lines):
    # Find how many prizes are winnable with 0..100 presses per button and
    # return the minimal token cost to win all possible prizes.
    blocks = parse_blocks(lines)
    total_tokens = 0
    winnable = 0
    for A, B, P in blocks:
        best = None
        Ax, Ay = A
        Bx, By = B
        Px, Py = P
        # brute-force within hint bounds 0..100
        for n in range(101):
            # compute required m from x equation if possible to prune
            # but simplest: iterate m as well
            for m in range(101):
                if Ax * n + Bx * m == Px and Ay * n + By * m == Py:
                    cost = 3 * n + m
                    if best is None or cost < best:
                        best = cost
        if best is not None:
            winnable += 1
            total_tokens += best
    return total_tokens


def part2(lines):
    # Part 2: prize coordinates have an added offset; find minimal token cost
    # (3*n + m) to win as many prizes as possible (no 100-press bound here).
    OFFSET = 10_000_000_000_000
    blocks = parse_blocks(lines)
    total_tokens = 0
    for A, B, P in blocks:
        Ax, Ay = A
        Bx, By = B
        Px, Py = (P[0] + OFFSET, P[1] + OFFSET)
        D = Ax * By - Ay * Bx
        from math import gcd

        if D != 0:
            n_num = Px * By - Bx * Py
            m_num = Ax * Py - Px * Ay
            if n_num % D != 0 or m_num % D != 0:
                continue
            n = n_num // D
            m = m_num // D
            if n >= 0 and m >= 0:
                total_tokens += 3 * n + m
            continue

        # Collinear case: need Px,Py collinear with A (or B)
        if Ax * Py - Ay * Px != 0:
            continue

        # Solve a*n + b*m = c using x-components (fallback to y if both zero)
        a = Ax
        b = Bx
        c = Px
        if a == 0 and b == 0:
            continue
        if a == 0:
            # need b*m = c
            if b == 0 or c % b != 0:
                continue
            m = c // b
            if m >= 0:
                total_tokens += m
            continue
        if b == 0:
            if c % a != 0:
                continue
            n = c // a
            if n >= 0:
                total_tokens += 3 * n
            continue

        g = gcd(a, b)
        if c % g != 0:
            continue

        # extended gcd
        def extgcd(x, y):
            if y == 0:
                return (1, 0, x)
            u, v, g2 = extgcd(y, x % y)
            return (v, u - (x // y) * v, g2)

        x0, y0, g2 = extgcd(a, b)
        mult = c // g2
        n0 = x0 * mult
        m0 = y0 * mult
        bg = b // g2
        ag = a // g2

        # t range for non-negativity
        if bg > 0:
            tmin = ceil((-n0) / bg)
        else:
            tmin = -10**30
        if ag > 0:
            tmax = floor(m0 / ag)
        else:
            tmax = 10**30
        if tmin > tmax:
            continue

        # minimize token cost = 3*(n0 + bg*t) + (m0 - ag*t) = base + coef * t
        base = 3 * n0 + m0
        coef = 3 * bg - ag
        if coef > 0:
            tbest = tmin
        elif coef < 0:
            tbest = tmax
        else:
            tbest = tmin

        n = n0 + bg * tbest
        m = m0 - ag * tbest
        if n < 0 or m < 0:
            continue
        total_tokens += 3 * n + m
    return total_tokens


def parse_blocks(lines):
    blocks = []
    cur = []
    for ln in lines:
        s = ln.strip()
        if not s:
            if cur:
                blocks.append(parse_block(cur))
                cur = []
            continue
        cur.append(s)
    if cur:
        blocks.append(parse_block(cur))
    return blocks


def parse_block(lines):
    # lines expected: Button A: X+ax, Y+ay  ; Button B: X+bx, Y+by ; Prize: X=px, Y=py
    def nums(s):
        return list(map(int, re.findall(r"-?\d+", s)))

    a = nums(lines[0])
    b = nums(lines[1])
    p = nums(lines[2])
    # For Button lines the order is ax, ay; for prize it's px, py
    Ax, Ay = a[0], a[1]
    Bx, By = b[0], b[1]
    Px, Py = p[0], p[1]
    return (Ax, Ay), (Bx, By), (Px, Py)


def has_solution(A, B, P):
    return minimal_presses(A, B, P) is not None


def minimal_presses(A, B, P):
    Ax, Ay = A
    Bx, By = B
    Px, Py = P
    D = Ax * By - Ay * Bx
    # helper for gcd
    from math import gcd

    if D != 0:
        # unique rational solution
        n_num = Px * By - Bx * Py
        m_num = Ax * Py - Px * Ay
        if n_num % D != 0 or m_num % D != 0:
            return None
        n = n_num // D
        m = m_num // D
        if n >= 0 and m >= 0:
            return n + m
        return None
    else:
        # collinear vectors: check if P is collinear too
        if Ax * Py - Ay * Px != 0:
            return None
        # reduce to single eq: Ax*n + Bx*m = Px (use x components if possible else y)
        a = Ax
        b = Bx
        c = Px
        if a == 0 and b == 0:
            return None
        if a == 0:
            # then need b*m = c
            if b == 0:
                return None
            if c % b != 0:
                return None
            m = c // b
            if m >= 0:
                return m
            return None
        if b == 0:
            if c % a != 0:
                return None
            n = c // a
            if n >= 0:
                return n
            return None

        g = gcd(a, b)
        if c % g != 0:
            return None
        # find one solution to a*n + b*m = c using extended gcd
        def extgcd(x, y):
            if y == 0:
                return (1, 0, x)
            u, v, g = extgcd(y, x % y)
            return (v, u - (x // y) * v, g)

        x0, y0, g2 = extgcd(a, b)
        # particular solution
        mult = c // g2
        n0 = x0 * mult
        m0 = y0 * mult
        # general solution: n = n0 + (b/g)*t, m = m0 - (a/g)*t
        bg = b // g2
        ag = a // g2

        # find t range so that n,m >=0
        # n >=0 => t >= ceil(-n0 / (b/g)) if b/g >0 else <=
        from math import ceil, floor

        if bg > 0:
            tmin = ceil((-n0) / bg)
        else:
            tmin = -10**18
        if ag > 0:
            tmax = floor(m0 / ag)
        else:
            tmax = 10**18

        if tmin > tmax:
            return None

        # minimize n+m = n0 + m0 + t*(b/g - a/g) = base + t*(bg - ag)
        base = n0 + m0
        coef = bg - ag
        # choose t in [tmin,tmax] that minimizes base + coef * t
        if coef > 0:
            tbest = tmin
        elif coef < 0:
            tbest = tmax
        else:
            # all t equal, pick any valid
            tbest = tmin

        n = n0 + bg * tbest
        m = m0 - ag * tbest
        if n < 0 or m < 0:
            return None
        return n + m


if __name__ == "__main__":
    lines = Path(sys.argv[1]).read_text().splitlines()
    print(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
