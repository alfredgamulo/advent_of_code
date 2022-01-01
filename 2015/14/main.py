import sys
from collections import defaultdict

lines = sys.stdin.readlines()

reindeer = dict()
for line in lines:
    name, _, _, speed, _, _, duration, *_, rest, _ = line.split()
    reindeer[name] = (int(speed), int(duration), int(rest))

distance = -1
for stats in reindeer.values():
    i, m = divmod(2503, (stats[1] + stats[2]))
    t = min(stats[1], m)
    d = (i * stats[1] + t) * stats[0]
    distance = max(distance, d)

print("Part 1:", distance)

race = defaultdict(dict)
lead = -1
top = 0
for t in range(2503):
    for r, stats in reindeer.items():
        if r not in race:
            race[r] = defaultdict(int)
        d, m = divmod(t, stats[1] + stats[2])
        if t < stats[1] or (d and m < stats[1]):
            race[r]["distance"] += stats[0]
        lead = max(lead, race[r]["distance"])
    for r in race:
        if race[r]["distance"] == lead:
            race[r]["score"] += 1
            top = max(top, race[r]["score"])

print("Part 2:", top)
