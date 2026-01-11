#1. Генераторна функція

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    for n in range(end):
        yield begin
        begin = func(begin)
print(list(some_gen(2,4,pow)))

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

##########################################################################################

#2. Знайти перше слово

def first_word(text: str) -> str:
    """ Пошук першого слова """
    new_text = text.replace(",", " ").replace(".", " ")
    lst = new_text.split()
    return lst[0]

print(first_word(".., and so on ..."))

###########################################################################

#3. Перевірити чи є парним чи ні

def is_even(digit: int) -> bool:
    """ Перевірка чи є парним число """
    if digit % 2 == 0:
        return True
    return False

print(is_even(2))