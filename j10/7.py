def name1():
    print("name1")
    c = 2 + 4
    return c

def name2(a, b):
    return "name2:", a + b


def name3(a, b):
    return "name3:", "a =", a, "b =", b


def name4(a, b):
    print("name4:", "a =", a, "b =", b)


name1()
name2(1, 2)
name3(3, 5)
name4(8, 7)

print()
print(name2(5, 6))
print(f"{name3(1, 2)}")