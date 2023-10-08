import random_num

# Generate a random number between 1 and 100
randNum = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Start the game with a while loop
while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < randNum:
        print("Too low! Try again.")
    elif guess > randNum:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {randNum} in {attempts} attempts.")
        break
