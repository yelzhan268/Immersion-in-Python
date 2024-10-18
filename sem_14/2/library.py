# Задача 2. Тестирование класса с использованием unittest
# Напишите класс Library, который управляет книгами. Класс должен поддерживать
# следующие методы:
# ● add_book(title): добавляет книгу в библиотеку.
# ● remove_book(title): удаляет книгу из библиотеки.
# ● list_books(): возвращает список всех книг в библиотеке.
# При попытке удалить книгу, которая не существует, должно выбрасываться исключение
# BookNotFoundError. Для тестирования используйте unitest.
class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")


class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        self.books.add(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError()
        self.books.remove(title)

    def list_books(self):
        return list(self.books)
