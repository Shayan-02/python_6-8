def sums(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

result = 0
while True:
    a = int(input("Enter number: "))
    op = input("Enter operator: ")
    b = int(input("Enter a number: "))
    if op == "+":
        result = sums(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Invalid operator")
    print(result)
    again = input("Do you want to continue? (y/n) ")
    if again == "n":
        break
    else:
        pass