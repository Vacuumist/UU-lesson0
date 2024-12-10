from math import pi

class Figure:
    sides_count = 0

    def __init__(self, colour, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count #При передаче некорректного числа сторон формируется единичная фигура
        else:
            self.__sides = list(sides)
        if len(colour) == 3 and self.__is_valid_colour(*colour):
            self.__colour = colour
        else:
            self.__colour = []
        self.filled = self.__colour != []     # Если фигура имеет цвет, значит она закрашена.

    def get_colour(self):
        return list(self.__colour)

    def __is_valid_colour(self, r, g, b):
        for c in (r, g, b):
            if not isinstance(c, int) or c < 0 or c > 255:
                return False
        return True

    def set_colour(self, r, g, b):
        if self.__is_valid_colour(r, g, b):
            self.__colour = [r, g, b]
            self.filled = True

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for s in sides:
            if isinstance(s, int) or s < 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return len(self) / (2 * pi)

    def get_area(self):
        return pi * self.__radius() ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, colour, *sides):
        if len(sides) == 3:
            # Проверка на соответствие длин сторон неравенству треугольника:
            if sides[0] > sides[1] + sides[2] or sides[1] > sides[0] + sides[2] or sides[2] > sides[0] + sides[1]:
                sides = [1, 1, 1]
        super().__init__(colour, *sides)

    def get_area(self):
        s = self.get_sides()
        hp = sum(s) / 2
        area = (hp * (hp - s[0]) * (hp - s[1]) * (hp - s[2])) ** 0.5
        return area

class Cube(Figure):
    sides_count = 12

    def __init__(self, colour, *side):
        if len(side) == 1:
            super().__init__(colour, *side * self.sides_count)
        else:
            super().__init__(colour, [1] * self.sides_count)

    def get_volume(self):
        return (len(self) / self.sides_count) ** 3

# №1. Проверки кода из домашнего задания:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_colour(55, 66, 77) # Изменится
print(circle1.get_colour())
cube1.set_colour(300, 70, 15) # Не изменится
print(cube1.get_colour())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())

# №2. Дополнительные проверки кода для круга:
circle2 = Circle((390,), 34) # Объявление цвета в некорректном формате
print(circle2.get_colour()) # Пустой список
print(circle2.filled)       # False - круг не закрашен
print(len(circle2))         # Длина окружности - число
print(circle2.get_area())   # Площадь круга
circle2.set_colour(141, 34, 87)    # Окрашивание в корректный цвет
circle2.set_sides(13)                       # Новый размер (длина окружности)
print(circle2.get_colour()) # Пустой список
print(circle2.filled)       # True - круг закрашен
print(len(circle2))         # Новая длина окружности
print(circle2.get_area())   # Новая площадь круга
circle3 = Circle((90, 230, 34), 34, 6, 0) # Передача некорректного числа параметров
print(circle3.get_sides()) # Переданные значения проигногированы, создан круг с длиной окружности 1

# №3. Дополнительные проверки кода для треугольника:
tri1 = Triangle((132, 56, 93), 3, 6, 7, 0)  # Передача некорректного числа параметров
tri2 = Triangle((132, 56, 93), 3, 6, 70)     # Длины сторон не соответствуют неравенству треугольника
print(tri1.get_sides(), tri2.get_sides())                # Созданы треугольники со сторонами 1
tri1.set_sides(5, 2, 6)                   # Изменение сторон треугольника
tri2.set_colour(255, 255, 255)              # Изменение цвета на белый
print(tri1.get_sides())                              # Изменения были внесены
print(tri2.get_colour())
tri3 = Triangle((0, 0, 0), 3, 4, 5)     # Передача корректных значений
print(tri3.get_sides())                              # Создан треугольник с корректными длинами сторон
print(tri3.get_area())                               # Площадь треугольника
print(tri3.get_colour(), tri3.filled)                # Треугольник закрашен в чёрный цвет

# №4. Дополнительные проверки кода для куба:
cube2 = Cube((), 30)                                    # Куб без указания цвета и указанием длины ребра
print(cube2.get_sides(), cube2.get_colour(), cube2.filled)    # Создан незаполненный куб с указанной длиной ребра
print(cube2.get_volume())
cube3 = Cube((43, 60, 23), 23, 23, 23)           # Некорректное указание длины рёбер
print(cube3.get_sides(), cube3.get_colour(), cube3.filled)    # Создан заполненный куб с длиной ребра 1
print(cube3.get_volume())                                     # Объём куба
