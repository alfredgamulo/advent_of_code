import time

start_time = time.time()

with open("input") as f:
    cypher = list(map(int, f.readlines()))

pos = 25

# Part 1
part1 = None
for c in cypher[pos:]:
    pre = set(cypher[pos - 25 : pos])
    if not any(c - p in pre for p in pre):
        part1 = (pos, c)
        break
    pos += 1

print("Part 1:", part1[1])

# Part 2
hi = part1[0] - 1
lo = part1[0] - 2
t = part1[1]
while lo > 0 and hi > 0:
    r = cypher[lo:hi]
    s = sum(r)
    if s == t:
        print("Part 2:", min(r) + max(r))
        break
    if s < t:
        lo -= 1
    else:
        hi -= 1

print("--- %s seconds ---" % (time.time() - start_time))
