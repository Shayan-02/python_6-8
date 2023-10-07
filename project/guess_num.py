# Generate a random number between 1 and 100
randNum = 50

# Initialize the number of attempts
attempts = 1

# Start the game with a while loop
while attempts <= 5:
    guess = int(input(f"Enter your guess{attempts} (you have {5-attempts} attempts left): "))
    attempts += 1

    if guess < randNum:
        print("Too low! Try again.")
    elif guess > randNum:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {randNum} in {attempts} attempts.")
        break
