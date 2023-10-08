j = 1
n = int(input("enter a number: "))
m = int(input("enter a number: "))
i = n
for i in range(n, m):
    if i % 2 == 0:
        print(f"{j}: {i}")
        j += 1
        i += 1