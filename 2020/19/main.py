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
