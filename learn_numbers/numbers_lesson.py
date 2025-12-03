# 1. Квадрат числа

n = int(input("Введіть число для виводу його в квадрат: "))
print("Результат:", n**2)

# 2. Середнє трьох чисел

from decimal import Decimal

n1 = Decimal(input("Введіть перше число: "))
n2 = Decimal(input("Введіть друге число: "))
n3 = Decimal(input("Введіть третє число: "))
average_n = round((n1+n2+n3)/3, 1)
print("Середнє арифметичне тьох чисел:", average_n)

# 3. Перетворення хвилин в години

n = int(input("Введіть кількість хвилин: "))
hours = n // 60
minutes = n % 60
print(hours, "години", minutes, "хвилин")

# 4. Розрахунок знижки
from decimal import Decimal

price = Decimal(input("Введіть ціну: "))
discount = Decimal(input("Розмір знижки: "))
n = round((p * d)/100, 2)
print("Ціна зі знижкою :", price - n)

# 5. Остання цифра числа
n = int(input("Введіть число: "))
print(n%10)

# 6. Периметр прямокутника

a = float(input("Введіть число: "))
b = float(input("Введіть число: "))
print("Периметр:", (a+b)*2)

7. Виведення числа в стовпчик

n = int(input("Введіть число 4-х значне число: "))
n1, n2 = divmod(n, 100)
print(n1//10)
print(n1%10)
print(n2//10)
print(n2%10)