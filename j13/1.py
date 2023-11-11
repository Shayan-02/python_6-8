import numpy as np


a = [25, 50 , 4, 5, 70, 20]
max = 0
min = 100
sum = 0
for i in a:
    if i > max:
        max = i
    i += 1
for j in a:
    if j < min:
        min = j
    j += 1
for k in a:
    sum += k
    k += 1
print(sum)
print(max)
print(min)


e = np.array([15, 20, 13, 87, 25, 50, 78])
print(np.max(e))
print(np.min(e))


s = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
ss = np.random.shuffle(s)
print(ss)
