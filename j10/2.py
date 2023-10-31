import random

# Game choices
choices = ["rock", "paper", "scissors"]

def play_round():
    # Computer's random choice
    computer_choice = random.choice(choices)

    # Player input
    player_choice = input("Choose (rock, paper, or scissors) or 'q' to quit: ")

    if player_choice == 'q':
        return "quit"  # Return 'quit' to indicate that the player wants to quit.

    if player_choice in choices:
        # Print computer and player choices
        print(f"Computer's choice: {computer_choice}")
        print(f"Your choice: {player_choice}")

        # Determine the game result
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"
    else:
        return "invalid"

while True:
    result = play_round()

    if result == "quit":
        print("Goodbye! Thanks for playing.")
        break
    elif result == "tie":
        print("It's a tie! The game is a draw.")
    elif result == "win":
        print("You win! Congratulations!")
    elif result == "lose":
        print("Computer wins! Better luck next time.")
    else:
        print("Invalid choice. Please enter one of the valid options.")
