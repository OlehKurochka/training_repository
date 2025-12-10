# 1. Перемістити всі нулі до кінця списку

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for number in lst:
    if number == 0:
        lst.remove(number)
        lst.append(number)
print(lst)

# 2. Знайти суму елементів із парними індексами

lst = [0, 1, 7, 2, 4, 8]
if lst:
    summa = sum(lst[::2] * lst[-1])
else:
    summa = 0
print(lst, '=>', summa)

# 3. Список із 3 елементів

from random import randint

lst = []
for element in range(randint(3, 10)):
    lst.append(randint(1, 10))
new_lst = [lst[0], lst[2], lst[-2]]
print(lst, '==', new_lst)