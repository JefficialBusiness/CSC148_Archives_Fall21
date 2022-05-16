# Problem Set 3
# Name: Jeffrey Williams
# Time Spent: 5:30
# Last Modified: Oct 13, 2021

import random

# Presets amount in pile and default value for current player
pile = 100
current_player = ""

# Following code executes for as long as pile is equal to or beneath 100
while pile <= 100:
    current_player = "Computer"  # Assignment of current player variable to computer to indicate its turn
    if pile == 0:  # Breaks out of loop if there are zero stones in pile
        break
    if pile >= 5:  # Checks for amount of stones in pile to determine how many computer can take
        take = random.randint(1, 5)
    else:
        take = random.randint(1, pile)

    # Subtracts chosen amount of stones from pile, prints amount taken and what remains
    pile = pile - take
    print("It is the computer's turn. It took %.1i stone(s). There are now %.1i stones remaining." % (take, pile))

    current_player = "User"  # Signifies change to player/user's turn
    if pile == 0:
        break

    # Sets and holds invalid status until user inputs valid number of stones
    invalid = True
    while invalid:
        take = int(input("Pick between 1 and 5 stones to take. "))
        if take > 5 or take < 1:  # Ensures that amount of stones taken is between 1 and 5
            print("Please enter a number between 1 and 5.")
        elif take > pile:  # Checks to see if there are enough stones, otherwise prompts user again
            print("Please enter another number. There are not enough stones. Number of stones:", pile)
        else:  # Breaks invalid status if input is valid and proceeds
            invalid = False
            pile = pile - take
            print("It is the user's turn. They took %.1i stone(s). There are now %.1i stones remaining." % (take, pile))

# Determines and announces winner of game
if current_player == "User":
    print("The user wins.")
else:
    print("The computer wins.")
