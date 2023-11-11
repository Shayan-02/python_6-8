a = {1, 1, 2, 3, 5, 1, 2, 3}
lst1 = [1, 1, 2, 3, 5, 1, 2, 3]
lst2 = [1, 1, 2, 3, 5, 1, 2, 3]
print(len(a))
print(len(lst1))
print(a)
print(type(a))
print(type(lst1))

b = set(lst1)
print(b)
print()
c = list(a)
print(a)
c[3] = "correct"
print(set(c))