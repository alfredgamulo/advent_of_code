import sys

input = sys.argv[1]

# Create readable input
with open(input) as f:
    section1, section2 = f.read().split("\n\n")
    section1 = section1.splitlines()
    section2 = section2.splitlines()

# Looping through cases
with open(input) as f:
    lines = f.read().splitlines()
