from random import randint


def random_number_generator(minimum, maximum, guess, random_number):
    """
    Generates a random number between the minimum and maximum values.

    parameters:
    param minimum (int): The minimum value.
    param maximum (int): The maximum value.
    param guess (int): User guess value.
    param random_number (int): The random value.

    :return: A random number between the minimum and maximum values.
    """
    global correct
    correct = False
    if guess < minimum or guess > maximum:
        print("out of range ...")
    elif guess < random_number:
        print("too low ...")
    elif guess > random_number:
        print("too high ...")
    elif guess == random_number:
        print("correct ...")
        correct = True


minimum = int(input('Min number: '))
maximum = int(input('Max number: '))
r = randint(minimum, maximum)

i = 1
while i < 6:
    guess = int(input('Guess number: '))
    random_number_generator(minimum, maximum, guess, r)
    if correct == True:
        break
    i += 1
# end while
