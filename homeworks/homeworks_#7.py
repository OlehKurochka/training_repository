# 1. Вітання

def say_hi(name, age):
    return (f"Hi. My name is {name} and I'm {age} years old")

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

# 2. Модифікувати рядок

def correct_sentence(text):
    new_text = text[0].upper() + text[1:]
    if not new_text.endswith("."):
        new_text += "."
    return new_text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

#3. Пошук підрядка

def second_index(text, some_str):
    first_ind = text.find(some_str)
    second_ind = text.find(some_str, first_ind + 1)
    if second_ind == -1:
        return None
    return second_ind

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

# 4. Пошук спільних елементів

def common_elements():
    multiple3 = set()
    for i in range(0, 100, 3):
        multiple3.add(i)
    multiple5 = set()
    for i in range(0, 100, 5):
        multiple5.add(i)
    intersection_set = multiple3.intersection(multiple5)
    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')