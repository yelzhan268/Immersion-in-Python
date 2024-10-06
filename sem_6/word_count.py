# Задание 1. Модуль для подсчета количества повторений слов
def count_wors_occurrences(words):
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count