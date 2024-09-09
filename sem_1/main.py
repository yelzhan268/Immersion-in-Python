# # Задание 1. Рамка
# height = int(input("Введите высоту рамки: "))
# width = int(input("Введите ширину рамки: "))
#
# for line in range(height + 1):
#     for col in range(width + 1):
#         if col == width or col == 0:
#             print('|', end='')
#         elif line == height or line == 0:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()
#
# # Задание 2. Треугольник
# a = float(input("Введите сторону a: "))
# b = float(input("Введите сторону b: "))
# c = float(input("Введите сторону c: "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует.")
#     if a == b == c:
#         print("Треугольник равносторонний.")
#     elif a == b or b == c or c == a:
#         print("Треугольник равнобедренный.")
#     else:
#         print("Треугольник разносторонний.")
# else:
#     print("Треугольник не существует.")
#
# # Задача 3. Простые числа
# n = int(input("Введите количество чисел в последовательности: "))
# count = 0
#
# for i in range(n):
#     number = int(input("Введите число: "))
#     if number > 1:
#         for divider in range(2, number):
#             if number % divider == 0:
#                 break
#         else:
#             count += 1
#
# print('Количество простых чисел: ', count)

# # Задача 4. Яма
# n = int(input("Введите число: "))
#
# for line in range(n):
#     for left_number in range(n, n - line -1, -1):
#         print(left_number, end="")
#     point_count = 2 * (n - line - 1)
#     print("." * point_count, end="")
#     for right_number in range(n - line, n + 1):
#         print(right_number, end="")
#     print()

# Задача 5. Игра "Компьютер угадывает число"
start = 1
finish = 100
count = 1
while True:
    n = (start + finish) // 2
    print('Число равно, меньше или больше ', n)
    print('1 - равно, 2 - меньше, 3 - больше')
    answer = int(input())
    if answer == 1:
        print('Я угадал! Ура! с', count, 'попыток')
    elif answer == 2:
        finish = n
    elif answer == 3:
        start = n
    count += 1
