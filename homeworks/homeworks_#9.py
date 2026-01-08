#1. Визначити популярність певних слів у тексті
def popular_words(text: str, list_words: list ) -> dict:
    text_lst = text.lower().split()
    number_of_words = {word: text_lst.count(word) for word in list_words}
    return number_of_words
print(popular_words("When I was One I had just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near']))

###############################################################################################################

#2. Різниця між числами
def difference(*args):
    return 0 if len(args) == 0 else round(max(args) - min(args), 2)
print(difference(10.2, -2.2, 0, 1.1, 0.5))