import random
random_numbers = [random.randint(0, 1000) for i in range(100)]
random_numbers.sort()

for index, number in enumerate(random_numbers):
    print(f"{index+1}: {number}")
