# # 1. Вітання
#
# def say_hi(name, age):
#     return (f"Hi. My name is {name} and I'm {age} years old")
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

# # 2. Модифікувати рядок
#
# def correct_sentence(text):
#     new_text = text[0].upper() + text[1:]
#     if not new_text.endswith("."):
#         new_text += "."
#     return new_text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

# 3. Пошук підрядка
