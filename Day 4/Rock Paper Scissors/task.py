import random

# Define ASCII art for Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store ASCII art in a list
randomizer = [rock, paper, scissors]

# Get user input with validation
try:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
    if user not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1, or 2.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number: 0, 1, or 2.")
    exit()

# Computer makes a random choice
choice = random.randint(0, 2)

# Display user and computer choices
print(f"\nYou chose:\n{randomizer[user]}")
print(f"Computer chose:\n{randomizer[choice]}")

# Determine the result
if user == choice:
    print("It's a draw!")
elif (user == 0 and choice == 2) or (user == 1 and choice == 0) or (user == 2 and choice == 1):
    print("You won!")
else:
    print("You lost!")
