# game.py

print("Rock, Paper, Scissors, Shoot!") # this is also a comment

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("--------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS

if user_choice in ["rock", "paper", "scissors"]:
    print("VALID")
else:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

print("GENERATING...")

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES
