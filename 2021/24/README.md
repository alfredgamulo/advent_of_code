Input:

| 1|2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |13 |14 |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w | inp w |
| mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 | mul x 0 |
| add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z | add x z |
| mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 | mod x 26 |
| `div z 1` | `div z 1` | `div z 1` | `div z 1` | `div z 26` | `div z 1` | `div z 1` | `div z 26` | `div z 1` | `div z 26` | `div z 26` | `div z 26` | `div z 26` | `div z 26` |
| `add x 15` | `add x 11` | `add x 10` | `add x 12` | `add x -11` | `add x 11` | `add x 14` | `add x -6` | `add x 10` | `add x -6` | `add x -6` | `add x -16` | `add x -4` | `add x -2` |
| eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w | eql x w |
| eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 | eql x 0 |
| mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 |
| add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 | add y 25 |
| mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x |
| add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 | add y 1 |
| mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y | mul z y |
| mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 | mul y 0 |
| add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w | add y w |
| `add y 9` | `add y 1` | `add y 11` | `add y 3` | `add y 10` | `add y 5` | `add y 0` | `add y 7` | `add y 9` | `add y 15` | `add y 4` | `add y 10` | `add y 4` | `add y 9` |
| mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x | mul y x |
| add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y | add z y |

The entire input is in the form repeated 14 times:
```
inp w
mul x 0
add x z
mod x 26
div z {a}
add x {b}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {c}
mul y x
add z y
```

Each of the 14 subroutines can be decompiled as Python in the following form:

```
w = int(input())
x = int((z % 26) + b != w)
z //= a
z *= 25*x+1
z += (w+c)*x
```

The values for `a` is `1` seven times and `26` for the other seven times. In the blocks where `a` is `1`, `b` is always between `10` and `16`. When `a` is `1`,  then the `z //=a` step is a no-op and `(z % 26) + b != w` is always true. So the decompiled Python can be simplified further:

```
w = int(input())
z *= 26
z += w+c
```