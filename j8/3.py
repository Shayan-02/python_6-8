def sums(a, b):
    print(f"result: ", a + b)

def sub(a, b):
    print(f"result: ", a + b)

def mul(a, b):
    print(f"result: ", a + b)

def div(a, b):
    print(f"result: ", a + b)

number1 = int(input("enter number1: "))
op = input("enter the operation: ")
number2 = int(input("enter number2: "))

if op == "+":
    sums(number1, number2)
elif op == "-":
    sub(number1, number2)
elif op == "*":
    sub(number1, number2)
elif op == "/":
    sub(number1, number2)
else:
    print("invalid operation...")