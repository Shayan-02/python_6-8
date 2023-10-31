import random
import re
from termcolor import colored

def generate_password(length):
    # Define the character classes for the password
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_chars = '!@#$%^&*'

    # Combine all character classes
    all_chars = uppercase + lowercase + digits + special_chars

    # Use regular expressions to ensure password complexity
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*]).{' + str(length) + ',}$')

    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if pattern.match(password):
            return password

# Usage: Generate an 8-character password
l = int(input("Enter length of password: "))
password = generate_password(l)
print(colored(password, "green"))
