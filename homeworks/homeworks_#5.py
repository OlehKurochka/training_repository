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
