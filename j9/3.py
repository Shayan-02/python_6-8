import random
# from random import randint
a = []
for i in range(51):
    a.append(random.randint(1000, 5000))
for j in a:
    print(j, end = " ")