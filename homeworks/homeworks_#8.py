# 1. Додати 1 до числа

def add_one(some_list):
    number = int("".join(map(str, some_list)))
    new_number = number + 1
    new_lst = list(map(int, str(new_number)))
    return new_lst

print(add_one([1, 2, 3, 4]))

#######################################################################################

# 2. Паліандром

def is_palindrome(text):
    text = text.lower()
    new_text = ""
    for letter in text:
        if letter.isalnum():
            new_text += letter
    return new_text == new_text[::-1]
print(is_palindrome('A man, a plan, a canal: Panama'))

########################################################################################

# 3. Унікальне число

def find_unique_value(some_list):
    some_list = [5, 5, 5, 2, 2, 0.5]
    new_dict = {}
    for item in some_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    revers_new_dict = {}
    for key, value in new_dict.items():
        revers_new_dict[value] = key
    return revers_new_dict[1]
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))