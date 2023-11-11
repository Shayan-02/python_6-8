while True:
    num1 = int(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")

    print("Result * 2: ", result*2)

    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        break
