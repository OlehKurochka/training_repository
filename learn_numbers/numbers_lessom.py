# # 1. Квадрат числа
#
# n = float(input("Введіть число для виводу його в квадрат: "))
# print("Результат:", n**2)
#
# # 2. Середнє трьох чисел
#
# from decimal import Decimal
#
# n1 = Decimal(input("Введіть перше число: "))
# n2 = Decimal(input("Введіть друге число: "))
# n3 = Decimal(input("Введіть третє число: "))
# k = round((n1+n2+n3)/3, 2)
# print("Середнє арифметичне тьох чисел:", k)
#
# # 3. Перетворення хвилин в години
#
# n = int(input("Введіть кількість хвилин: "))
# hours = n // 60
# minutes = n % 60
# print(hours, "години", minutes, "хвилин")

# # 4. Розрахунок знижки
# from decimal import Decimal
#
# p = Decimal(input("Введіть ціну: "))
# d = Decimal(input("Розмір знижки: "))
# n = round((p * d)/100, 2)
# print("Ціна зі знижкою :", p - n)
