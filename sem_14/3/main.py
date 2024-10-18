class Rectangle:
    """
    Класс для управления прямоугольником.
    """

    def __init__(self, width=0, height=0):
        """
        Инициализирует прямоугольник с заданной шириной и высотой.

        >>> rect = Rectangle(3, 4)
        >>> rect.get_area()
        12
        >>> rect.get_perimeter()
        14
        """
        self.set_dimensions(width, height)

    def set_dimensions(self, width, height):
        """
        Устанавливает ширину и высоту прямоугольника.

        :param width: Ширина прямоугольника.
        :param height: Высота прямоугольника.

        >>> rect = Rectangle()
        >>> rect.set_dimensions(3, 4)
        >>> rect.get_area()
        12
        >>> rect.get_perimeter()
        14

        >>> rect.set_dimensions(0, 5)
        >>> rect.get_area()
        0
        >>> rect.get_perimeter()
        10

        >>> rect.set_dimensions(-1, 4)
        Traceback (most recent call last):
            ...
        ValueError: Ширина и высота должны быть неотрицательными числами.
        """
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть неотрицательными числами.")
        self.width = width
        self.height = height

    def get_area(self):
        """
        Возвращает площадь прямоугольника.

        >>> rect = Rectangle(2, 5)
        >>> rect.get_area()
        10
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Возвращает периметр прямоугольника.

        >>> rect = Rectangle(2, 5)
        >>> rect.get_perimeter()
        14
        """
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    import doctest

    doctest.testmod()