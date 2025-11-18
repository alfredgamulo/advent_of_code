import re
import time as timer
from collections import defaultdict

start_time = timer.time()

# Create readable input
with open("input") as f:
    rules, messages = f.read().split("\n\n")
    rules = rules.splitlines()
    messages = messages.splitlines()

parsed = defaultdict(list)
for rule in rules:
    root, children = rule.split(":")
    for c in children.split():
        parsed[int(root)].append(c.strip('"'))


# Create the Rule tree
class Rule:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Rule(parsed[0])


def stuffit(root):
    options = root.val
    if len(options) == 1:
        if options[0] in ("a", "b"):
            root.val = options[0]
            return root
        else:
            return stuffit(Rule(parsed[int(options[0])]))
    if "|" in options:
        pipe = options.index("|")
        root.val = "|"
        root.left = stuffit(Rule(options[:pipe]))
        root.right = stuffit(Rule(options[pipe + 1 :]))
        return root
    if len(options) == 2:
        root.val = "and"
        root.left = stuffit(Rule(parsed[int(options[0])]))
        root.right = stuffit(Rule(parsed[int(options[1])]))
        return root
    if len(options) == 3:
        root.val = "and"
        root.left = stuffit(Rule(parsed[int(options[0])]))
        root.right = stuffit(Rule(options[1:]))
        return root


root = stuffit(root)


# Convert Rule tree to regex
def inorder(root, ra):
    if root:
        if root.left:
            ra.append("(")
        inorder(root.left, ra)
        if root.val == "and":
            pass
        else:
            ra.append(root.val)
        inorder(root.right, ra)
        if root.right:
            ra.append(")")


ra = []
inorder(root, ra)
rx = "^" + "".join(ra) + "$"
print(rx)
p = re.compile("".join(rx))
matches = [p.match(m) for m in messages]
print("Part 1:", len(list(filter(None, matches))))

print(f"--- {((timer.time() - start_time)*1000)} millis ---")
"""
Part 2: handle recursive rules 8 and 11
Rule 8: 42 | 42 8 => 42+
Rule 11: 42 31 | 42 11 31 => n times 42 followed by n times 31 (n>=1)
We'll build regex for rule 0 as: ^(42+)(42{n}31{n})$
"""

# Re-parse rules for part 2
parsed2 = defaultdict(list)
for rule in rules:
    root, children = rule.split(":")
    parsed2[int(root)] = [c.strip('"') for c in children.split()]

# Patch rules 8 and 11 for part 2
parsed2[8] = ["42", "|", "42", "8"]
parsed2[11] = ["42", "31", "|", "42", "11", "31"]

def build_regex(num, cache):
    if num in cache:
        return cache[num]
    rule = parsed2[num]
    if len(rule) == 1:
        if rule[0] in ("a", "b"):
            cache[num] = rule[0]
            return rule[0]
        else:
            return build_regex(int(rule[0]), cache)
    if "|" in rule:
        pipe = rule.index("|")
        left = build_regex_seq(rule[:pipe], cache)
        right = build_regex_seq(rule[pipe+1:], cache)
        out = f"(?:{left}|{right})"
        cache[num] = out
        return out
    else:
        out = build_regex_seq(rule, cache)
        cache[num] = out
        return out

def build_regex_seq(seq, cache):
    return "".join(build_regex(int(x), cache) for x in seq)

# Build regex for rules 42 and 31
cache = {}
rule_42 = build_regex(42, cache)
rule_31 = build_regex(31, cache)

# For rule 0: 8 11 => (42+)(42{n}31{n}) for n>=1
# We'll try n=1..10 (should be enough for input)
part2_regex = "^" + f"({rule_42})+" + "(" + "|".join([f"{rule_42}{{{n}}}{rule_31}{{{n}}}" for n in range(1, 10)]) + ")" + "$"

p2 = re.compile(part2_regex)
part2_matches = [p2.match(m) for m in messages]
print("Part 2:", len(list(filter(None, part2_matches))))
