import random
import string

random_string = ''.join(random.choice(string.ascii_letters) for _ in range(17))
print(random_string)
