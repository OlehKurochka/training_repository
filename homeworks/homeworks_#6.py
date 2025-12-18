# # 1. Діапазон букв
# from string import ascii_letters
# letters = input("Enter a two letters: ")
#
# first_letter, last_letter = letters.split("-")
# start = ascii_letters.index(first_letter)
# end = ascii_letters.index(last_letter)
# result = " "
# for ind in range(start, end + 1):
#     result += ascii_letters[ind]
#
# print(result)

# # 2. Конвертер із числа в дату
#
# number = int(input("Enter a number: "))
# if number <= 8640000:
#     day, n1 = divmod(number, 86400)
#     hour, n2 = divmod(n1, 3600)
#     minute, second = divmod(n2, 60)
#     if day == 1:
#         prnt_day = "день"
#     elif 2 <= day % 10 <= 4 and not 11 <= day % 100 <= 14:
#         prnt_day = "дні"
#     else:
#         prnt_day = "днів"
#     time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
#     print(f"{day} {prnt_day}, {time}")
# else:
#     print("The number must be up to 8640000")