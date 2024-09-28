# # Задание 1. Удаление дубликатов из списка
# a = [1, 1, 2, 3, 3, 4, 4, 5, 6]
# duplicate = []
# for i in a:
#     if a.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)
#
# print(duplicate)
#
#
# # Задача 2. Поиск наибольшего числа в списке
# a = [int(i) for i in input("Введите числа через пробел: ").split()]
# max_num = a[0]
#
# for i in a:
#     if i > max_num:
#         max_num = i
#
# print(max_num)
#
#
# # Задача 3. Проверка палиндрома
# string = input("Введите строку: ").lower()
#
# odd_chars = set()
#
# for char in string:
#     if char in odd_chars:
#         odd_chars.remove(char)
#     else:
#         odd_chars.add(char)
#
# if len(odd_chars) <= 1:
#     print("Строка является палиндромом")
# else:
#     print("Строка не является палиндромом")
#
#
# # Задача 4. Генерация паролей
import random
import string

lenght = int(input("Введите длину пароля: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(lenght))
print(password)

# Задача 5. Нахождение анаграмм
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
if len(word1) != len(word2):
    print("Слова не являются анаграммами")
else:
    char_count1 = {}
    char_count2 = {}
    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    if char_count1 ==char_count2:
        print("Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")