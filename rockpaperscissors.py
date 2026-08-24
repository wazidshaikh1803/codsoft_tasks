# Rock, Paper, Scissors Game

import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("----- ROCK, PAPER, SCISSORS -----")
print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock")

while True:
    # Get user's choice
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    if user_choice not in options:
        print("Invalid choice! Please type rock, paper, or scissors.")
        continue

    # Get computer's random choice
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score = user_score + 1

    else:
        print("Computer wins this round!")
        computer_score = computer_score + 1

    # Show the current score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Ask if the user wants to play again
    again = input("Do you want to play again? (Y/N): ")

    if again.lower() in ['y', 'yes']:
        continue
    else:
        print("\nThanks for playing!")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break