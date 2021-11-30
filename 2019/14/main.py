def read_input(file):
    formulas = {}
    with open(file) as f:
        for r in f.readlines():
            left, right = map(str.strip, r.split("=>"))
            left = list(map(str.strip, left.split(",")))
            right = right.split(" ")
            formulas[right[1]] = ()
            formulas[right[1]] = (
                int(right[0]),
                {l.split(" ")[1]: int(l.split(" ")[0]) for l in left},
            )

    return formulas


def main(fuel):
    formulas = read_input("input")
    demand = {"FUEL": fuel}
    supply = {}
    while True:
        try:
            d = next(d for d in demand if d != "ORE")
        except Exception:
            return demand

        amount, materials = formulas[d]

        div, mod = divmod(demand[d], amount)
        if mod:
            supply[d] = amount - mod
            div += 1
        del demand[d]

        for k, v in materials.items():
            demand[k] = demand.get(k, 0) + div * v - supply.get(k, 0)
            if k in supply:
                del supply[k]


print("Part 1:", main(1))  # >>> 371695

print("Part 2:", main(4052920))
