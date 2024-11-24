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

def floor_section(building, floors_in_section):
    if floors_in_section <= 0 or floors_in_section > building.number_of_floors:
        return f'Введено некорректное число этажей. Допускаются значения от 1 до {building.number_of_floors}'
    else:
        if floors_in_section % 10 == 1 and floors_in_section != 11:
            fs = 'у'
        elif 2 <= floors_in_section % 10 <= 4 and not 12 <= floors_in_section <= 14:
            fs = 'а'
        else:
            fs = 'ей'
        sect_num = building.number_of_floors // floors_in_section
        if sect_num == 0:
            sn = ''
        elif sect_num % 10 == 1 and sect_num != 11:
            sn = f'{sect_num} секцию по {floors_in_section} этаж{fs}'
        elif 2 <= sect_num % 10 <= 4 and not 12 <= sect_num <= 14:
            sn = f'{sect_num} секции по {floors_in_section} этаж{fs}'
        else:
            sn = f'{sect_num} секций по {floors_in_section} этаж{fs}'
        residue_floors = building.number_of_floors % floors_in_section
        if residue_floors == 0:
            rf = ''
        elif residue_floors % 10 == 1 and residue_floors != 11:
            rf = f'одну секцию в {residue_floors} этаж'
        elif 2 <= residue_floors % 10 <= 4 and not 12 <= residue_floors <= 14:
            rf = f'одну секцию в {residue_floors} этажа'
        else:
            rf = f'одну секцию в {residue_floors} этажей'
        if sect_num != 0 and residue_floors != 0:
            ee = ' и '
        else:
            ee = ''
        return f'"{building.name}" можно разделить на {sn}{ee}{rf}.'

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

seq1 = int(input(f'Сколько будет этажей в секции у объекта "{pythonhouse.name}"?   '))
seq2 = int(input(f'Сколько будет этажей в секции у объекта "{natrixhouse.name}"?   '))
print(floor_section(pythonhouse, seq1))
print(floor_section(natrixhouse, seq2))
print()

pythonhouse *= int(input(f'Во сколько раз увеличить высоту у объекта "{pythonhouse.name}"?   '))
natrixhouse += int(input(f'Сколько этажей добавить объекту "{natrixhouse.name}"?   '))
print('Теперь', floor_section(pythonhouse, seq1))
print('Теперь', floor_section(natrixhouse, seq2))