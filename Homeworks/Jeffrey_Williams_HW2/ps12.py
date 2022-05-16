# Problem Set 2
# Name: Jeffrey Williams
# Time Spent: 2:00
# Last Modified: Oct 13, 2021

# Variables to record / maintain scores and round number, all increase by 1 when appropriate
round = 0
p1_score = 0
p2_score = 0
tie_score = 0

# Pre-written strings to announce results of a round
p1_winround = str("Player 1 wins this round!")
p2_winround = str("Player 2 wins this round!")
tieround = str("Players 1 and 2 are tied for this round!")

# Code executes for as long as 5 rounds have not been reached
while round < 5:
    # Requests input from the user (rock, paper, or scissors)
    p1_input = str.lower(input("Player 1, what do you pick?"))
    p2_input = str.lower(input("Player 2, what do you pick?"))

    # Player 1 earns a point and is declared round winner if one of three outcomes are achieved
    if (p1_input == "rock" and p2_input == "scissors") or (p1_input == "paper" and p2_input == "rock") or \
            (p1_input == "scissors" and p2_input == "paper"):
        print(p1_winround)
        p1_score = p1_score + 1
        round = round + 1

    # Player 2 earns a point and is declared round winner if one of three outcomes are achieved
    elif (p1_input == "scissors" and p2_input == "rock") or (p1_input == "paper" and p2_input == "scissors") or \
            (p1_input == "rock" and p2_input == "paper"):
        print(p2_winround)
        p2_score = p2_score + 1
        round = round + 1

    # Number of ties increases by one if none of the conditions above are met, indicating a tie
    else:
        print(tieround)
        tie_score = tie_score + 1
        round = round + 1

# Tallies the outcomes for each round
print("Player 1 won %.1i game(s), Player 2 won %.1i game(s), and %.1i game(s) were tied." % (p1_score, p2_score,
                                                                                             tie_score))

