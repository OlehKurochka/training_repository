# 1. Додати 1 до числа

def add_one(some_list:list) -> list:
    number = int("".join(map(str, some_list)))
    new_number = number + 1
    return list(map(int, str(new_number)))
print(add_one([1, 2, 3, 4]))

#######################################################################################

# 2. Паліандром

def is_palindrome(text:str) -> bool:
    text = text.lower()
    new_text = ""
    for letter in text:
        if letter.isalnum():
            new_text += letter
    return new_text == new_text[::-1]
print(is_palindrome('A man, a plan, a canal: Panama'))

########################################################################################

# 3. Унікальне число

def find_unique_value(some_list:list) -> int | float | None:
    for item in some_list:
        if some_list.count(item) == 1:
            return item
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))