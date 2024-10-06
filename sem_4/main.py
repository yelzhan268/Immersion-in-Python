# # Задание 1. Апгрейд калькулятора
# def digits_summ(num):
#     summ = 0
#     while num > 0:
#         digit = num % 10
#         summ += digit
#         num //= 10
#     print('Сумма цифр: ', summ)
#
# def max_digit(num):
#     maximum = 0
#     while num > 0:
#         digit = num % 10
#         if digit > maximum:
#             maximum = digit
#         num //= 10
#     print('Максимальная цифра: ', maximum)
#
# def min_digit(num):
#     minimum = num %10
#     while num > 0:
#         digit = num % 10
#         if digit < minimum:
#             minimum = digit
#         num //= 10
#     print('Минимальная цифра: ', minimum)
#
# while True:
#     num = int(input('Введите число: '))
#     action = int(input('Введите номер действия : 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: '))
#     if action == 1:
#         digits_summ(num)
#     elif action == 2:
#         max_digit(num)
#     elif action == 3:
#         min_digit(num)
#     else:
#         print('Ошибка: неверная команда.')
#
# # Задача 2. Недоделка
# def rock_paper_scissors():
#     player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите Ваш выбор: "))
#     computer = 1
#     if player == computer:
#         print("Ничья!")
#     elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#         print("Вы победили!")
#     elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
#         print("Вы проиграли!")
#     else:
#         print("Неверная команда.")
#
# def guess_the_number():
#     number = 7
#
#     while True:
#         guess_num = int(input('Введите число: '))
#
#         if guess_num > number:
#             print('Число больше, чем нужно.Попробуйте еще раз!')
#         elif guess_num < number:
#             print('Число меньше, чем нужно.Попробуйте еще раз!')
#         else:
#             print('Поздравляю, Вы угадали! возврат в главное меню.')
#             break
#
# def main_menu():
#     while True:
#         print('Во что хотите поиграть?')
#         game = int(input('1 - Камень, ножницы, бумага; 2 - Угадай число; 3 - Выйти: '))
#
#         if game == 1:
#             rock_paper_scissors()
#         elif game == 2:
#             guess_the_number()
#         elif game == 3:
#             print('Выход из цикла программ.')
#             break
#         else:
#             print('Неверная команда. Попробуйте снова.')
#
# main_menu()
#
#
# # Задача 3. Число наоборот
# def reversal(x):
#     count = 0
#     revers_x = 0
#
#     for _ in str(x):
#         count += 1
#
#     while x > 0:
#         count -= 1
#         revers_x += (x % 10) * (10 ** count)
#         x = x // 10
#     return revers_x
#
#
# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# revers_num1 = reversal(num_1)
# revers_num2 = reversal(num_2)
#
# print('\nПервое число наоборот: ', revers_num1)
# print('Второе число наоборот: ', revers_num2)
# amount = revers_num1 + revers_num2
# revers_summ = reversal(amount)
#
# print('\nСумма: ', amount)
# print('Сумма наоборот: ', revers_summ)
#
#
# # Задача 4. Функция максимума
# def max_of_2(number_1, number_2):
#     if number_1 > number_2:
#         return number_1
#     return number_2
#
# def max_of_3(number_1, number_2, number_3):
#     return max_of_2(max_of_2(number_1, number_2), number_3)
#
# digit_1 = int(input('Введите первое число: '))
# digit_2 = int(input('Введите второе число: '))
# digit_3 = int(input('Введите третье число: '))
#
# print('Самое большое число: ', max_of_3(digit_1, digit_2, digit_3))
#
#
# # Задача 5. Яйца
def calculate_danger(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10

def find_safe_depth(max_danger):
    d_min = 0
    d_max = 4
    d_middle = (d_min + d_max) / 2
    middle_danger = calculate_danger(d_middle)

    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            d_min = d_middle
        else:
            d_max = d_middle
        d_middle = (d_min + d_max) / 2
        middle_danger = calculate_danger(d_middle)
    return d_middle

def main():
    max_danger = float(input('Введите допустимый уровень опасности: '))
    if max_danger < 0:
        print('Вы ввели недопустимое значение! Попробуйте еще раз.')
    else:
        safe_depth = find_safe_depth(max_danger)
        print(f'Приблизительная глубина безопасности кладки:  {safe_depth:.9f} м')


main()
