# 1. Генератор простих чисел

def prime_generator(end):
    for n in range(2, end + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n

print(list(prime_generator(20)))

#########################################################################################

# 2. Заповнення списку кубами чисел

def generate_cube_numbers(end):
    for n in range(2, end + 1):
        if n ** 3 >= end + 1:
            return
        yield n ** 3

print(list(generate_cube_numbers(1000)))

#########################################################################################

# 3. Перевірка на парність

def is_even(number):
    return str(number)[-1] in "02468"

print(is_even(2494563894034))