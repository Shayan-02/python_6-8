j = 1
min = int(input("enter min number: "))
max = int(input("enter max number: "))
i = min
for i in range(min, max):
    if i % 2 == 0:
        print(f"{j}: {i}")
        j += 1
        i += 1