f = open("input")

seat_ids = []

for line in f.read().splitlines():
    bs = "".join(["0" if l in ("F", "L") else "1" for l in line])
    val = int(bs, 2)
    seat_ids.append(val)

seat_ids.sort()

# part 1
print(seat_ids[-1])

# part 2
offset = seat_ids[0]
for i, s in enumerate(seat_ids):
    if i != s-offset:
        print(s-1)
        break