class House:

    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует! Лифты не летают! Куда вы вообще нажали?! Здесь даже такой кнопки нет!')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

pythonhouse = House('ЖК на ул. Питонов, 42', 22)
natrixhouse = House('Дом на пр. Ужей, 17', 14)

print(pythonhouse)
print(natrixhouse)

print(len(pythonhouse))
print(len(natrixhouse))