import sys
from pathlib import Path

if __name__ == "__main__":
    sections = Path(sys.argv[1]).read_text().split("\n\n")
    rules = list(map(lambda x: x.split("|"), sections[0].splitlines()))
    updates = sections[1].splitlines()

    wrongs = []
    middles = 0
    for update in updates:
        valid = True
        for rule in rules:
            try:
                if update.index(rule[0]) < update.index(rule[1]):
                    continue
                else:
                    valid = False
                    break
            except:
                continue
        update = update.split(",")
        if valid:
            middles += int(update[len(update) // 2])
        else:
            wrongs.append(update)

    print("Part 1:", middles)

    middles = 0
    for update in wrongs:
        check_again = True
        while check_again:
            check_again = False
            for rule in rules:
                try:
                    if update.index(rule[0]) < update.index(rule[1]):
                        continue
                    else:
                        swp = update[update.index(rule[0])]
                        update[update.index(rule[0])] = update[update.index(rule[1])]
                        update[update.index(rule[1])] = swp
                        check_again = True
                        break
                except ValueError:
                    continue
        middles += int(update[len(update) // 2])

    print("Part 2:", middles)
