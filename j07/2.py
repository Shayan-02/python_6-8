t = (1, "a", 2)
lst = list(t)
lst[1] = "b"
t = tuple(lst)
print(t)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits


print("1", green)
print("2", yellow)
print("3", red)
