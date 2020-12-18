import time as timer
start_time = timer.time()
from collections import defaultdict
from functools import reduce
import re

# Parse
with open("input") as f:
    fields, my_ticket, nearby_tickets = f.read().split("\n\n")

functions = []
for field in fields.splitlines():
    field_name, rules = field.split(':')
    field_name = "custom_"+"_".join(field_name.split())
    a, b, c, d = tuple(map(int,re.findall(r'\d+', rules)))
    exec(f'def {field_name}(x):\n\treturn {a}<=x<={b} or {c}<=x<={d}')
    functions.append(field_name)

my_ticket = list(map(int, my_ticket.splitlines()[1].strip().split(',')))

nearby_tickets = [list(map(int,n.split(','))) for n in nearby_tickets.splitlines()[1:]]

# Part 1
part1 = 0
good_tickets = []
for t in nearby_tickets:
    discard = False
    for n in t:
        if not any([globals()[f](n) for f in functions]):
            part1 += n
            discard = True
            break
    if not discard:
        good_tickets.append(t)

print("Part 1:", part1)

# Part 2
possible_fields = defaultdict(list)
x_len = len(good_tickets)
y_len = len(good_tickets[0])

for f in functions:
    for y in range(y_len):
        column = list(good_tickets[x][y] for x in range(x_len))
        if all([globals()[f](n) for n in column]):
            possible_fields[f].append(y)

good_fields = {}

while len(good_fields) < len(functions):
    c = None
    for f in functions:
        if len(possible_fields[f]) == 1:
            c = possible_fields[f][0]
            good_fields[f] = c
            break
    for f in possible_fields:
        try:
            possible_fields[f].remove(c)
        except ValueError:
            pass

part2 = reduce(lambda a, b: a*b, [my_ticket[v] for f,v in good_fields.items() if "departure" in f])
print("Part 2:", part2)

print("--- %s millis ---" % ((timer.time() - start_time)*1000))
