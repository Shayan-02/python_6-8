import random
# from random import randint
a = []
for i in range(50):
    a.append(random.randint(100, 500))
for j in a:
    print(j, end = " ")