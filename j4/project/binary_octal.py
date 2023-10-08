binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)

octal_number = 0
i = 1

while(decimal_number != 0):
    remainder = decimal_number % 8
    octal_number += remainder * i
    decimal_number = decimal_number // 8
    i *= 10

print("Octal number:", octal_number)