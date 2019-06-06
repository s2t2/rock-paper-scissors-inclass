# game.py

import random

print("Rock, Paper, Scissors, Shoot!") # this is also a comment

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("--------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(options)

print("--------------")
print("GENERATING...")
print("COMPUTER CHOICE:", computer_choice)

# DETERMINE THE WINNER
#
# rock beats scissors
# paper beats rock
# scissors beats paper
# same selections is a tie
#


#if user_choice == computer_choice:
#    print("TIE")
#elif user_choice == "rock" and computer_choice == "paper":
#    print("WINNER IS PAPER")
#    print("COMPUTER WINS")
#elif user_choice == "rock" and computer_choice == "scissors":
#    print("ROCK")
#elif user_choice == "paper" and computer_choice == "rock":
#    print("PAPER")
#elif user_choice == "paper" and computer_choice == "scissors":
#    print("SCISSORS")
#elif user_choice == "scissors" and computer_choice == "rock":
#    print("ROCK")
#elif user_choice == "scissors" and computer_choice == "paper":
#    print("SCISSORS")

if user_choice == computer_choice:
    winning_choice = None # the outcome is a tie
else:
    choices = [user_choice, computer_choice]
    choices.sort() # FYI: this is mutating

    if choices == ["paper", "rock"]:
        winning_choice = "paper"
    elif choices == ["paper", "scissors"]:
        winning_choice = "scissors"
    elif choices == ["rock", "scissors"]:
        winning_choice = "rock"

if winning_choice:
    if winning_choice == user_choice:
        print("YOU WON")
    elif winning_choice == computer_choice:
        print("YOU LOST")
    else:
        print("TIE")

print("Thanks for playing. Please play again!")

# DISPLAY FINAL OUTPUTS / OUTCOMES
