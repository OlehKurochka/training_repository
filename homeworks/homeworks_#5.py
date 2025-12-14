#1. Ім'я змінної

from string import punctuation
from keyword import kwlist

text = str(input('Enter a text: '))
result = True

if text[0].isdigit():
    result = False
if ' ' in text:
    result = False
if text in kwlist:
    result = False
if '__' in text:
    result = False
for char in text:
    if char in punctuation and char != "_":
        result = False
for char in text:
    if char.isalpha() and not char.islower():
        result = False
print(result)

#2. Модифікувати калькулятор

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    action = input("What action to take (+, -, *, /): ")
    result = None

    if action == "+":
        result = num1 + num2
    elif action == "-":
        result = num1 - num2
    elif action == "*":
        result = num1 * num2
    elif action == "/":
        if num2 == 0:
            print("You can't divide by zero!")
        else:
            result = num1 / num2
    else:
        print("Invalid action!")
    if result is not None:
        print("Result:", result)

    command = input("Continue? (y/n): ")
    if command != "y":
        break

#3. hashtag

from string import punctuation
text = input("Enter text: ")

text = text.title()
text = text.replace(" ", "")

new_text = ""
for char in text:
    if char not in punctuation:
        new_text += char

hashtag = "#"
for char in new_text:
    hashtag += char
if len(hashtag) > 140:
        hashtag = hashtag[:140]

print(hashtag)