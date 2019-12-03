rule = {
    "rock": {"rock": "draw",
             "paper": "Player2 wins",
             "scissor": "Player1 wins"},
    "paper": {"rock": "Player1 wins",
              "paper": "draw",
              "scissor": "Player2 wins"},
    "scissor": {"rock": "Player2 wins",
                "paper": "draw",
                "scissor": "Player1 wins"}
}

play = True

while play:
    ply1 = input(">> ")
    ply2 = input(">> ")
    print(rule[ply1][ply2])
    if (ply1 or ply2) == 'stop':
        play = False