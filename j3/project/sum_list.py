d = []
sum = 0
c = int(input("enter number of sessions: "))
for i in range(1, c + 1):
    a = int(input(f"enter the score of session{i}: "))
    d.append(a)
    i += 1
print(d)

for j in d:
    sum += j
    j += 1
result = sum / c
print(f"avg: {result}")