import re

data = [{}]

with open("input") as f:
    for line in f.read().splitlines():
        if line == '':
            data.append({})
        data[-1].update((dict(s.split(':') for s in line.split())))

    
required = {
    "byr": lambda s: 1920 <= int(s) <= 2002 if s.isdigit() else False,
    "iyr": lambda s: 2010 <= int(s) <= 2020 if s.isdigit() else False,
    "eyr": lambda s: 2020 <= int(s) <= 2030 if s.isdigit() else False,
    "hgt": lambda s: (59 <= int(s.rstrip("cmin")) <= 76, 150 <= int(s.rstrip("cmin")) <= 193)["cm" in s] if "in" in s or "cm" in s else False,
    "hcl": lambda s: bool(re.match('^#([a-fA-F0-9]{6})$', s)),
    "ecl": lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda s: bool(re.match('^([0-9]{9})$', s))
    }

part1 = 0
part2 = 0

for d in data:
    d.pop("cid", None)
    
    if set(required.keys()) == (set(d.keys())):
        part1 += 1
    else:
        continue

    if all([required.get(k)(d.get(k)) for k in d.keys()]):
        part2 += 1

print(part1)
print(part2)
