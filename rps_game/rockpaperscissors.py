'''
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner
'''

import random

def get_hand(x):
    # takes in an int and converts it to "Rock", "Paper", or "Scissors"
    if x == 0:
        return "Rock"
    elif x == 1:
        return "Paper"
    else:
        return "Scissors"

def determine_winner(rps: dict) -> str:
    # takes in a dict with player and computer selection and returns the winner
    # Determine if Player wins
    if (rps["Player"] == "Rock" and rps["Comp"] == "Scissors") or \
            (rps["Player"] == "Paper" and rps["Comp"] == "Rock") or \
            (rps["Player"] == "Scissors" and rps["Comp"] == "Paper"):
        winner = "Congrats! You win!"
    elif (rps["Player"] == "Rock" and rps["Comp"] == "Paper") or \
            (rps["Player"] == "Paper" and rps["Comp"] == "Scissors") or \
            (rps["Player"] == "Scissors" and rps["Comp"] == "Rock"):
        winner = "Computer Wins :("
    else:
        winner = "It's a tie!"
    return winner

# main program
print("Rock Paper Scissors Game!")

while True:         # get user selection
    player = input("\nSelect 0 for Rock, 1 for Paper, 2 for Scissors: ")
    if (player == "0") or (player == "1") or (player == "2"):
        player = int(player)
        break
    else:
        print("\nInvalid selection")

computer = random.randint(0,2)      # get computer selection
player_vs_comp = {"Player": get_hand(player), "Comp": get_hand(computer)}

# print out results
print(f"\nYou chose {get_hand(player)}. The computer chose {get_hand(computer)}!\n\n{determine_winner(player_vs_comp)}\n")

