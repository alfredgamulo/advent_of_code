import sys
import json

data = json.loads(sys.stdin.read().strip())


def dig(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        s = 0
        for v in data:
            s += dig(v)
        return s
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        s = 0
        for k, v in data.items():
            s += dig(v)
        return s
    return 0


print("Part 1:", dig(data))
