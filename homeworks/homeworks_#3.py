# 1. Калькулятор

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
action = input("What action to take (+, -, *, /): ")

if action == "+":
    print("Result", num1 + num2)
elif action == "-":
    print("Result", num1 - num2)
elif action == "*":
    print("Result", num1 * num2)
elif action == "/":
    if num2 == 0:
        num2 = None
        print("На нуль ділити не можна!")
    else:
        print("Result", num1 / num2)