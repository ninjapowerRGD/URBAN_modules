print("ПРИВЕТ, Я МОГУ НАЙТИ ОДНОКОРЕННЫЕ СЛОВА В СПИСКЕ")
root_word = input("Введите слово, которое мы будем сравнивать (корень): ").casefold()
other_words = input("Введите список слов для сравнения, разделяя их пробелами: ").casefold().split()


def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:

        if root_word in word or word in root_word:
            same_words.append(word)

    return same_words


result = single_root_words(root_word, *other_words)
print(result)
