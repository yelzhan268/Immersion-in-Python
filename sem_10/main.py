# # Задание 1. Отцы, матери и дети.
# class Parent:
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.children = []  # Список детей
#     def info(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет")
#
#
#     def add_child(self, child):
#         if self.age - child.age >= 16:
#             self.children.append(child)
#             print(f"Ребёнок {child.name} добавлен к {self.name}.")
#         else:
#             print(f"Ребёнок {child.name} не добавлен к {self.name}, так как разница в возрасте слишком мала.")
#
#     def feed(self, child):
#         if child in self.children:
#             child.hungry = False
#             print(f"{self.name} покормил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребёнком {self.name}.")
#
#     def calm(self, child):
#         if child in self.children:
#             child.calm = True
#             print(f"{self.name} успокоил(а) {child.name}.")
#         else:
#             print(f"{child.name} не является ребёнком {self.name}.")
#
#     def list_children(self):
#         if self.children:
#             print(f"У {self.name} есть следующие дети:")
#             for child in self.children:
#                 print(f" - {child}")
#         else:
#             print(f"У {self.name} нет детей.")
#
# class Child:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         self.calm = False  # Ребёнок по умолчанию не спокоен
#         self.hungry = True  # Ребёнок по умолчанию голоден
#
#     def get_status(self):
#         calm_status = "спокоен" if self.calm else "не спокоен"
#         hungry_status = "сыт" if not self.hungry else "голоден"
#         print(f"Ребёнок {self.name} {calm_status} и"
#               f"{hungry_status}.")
#
#     def __str__(self):
#         return f"Ребёнок {self.name}, {self.age} лет"
#
#
# parent = Parent("Иван", 40)
# child1 = Child("Анна", 20)
# child2 = Child("Петя", 10)
# child3 = Child("Маша", 3)
#
# for child in [child1, child2, child3]:
#     parent.add_child(child)
#
# parent.info()
# parent.list_children()
#
# for child in parent.children:
#     parent.feed(child)
#     parent.calm(child)
#     child.get_status()
#
#
# # Задача 2. Совместное проживание
# import random
#
#
# class House:
#     def __init__(self, food=50, money=0):
#         self.food = food
#         self.money = money
#
#
#     def buy_food(self, quantity, price):
#         if self.money >= price:
#             self.food += quantity
#             self.money -= price
#             print(f"Купили {quantity} единиц еды за {price} денег.")
#         else:
#             print("Недостаточно денег для покупки еды!")
#
#
#     def earn_money(self, salary):
#         self.money += salary
#         print(f"Заработали {salary} денег.")
#
#
# class Human:
#     def __init__(self, name, house):
#         self.name = name
#         self.hunger = 50
#         self.house = house
#
#
#     def eat(self):
#         if self.house.food >= 10:
#             self.hunger += 10
#             self.house.food -= 10
#             print(f"{self.name} поел. Сытость увеличилась до"
#                   f"{self.hunger}, еда уменьшилась до {self.house.food}.")
#         else:
#             print(f"{self.name} хотел поесть, но в доме недостаточно еды!")
#
#
#     def work(self):
#         self.hunger -= 10
#         self.house.earn_money(50)
#         print(f"{self.name} поработал. Сытость уменьшилась до{self.hunger}.")
#
#
#     def play(self):
#         self.hunger -= 5
#         print(f"{self.name} поиграл. Сытость уменьшилась до {self.hunger}.")
#
#
#     def shop_for_food(self):
#         self.house.buy_food(15, 50)
#
#
#     def live_day(self):
#         cube = random.randint(1, 6)
#         print(f"\nСегодняшний кубик: {cube}")
#         if self.hunger < 20:
#             self.eat()
#         elif self.house.food < 10:
#             self.shop_for_food()
#         elif self.house.money < 50:
#             self.work()
#         elif cube == 1:
#             self.work()
#         elif cube == 2:
#             self.eat()
#         else:
#             self.play()
#         if self.hunger <= 0:
#             print(f"{self.name} умер от голода.")
#             return False
#         return True
#
# house1 = House()
# human1 = Human("Артем", house1)
# human2 = Human("Даша", house1)
# house2 = House()
# human3 = Human("Филипп", house2)
#
# try:
#     for day in range(1, 366):
#         print(f"\nДень {day}")
#         if not human1.live_day() or not human2.live_day() or not human3.live_day():
#             print(f"Человек умер на {day} день.")
#             break
#
# finally:
#     print("\nСостояние пары:")
#     print(f"Еда в холодильнике - {house1.food}, Деньги - {house1.money}")
#     print(f"Состояние {human1.name}: Сытость - {human1.hunger}")
#     print(f"Состояние {human2.name}: Сытость - {human2.hunger}\n")
#     print("Состояние одиночки:")
#     print(f"Еда в холодильнике - {house2.food}, Деньги - {house2.money}")
#     print(f"Состояние {human3.name}: Сытость - {human3.hunger}")
#
#
# # Задача 3. Крестики-нолики
# class Cell:
#     def __init__(self, number):
#         self.number = number
#         self.symbol = " "
#         self.occupied = False
#
#
# class Board:
#     def __init__(self):
#         self.cells = [Cell(i) for i in range(1, 10)]
#
#     def display_board(self):
#         print("-------------")
#         for i in range(0, 9, 3):
#             print(f"| {self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol} |")
#             print("-------------")
#
#
#     def change_cell(self, cell_number, symbol):
#         cell = self.cells[cell_number - 1]
#         if cell.occupied:
#             return False
#         cell.symbol = symbol
#         cell.occupied = True
#         return True
#
#
#     def check_game_over(self):
#         win_positions = [
#             (0, 1, 2), (3, 4, 5), (6, 7, 8),
#             (0, 3, 6), (1, 4, 7), (2, 5, 8),
#             (0, 4, 8), (2, 4, 6)
#         ]
#
#         for pos in win_positions:
#             if self.cells[pos[0]].symbol != " " and self.cells[pos[0]].symbol == self.cells[pos[1]].symbol == self.cells[pos[2]].symbol:
#                 return True
#         return False
#
#     def reset_board(self):
#         for cell in self.cells:
#             cell.symbol = " "
#             cell.occupied = False
#
#
# class Player:
#     def __init__(self, name, symbol):
#         self.name = name
#         self.symbol = symbol
#         self.wins = 0
#
#
#     def make_move(self):
#         while True:
#             try:
#                 move = int(input(f"{self.name}, введите номер клетки"
#                                  f"для вашего хода(1 - 9): "))
#                 if move < 1 or move > 9:
#                     raise ValueError
#                 return move
#             except ValueError:
#                 print("Неправильный ввод. Пожалуйста, введите число от 1 до 9.")
#
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.players = [player1, player2]
#         self.board = Board()
#
#
#     def launch_move(self, player):
#         while True:
#             self.board.display_board()
#             cell_number = player.make_move()
#             if self.board.change_cell(cell_number, player.symbol):
#                 if self.board.check_game_over():
#                     return True
#                 return False
#             print("Клетка занята. Сделайте другой ход.")
#
#
#     def play_one_game(self):
#         print("Игра началась!")
#         while True:
#             for player in self.players:
#                 if self.launch_move(player):
#                     self.board.display_board()
#                     print(f"Поздравляем, {player.name}! Вы выиграли!")
#                     player.wins += 1
#                     return
#                 if all(cell.occupied for cell in self.board.cells):
#                     self.board.display_board()
#                     print("Ничья!")
#                     return
#
#     def start_games(self):
#         print("Добро пожаловать в игру Крестики-Нолики!")
#         while True:
#             self.board.reset_board()
#             self.play_one_game()
#             print(f"Счет: {self.players[0].name} -"
#                   f"{self.players[0].wins}, {self.players[1].name} -"
#                   f"{self.players[1].wins}")
#             again = input("Хотите продолжить игру? (да/нет): ")
#             if again.lower() != 'да':
#                 print("Спасибо за игру!")
#                 break
#
#
# player1 = Player("Игрок 1", 'X')
# player2 = Player("Игрок 2", 'O')
#
# game = Game(player1, player2)
#
# game.start_games()
#
#
# # Задача 4. Создание класса-фабрики для животных
class Animal:
    def __init__(self, name: str):
        self.name = name


    def speak(self):
        raise NotImplementedError("Subclasses should implement this method")


    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed


    def speak(self):
        return "Woof!"


    def __str__(self):
        return f"{super().__str__()} of breed {self.breed}"



class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color


    def speak(self):
        return "Meow!"


    def __str__(self):
        return f"{super().__str__()} with color {self.color}"



class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        animal_classes = {
            'Dog': Dog,
            'Cat': Cat
        }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")



dog = AnimalFactory.create_animal('Dog', 'Buddy', 'Golden Retriever')
cat = AnimalFactory.create_animal('Cat', 'Whiskers', 'Black')

print(dog)
print(cat)
print(dog.speak())
print(cat.speak())