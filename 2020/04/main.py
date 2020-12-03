import re

data = [{}]

with open("input") as f:
    for line in f.read().splitlines():
        if line == '':
            data.append({})
        data[-1].update((dict(s.split(':') for s in line.split())))

def validate_byr(s):
    try:
        return 1920 <= int(s) <= 2002
    except:
        pass
    return False

def validate_iyr(s):
    try:
        return 2010 <= int(s) <= 2020
    except:
        pass
    return False
        
def validate_eyr(s):
    try:
        return 2020 <= int(s) <= 2030
    except:
        pass
    return False
    
def validate_hgt(s):
    num = s.rstrip("cmin")
    try:
        if "in" in s:
            return 59 <= int(num) <= 76
        elif "cm" in s:
            return 150 <= int(num) <= 193 
    except:
        pass
    return False
    
def validate_hcl(s):
    try:
        return bool(re.match('^#([a-fA-F0-9]{6})$', s))
    except:
        pass
    return False
    
def validate_ecl(s):
    try:
        return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    except:
        pass
    return False
    
def validate_pid(s):
    try:
        return bool(re.match('^([0-9]{9})$', s))
    except:
        pass
    return False
    
required = {
    "byr": validate_byr,
    "iyr": validate_iyr,
    "eyr": validate_eyr,
    "hgt": validate_hgt,
    "hcl": validate_hcl,
    "ecl": validate_ecl,
    "pid": validate_pid
    }

optional = [
    "cid"
    ]

rkeys = list(required.keys())

part1 = 0
part2 = 0

for d in data:
    key_helper1 = [False]*len(required)
    key_helper2 = [False]*len(required)
    for k in d.keys():
        if k in rkeys:
            key_helper1[rkeys.index(k)] = True
            key_helper2[rkeys.index(k)] = required.get(k)(d.get(k))
    if all(key_helper1):
        part1 += 1
    if all(key_helper2):
        part2 += 1

print(part1)
print(part2)
