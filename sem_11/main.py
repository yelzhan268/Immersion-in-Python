# # Задание 1. Матрицы
# # Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
# # поручили разработать класс Matrix для обработки и анализа данных. Ваш класс
# # должен предоставлять функциональность для выполнения основных операций
# # с матрицами, таких как сложение, вычитание, умножение и транспонирование.
# # Это будет полезно для обработки и структурирования больших объёмов
# # данных, которые используются в обучении нейронных сетей.
# # Задача
# # 1. Создайте класс Matrix для работы с матрицами.
# # Реализуйте методы:
# # ○ сложения,
# # ○ вычитания,
# # ○ умножения,
# # ○ транспонирования матрицы.
# # 2. Создайте несколько экземпляров класса Matrix и протестируйте
# # реализованные операции.
# class Matrix:
#     def __init__(self, rows, cols):
#         self.data = [[0 for _ in range(cols)] for _ in range(rows)]
#         self.rows = rows
#         self.cols = cols
#
#     def add(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for addition.")
#         return Matrix(self.rows, self.cols).from_list(
#             [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         )
#
#     def subtract(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for subtraction.")
#         return Matrix(self.rows, self.cols).from_list(
#             [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         )
#
#     def multiply(self, other):
#         if self.cols != other.rows:
#             raise ValueError("Invalid matrices dimensions for multiplication.")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 for k in range(self.cols):
#                     result.data[i][j] += self.data[i][k] * other.data[k][j]
#         return result
#
#     def transpose(self):
#         return Matrix(self.cols, self.rows).from_list(
#             [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
#         )
#
#     def from_list(self, data):
#         self.data = data
#         self.rows = len(data)
#         self.cols = len(data[0]) if data else 0
#         return self
#
#     def __str__(self):
#         return '\n'.join(['\t'.join(map(str, row)) for row in self.data])
#
#
# m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]
# m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]
# print("Матрица 1:")
# print(m1)
# print("Матрица 2:")
# print(m2)
# print("Сложение матриц:")
# print(m1.add(m2))
# print("Вычитание матриц:")
# print(m1.subtract(m2))
# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]
# print("Умножение матриц:")
# print(m1.multiply(m3))
# print("Транспонирование матрицы 1:")
# print(m1.transpose())
#
#
# # Задача 2. Магия
# # Для одной игры необходимо реализовать механику магии, где при соединении
# # двух элементов получается новый. У нас есть четыре базовых элемента:
# # «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
# # «Пар», «Грязь», «Молния», «Пыль», «Лава».
# import random
#
# TRIES = 10
#
#
# class Storm:
#     answer = "Вы сложили Воду и Воздух и получили класс Шторм"
#
#
# class Steam:
#     answer = "Вы сложили Воду и Огонь и получили класс Пар"
#
#
# class Mud:
#     answer = "Вы сложили Воду и Землю и получили класс Грязь"
#
#
# class Bolt:
#     answer = "Вы сложили Воздух и Огонь и получили класс Молния"
#
#
# class Dust:
#     answer = "Вы сложили Воздух и Землю и получили класс Пыль"
#
#
# class Lava:
#     answer = "Вы сложили Огонь и Землю и получили класс Лава"
#
#
# class Fog:
#     answer = "Вы сложили Воду и Пыль и получили класс Туман"
#
#
# class Water:
#     def __add__(self, other):
#         if isinstance(other, Soil):
#             return Mud()
#         elif isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Dust):
#             return Fog()
#         return None
#
#
# class Fire:
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Bolt()
#         elif isinstance(other, Soil):
#             return Lava()
#         return None
#
#
# class Air:
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Bolt()
#         elif isinstance(other, Soil):
#             return Dust()
#         return None
#
#
# class Soil:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Mud()
#         elif isinstance(other, Air):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lava()
#         return None
#
#
# def main():
#     elements = [Water(), Fire(), Air(), Soil(), Dust()]
#     try_count = 0
#     while try_count < TRIES:
#         element_a = random.choice(elements)
#         element_b = random.choice(elements)
#         if element_a is element_b:
#             continue
#         result = element_a + element_b
#         if result is None:
#             continue
#         try_count += 1
#         print(result.answer)
#
#
# main()
#
# # Задача 3. Класс Rectangle - работа с прямоугольниками
# # Разработайте программу для работы с прямоугольниками. Необходимо создать класс
# # Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
# class Rectangle:
#     def __init__(self, width, height=None):
#         self.width = width
#         self.height = height if height is not None else width
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def __add__(self, other):
#         new_perimeter = self.perimeter() + other.perimeter()
#         new_width = new_perimeter // 4
#         new_height = new_width
#         return Rectangle(new_width, new_height)
#
#     def __sub__(self, other):
#         new_perimeter = abs(self.perimeter() - other.perimeter())
#         new_width = new_perimeter // 4
#         new_height = new_width
#         return Rectangle(new_width, new_height)
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __le__(self, other):
#         return self.area() <= other.area()
#
#     def __str__(self):
#         return f"Прямоугольник со сторонами {self.width} и {self.height}"
#
#     def __repr__(self):
#         return f"Rectangle({self.width}, {self.height})"
#
#
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
# print(f"Периметр rect1: {rect1.perimeter()}") # Вывод: 30
# print(f"Площадь rect2: {rect2.area()}") # Вывод: 21
# print(f"rect1 < rect2: {rect1 < rect2}") # Вывод: False
# print(f"rect1 == rect2: {rect1 == rect2}") # Вывод: False
# print(f"rect1 <= rect2: {rect1 <= rect2}") # Вывод: False
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}") # Вывод: 50
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}") # Вывод: 2
# print(rect3) # Вывод: Прямоугольник со сторонами 12 и 12
# print(repr(rect4)) # Вывод: Rectangle(2, 2)
#
#
# Задача 4. Стек
# В программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых
# структур является стек.
# class Stack:
#     def __init__(self):
#         self.__stack = list()
#
#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.__stack.pop()
#
#     def push(self, item):
#         self.__stack.append(item)
#
#     def is_empty(self):
#         return len(self.__stack) == 0
#
#     def top(self):
#         if self.is_empty():
#             return None
#         return self.__stack[-1]
#
#
# class TaskManager:
#     def __init__(self):
#         self.tasks = dict()
#
#     def new_task(self, text, priority):
#         if priority not in self.tasks:
#             self.tasks[priority] = Stack()
# # Добавляем задачу в стек для данного приоритета
#         self.tasks[priority].push(text)
#
#     def remove_task(self, text):
#         for stack in self.tasks.values():
#             temp_stack = Stack()
#             while not stack.is_empty():
#                 task = stack.pop()
#                 if task != text:
#                     temp_stack.push(task)
#             while not temp_stack.is_empty():
#                 stack.push(temp_stack.pop())
#
#     def __str__(self):
#         sorted_keys = sorted(self.tasks.keys())
#         out = []
#         for key in sorted_keys:
#             task_line = [str(key)] # Начинаем строку с приоритета
#             temp_stack = Stack()
#             while not self.tasks[key].is_empty():
#                 task = self.tasks[key].pop()
#                 temp_stack.push(task)
#             while not temp_stack.is_empty():
#                 task_line.append(temp_stack.pop())
#             out.append(' '.join(task_line))
#         return '\n'.join(out)
#
#
# def main():
#     manager = TaskManager()
#     manager.new_task("сделать уборку", 4)
#     manager.new_task("помыть посуду", 4)
#     manager.new_task("отдохнуть", 1)
#     manager.new_task("поесть", 2)
#     manager.new_task("сдать дз", 2)
#     print(manager)
#     manager.remove_task("поесть")
#     print("\nПосле удаления задачи:")
#     print(manager)
#
#
# main()
#
#
# # Задача 5. Абстрактный класс
# # Вы работаете в компании, занимающейся разработкой программного обеспечения
# # для архитектурных проектов. Вам необходимо разработать программу для расчёта
# # площади различных геометрических фигур, таких как круги, прямоугольники и
# # треугольники
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2



class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
try:
    shape = Shape() # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка: {e}")

    