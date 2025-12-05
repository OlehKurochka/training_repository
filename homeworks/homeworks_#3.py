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
        print("You can't divide by zero!")
    else:
        print("Result", num1 / num2)

# 2. Перемістити елемент у списку

lst = [1]
if lst:
    last_element = lst.pop()
    lst.insert(0, last_element)
    print(lst)
else:
    print(lst)

# 3. Розділити один список на два списки

lst = [1, 2, 3, 4, 5]
half_list = ((len(lst) + 1) // 2)
first_list = lst[:half_list]
second_list = lst[half_list:]
new_lst = list()
new_lst.append(first_list)
new_lst.append(second_list)
print(new_lst)
