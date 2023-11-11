num_rows = int(input("enter a number: "))

current_number = 1

for i in range(num_rows):
    for j in range(i + 1):
        print(current_number, end=" ")
        current_number += 1
    print()
    """
    1
    2 3
    4 5 6
    7 8 9 10
    """