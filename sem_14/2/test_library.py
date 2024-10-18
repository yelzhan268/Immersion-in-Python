import unittest
from library import Library, BookNotFoundError  # Импортируем классы из файла library.py

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создает экземпляр библиотеки для тестирования."""
        self.library = Library()

    def test_add_book(self):
        """Проверяет, что метод add_book корректно добавляет книгу."""
        self.library.add_book("1984")
        self.assertIn("1984", self.library.list_books())

    def test_remove_book(self):
        """Проверяет, что метод remove_book корректно удаляет книгу."""
        self.library.add_book("Brave New World")
        self.library.remove_book("Brave New World")
        self.assertNotIn("Brave New World", self.library.list_books())

    def test_remove_book_not_found(self):
        """Проверяет, что метод remove_book выбрасывает исключение BookNotFoundError."""
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")

    def test_list_books(self):
        """Проверяет, что метод list_books возвращает правильный список книг."""
        self.library.add_book("To Kill a Mockingbird")
        self.library.add_book("The Great Gatsby")
        self.library.remove_book("To Kill a Mockingbird")
        self.assertEqual(self.library.list_books(), ["The Great Gatsby"])

if __name__ == "__main__":
    unittest.main()