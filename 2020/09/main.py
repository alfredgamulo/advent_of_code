with open("input") as f:
    cypher = list(map(int, f.readlines()))

pos = 25

# Part 1
part1 = -1
for c in cypher[pos:]:
    pre = set(cypher[pos-25:pos])
    if any([c-p in pre for p in pre]):
        pos += 1
        continue
    else:
        part1 = c
        break

print("Part 1:", part1)