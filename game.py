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













# DISPLAY FINAL OUTPUTS / OUTCOMES
