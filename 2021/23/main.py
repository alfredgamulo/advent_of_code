import sys
from rich.console import Console
import os

console = Console()

game = [[c for c in l.strip("\n")] for l in list(sys.stdin.readlines())]
sys.stdin.close()
sys.stdin = os.fdopen(1)

score = 0
selector = (-1, -1)
selected = ""

point_map = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

def set_selector(ch):
    global selector
    global selected
    for i in range(selector[0],len(game)):
        for j in range(0,len(game[i])):
            if i == selector[0] and j < selector[1]:
                continue
            if game[i][j] == ch.upper() and (i, j) != selector:
                selector = (i, j)
                selected = game[i][j]
                return
    for i, line in enumerate(game):
        for j, char in enumerate(line):
            if char == ch.upper() and (i, j) != selector:
                selector = (i, j)
                selected = game[i][j]
                return

while True:
    console.clear()
    for i, line in enumerate(game):
        for j, char in enumerate(line):
            if i == selector[0] and j == selector[1]:
                console.print(char, style="bold red", end="")    
            else:
                console.print(char, end="")
        console.print()
    console.print()
    console.print(f"Selector: {selector}")
    console.print(f"Selected: {selected}")
    console.print(f"Score: {score}")
    # ch = console.input("Select a letter [A/B/C/D], or direction \[up/down/left/right]. Press q to quit:")
    ch = console.input("Input:")
    move = False
    match ch:
        case "a" | "b" | "c" | "d" :
            set_selector(ch)
        case "\033[D":
            move = (0, -1)
        case "\033[A":
            move = (-1, 0)
        case "\033[B":
            move = (1, 0)
        case "\033[C":
            move = (0, 1)
        case "q":
            break
    if move:
        if selected == "":
            continue
        game[selector[0]][selector[1]] = "."
        selector = (selector[0] + move[0], selector[1] + move[1])
        game[selector[0]][selector[1]] = selected
        score += point_map[selected]
         

