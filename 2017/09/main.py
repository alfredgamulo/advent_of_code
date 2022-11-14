import sys

if __name__ == "__main__":
    character = (c for c in sys.stdin.readline())
    score = 0
    total = 0
    garbage = False
    gcount = 0
    for c in character:
        match (c):
            case "{":
                if not garbage:
                    score += 1
                else:
                    gcount += 1
            case "<":
                if not garbage:
                    garbage = True
                else:
                    gcount += 1
            case ">":
                garbage = False
            case "}":
                if not garbage:
                    total += score
                    score -= 1
                else:
                    gcount += 1
            case _:
                if garbage:
                    gcount += 1

    print(total, gcount)
