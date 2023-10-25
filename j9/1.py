# functions
def sum_numbers(a, b):
    return a + b
def sub_numbers(a, b):
    return a - b
def mul_numbers(a, b):
    return a * b
def div_numbers(a, b):
    return a / b

i = 1
loop = True

num1 = int(input(f"enter number{i}: "))
i += 1
op = input("enter operator: ")
num2 = int(input(f"enter a number{i}: "))
if op == "+":
    result = sum_numbers(num1, num2)
elif op == "-":
    result = sub_numbers(num1, num2)
elif op == "*":
    result = mul_numbers(num1, num2)
elif op == "/":
    result = div_numbers(num1, num2)
else:
    print("invalid operator")
i += 1
while loop:
    again = input("do you want to continue calc?(y/n): ")
    if again.lower() == "n":
        break
    elif again.lower() == "y":
        op2 = input("enter operator: ")
        num3 = int(input(f"enter a number{i}: "))
        if op2 == "+":
            result = sum_numbers(result, num3)
        elif op2 == "-":
            result = sub_numbers(result, num3)
        elif op2 == "*":
            result = mul_numbers(result, num3)
        elif op2 == "/":
            result = div_numbers(result, num3)
        else:
            print("invalid operator")
        i += 1

print("result:", result)
