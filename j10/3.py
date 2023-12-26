import random
import string

x = int(input("length: "))
random_string = ''.join(random.choice(string.ascii_letters) for _ in range(x))
print(random_string)

r_s2 = random.randint(10000, 100000)
print(r_s2)