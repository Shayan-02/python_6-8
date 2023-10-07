a = int(input("n: "))
b = int(input("m: "))

if a > 0 and b > 0:
    for i in range(1,a+1):
        for j in range (1,b+1):
            print(i*j , end="\t")
        print( )

elif a == 0 or b == 0:
    print(0)

else:
    print("false number...")