def name1():
    return "name1:", 2 + 4


def name2(a, b):
    print("name2:", a + b)


def name3(a, b):
    return "name3:", "a =", a, "b =", b


def name4(a, b):
    print("name4:", "a =", a, "b =", b)


name1()
name2(1, 2)
name3(1, 2)
name4(1, 2)

print()
print(name1())
print(f"{name3(1, 2)}")