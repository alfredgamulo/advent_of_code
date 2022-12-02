import sys

hand_values = {"A": 1, "B": 2, "C": 3}

round_score = {
    ("A", "A"): 3,
    ("A", "B"): 6,
    ("A", "C"): 0,
    ("B", "A"): 0,
    ("B", "B"): 3,
    ("B", "C"): 6,
    ("C", "A"): 6,
    ("C", "B"): 0,
    ("C", "C"): 3,
}


def play(rounds):
    decrypt1 = {"X": "A", "Y": "B", "Z": "C"}
    decrypt2 = {
        ("A", "X"): "C",
        ("A", "Y"): "A",
        ("A", "Z"): "B",
        ("B", "X"): "A",
        ("B", "Y"): "B",
        ("B", "Z"): "C",
        ("C", "X"): "B",
        ("C", "Y"): "C",
        ("C", "Z"): "A",
    }
    score1 = 0
    score2 = 0
    for (opp, me) in rounds:
        me1 = decrypt1[me]
        me2 = decrypt2[(opp, me)]
        score1 += round_score[(opp, me1)] + hand_values[me1]
        score2 += round_score[(opp, me2)] + hand_values[me2]
    print("Part 1:", score1)
    print("Part 2:", score2)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    rounds = [r.strip().split(" ") for r in lines]

    play(rounds)
