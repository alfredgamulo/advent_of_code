import sys

lines = sys.stdin.readlines()

flights = dict()
for line in lines:
    name, _, _, speed, _, _, duration, *_, rest, _ = line.split()
    flights[name] = (int(speed), int(duration), int(rest))

distance = -1
for reindeer, stats in flights.items():
    i, m = divmod(2503, (stats[1] + stats[2]))
    t = min(stats[1], m)
    d = (i * stats[1] + t) * stats[0]
    distance = max(distance, d)

print("Part 1:", distance)
