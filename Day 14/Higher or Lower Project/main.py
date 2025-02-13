# Import necessary modules
import random
from art import logo, vs
from game_data import data

def format_data(account):
    """Return a formatted string with account details."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, followers_a, followers_b):
    """Check if the user's guess is correct."""
    return (guess == "a" and followers_a > followers_b) or (guess == "b" and followers_b > followers_a)

# Display the logo at the start of the game
print(logo)

# Initialize variables
score = 0
continue_game = True
account_b = random.choice(data)  # Start with a random account for B

# Main game loop
while continue_game:
    # Shift account B to account A and get a new random account for B
    account_a, account_b = account_b, random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # Display both accounts
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # User input
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear screen (simple way to simulate clearing)
    print("\n" * 20)
    print(logo)

    # Retrieve follower counts
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    # Determine if the guess is correct
    if check_answer(guess, followers_a, followers_b):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_game = False
