with open("input") as f:
    seat_ids = set(
        int("".join(["0" if l in ("F", "L") else "1" for l in line]), 2)
        for line in f.read().splitlines()
    )

high = max(seat_ids)
print(high)
miss = next(s for s in range(high, 0, -1) if s not in seat_ids)
print(miss)
