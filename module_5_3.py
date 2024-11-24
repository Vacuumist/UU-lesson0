class House:

    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and isinstance(other, House)

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors and isinstance(other, House)

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors and isinstance(other, House)

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors and isinstance(other, House)

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors and isinstance(other, House)

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors and isinstance(other, House)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
        return self

    def __rsub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
        return self

    def __isub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
        return self

    def __mul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
        return self

    def __rmul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
        return self

    def __imul__(self, value):
        if isinstance(value, int):
            self.number_of_floors *= value
        return self

    def __truediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value  # Здесь деление с отстатком, т.к. обычное деление не имеет смысла
        return self

    def __rtruediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value  # Здесь деление с отстатком, т.к. обычное деление не имеет смысла
        return self

    def __itruediv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value  # Здесь деление с отстатком, т.к. обычное деление не имеет смысла
        return self

    def __floordiv__(self, value): # Можно использовать при подсчёте кол-ва полных секций по несколько этажей
        if isinstance(value, int):
            self.number_of_floors //= value
        return self

    def __rfloordiv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value
        return self

    def __ifloordiv__(self, value):
        if isinstance(value, int):
            self.number_of_floors //= value
        return self

    def __mod__(self, value):
        if isinstance(value, int):
            self.number_of_floors %= value
        return self

    def __rmod__(self, value):
        if isinstance(value, int):
            self.number_of_floors %= value
        return self

    def __imod__(self, value):
        if isinstance(value, int):
            self.number_of_floors %= value
        return self

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует! Лифты не летают! Куда вы вообще нажали?! Здесь даже такой кнопки нет!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

pythonhouse = House('ЖК на ул. Питонов, 42', 12)
natrixhouse = House('Дом на пр. Ужей, 17', 14)

print(pythonhouse)
print(natrixhouse)
print(pythonhouse == natrixhouse)

pythonhouse = pythonhouse + 2
print(pythonhouse)
print(pythonhouse == natrixhouse)

pythonhouse += 7
print(pythonhouse)

natrixhouse= 7 + natrixhouse
print(natrixhouse)

print(pythonhouse > natrixhouse)
print(pythonhouse >= natrixhouse)
print(pythonhouse < natrixhouse)
print(pythonhouse <= natrixhouse)
print(pythonhouse != natrixhouse)
print()

fl_seg = 5
print(f'''"{natrixhouse.name}" можно разделить 
на {(natrixhouse // fl_seg).number_of_floors} секций по {fl_seg} этажей 
и одну секцию в {(natrixhouse % fl_seg).number_of_floors} этажа.''')