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
print(summa)

