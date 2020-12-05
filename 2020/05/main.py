f = open("input")

seat_ids = []

for line in f.read().splitlines():
    rows = line[:7]
    cols = line[7:]
    
    row_range = list(range(128))
    col_range = list(range(8))

    for r in rows:
        index = len(row_range) // 2
        row_range = row_range[:index] if r == "F" else row_range[index:]
    
    for c in cols:
        index = len(col_range) // 2
        col_range = col_range[:index] if c == "L" else col_range[index:]
    
    val = row_range[0]*8+col_range[0]
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