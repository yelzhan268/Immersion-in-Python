# # Задание 1. Квадраты чисел
# from typing import Iterator
#
#
# def generator_function(n: int) -> Iterator[int]:
#     """
#     Генератор для вывода квадратов чисел отт 1 до n.
#     :param n: Число, до которого генерируются квадраты (включительно).
#     :return: Возвращает квадрат текущего числа в каждой итерации.
#     """
#     for number in range(1, n + 1):
#         yield number ** 2
#
#
# def main() -> None:
#     """
#     Основная функция. Запрашивает ввод числа N, выводит квадраты чисел двумя способами.
#     :return: None
#     """
#     n = int(input('Введите число N: '))
#
#     print('Вывод квадратов. Функция-генератор')
#
#     for square in generator_function(n):
#         print(square, end=' ')
#     print('\n')
#
#     print('Вывод квадратов. Генераторное выражение')
#
#     generator_expr = (i ** 2 for i in range(1, n + 1))
#
#     for square in generator_expr:
#         print(square, end=' ')
#     print()
#
# main()
#
# # Задача 2. Однострочный генератор словаря
# def calculate_bonus(names, salary, bonus):
#     result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
#     return result
#
#
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%","15%"]
#
# result = calculate_bonus(names, salary,bonus)
# print(result)
#
# # Задача 3. Генератор последовательности чисел Фибоначчи
# def fibonacci(n):
#     a, b = 0, 1
#
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# for number in fibonacci(10):
#     print(number)
#
# # Задача 4. Генератор подстрок
def substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]



for substring in substrings('abc'):
    print(substring)
