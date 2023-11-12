import numpy as np


def power_of_two(x):
    for j in range(3):
        return x ** 2


a = []
for i in range(1, 4):
    num = int(input(f"enter number{i}: "))
    a.append(power_of_two(num))
    i += 1

# 1
b = np.array(a)
print(sum(b))

# 2
sums = 0
for x in a:
    sums += x
print(sums)
