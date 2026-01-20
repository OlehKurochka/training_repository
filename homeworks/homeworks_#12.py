# 1. Очистити текст від html-тегів

import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    chars = []
    inside_tag = False
    for char in html:
        if char == "<":
            inside_tag = True
        elif char == ">":
            inside_tag = False
        elif not inside_tag:
            chars.append(char)
    without_tags = "".join(chars)
    # not_spaces = []
    # for line in without_tags.splitlines():
    #     if line.strip():
    #         not_spaces.append(line)
    without_spaces = "\n".join(line for line in without_tags.splitlines() if line.strip())
    print(without_spaces)

    with codecs.open(result_file, 'w', 'utf-8') as cleaned_file:
        cleaned_file.write(without_spaces)
delete_html_tags("draft.html")

#####################################################################################################

# 2. Корзина для покупок

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f'{self.name}'

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'User: {self.name} {self.surname}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        in_sum =''
        for item, cnt in self.products.items():
            in_sum += f'\t{str(item)}: {cnt} pcs. \n'
        return f'Items:\n{in_sum}'

    def get_total(self):
        for key, cnt in self.products.items():
            self.total += key.price * cnt
        return f'__________________________________________\n The total cost is: {self.total} UAH\n'


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())

cart.add_item(apple, 10)
print(cart)
print(cart.get_total())