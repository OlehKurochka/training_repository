# 1. Перемістити всі нулі до кінця списку

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for num in lst:
    if num == 0:
        lst.remove(num)
        lst.append(num)
print(lst)

