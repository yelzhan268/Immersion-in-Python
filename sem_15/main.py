# # Задание 1. Логирование с использованием нескольких файлов
# # Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# # Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# # WARNING и выше — в warnings_errors.log.
# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# debug_info_handler = logging.FileHandler('debug_info.log')
# debug_info_handler.setLevel(logging.DEBUG)
# debug_info_handler.setFormatter(formatter)
# logger.addHandler(debug_info_handler)
# warnings_errors_handler = logging.FileHandler('warnings_errors.log')
# warnings_errors_handler.setLevel(logging.WARNING)
# warnings_errors_handler.setFormatter(formatter)
# logger.addHandler(warnings_errors_handler)
# logger.debug('Это сообщение уровня DEBUG.')
# logger.info('Это сообщение уровня INFO.')
# logger.warning('Это сообщение уровня WARNING.')
# logger.error('Это сообщение уровня ERROR.')
# logger.critical('Это сообщение уровня CRITICAL.')
#
#
#
# # Задача 2. Работа с текущим временем и датой
# # Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# # формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# # недели в году.
# from datetime import datetime
# def display_current_datetime():
#     now = datetime.now()
#     formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
#     day_of_week = now.strftime('%A')
#     week_number = now.isocalendar()[1]
#     print(f'Current date and time: {formatted_date}')
#     print(f'Day of the week: {day_of_week}')
#     print(f'Week number: {week_number}')
# if __name__ == '__main__':
#     display_current_datetime()
#
#
# # Задача 3. Планирование задач
# # Напишите функцию, которая принимает количество дней от текущей даты и
# # возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# # выведите эту дату в формате YYYY-MM-DD.
# from datetime import datetime, timedelta
#
# def future_date(days_from_now):
#     today = datetime.now()
#     future_date = today + timedelta(days=days_from_now)
#     formatted_future_date = future_date.strftime('%Y-%m-%d')
#     return formatted_future_date
#
# if __name__ == '__main__':
#     days = 30
#     print(f'Date {days} days from now: {future_date(days)}')
#
# # Задача 4. Опции и флаги
# # Напишите скрипт, который принимает два аргумента командной строки: число и
# # строку. Добавьте следующие опции:
# # ● --verbose, если этот флаг установлен, скрипт должен выводить
# # дополнительную информацию о процессе.
# # ● --repeat, если этот параметр установлен, он должен указывать,
# # сколько раз повторить строку в выводе.
# import argparse
#
#
# def main():
#     parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')
#     parser.add_argument('number', type=int, help='Число для вывода')
#     parser.add_argument('text', type=str, help='Строка для вывода')
#     parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
#     parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
#     args = parser.parse_args()
#     if args.verbose:
#         print(f'Полученные аргументы: number={args.number},'
#               f'text="{args.text}", repeat={args.repeat}')
#     print(f'Число: {args.number}, Строка: {args.text * args.repeat}')
#
#
# if __name__ == '__main__':
#     main()
#
# # Задача 5. Запуск из командной строки
# # Напишите код, который запускается из командной строки и получает на вход путь
# # до директории на ПК. Соберите информацию о содержимом в виде объектов
# # namedtuple. Каждый объект хранит: имя файла без расширения или название
# # каталога, расширение, если это файл, флаг каталога, название родительского
# # каталога. В процессе сбора сохраните данные в текстовый файл используя
# # логирование.
import os
import logging
from collections import namedtuple
from argparse import ArgumentParser


FileInfo = namedtuple('FileInfo', ['name', 'extension',
                                   'is_directory', 'parent_directory'])
logging.basicConfig(filename='directory_contents.log',
                    level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_info(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не"
                         f"является директорией.")
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        if os.path.isdir(entry_path):
            file_info = FileInfo(name=entry, extension=None,
                                 is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(name=name,
                                 extension=extension.lstrip('.'), is_directory=False,
                                 parent_directory=parent_directory)
        logging.info(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}')


def main():
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")
    args = parser.parse_args()
    directory_path = args.directory
    try:
        collect_info(directory_path)
        print(f'Информация о содержимом директории'
              f'"{directory_path}" успешно записана в файл'
              f'"directory_contents.log".')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
