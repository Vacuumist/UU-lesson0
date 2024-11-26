class House:

    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history += [args[0]]
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def __del__(self):
        print(f'"{self.name}" cнесён, но он останется в истории.')

pythonhouse = House('ЖК на ул. Питонов, 42', 12)
print(House.houses_history)
natrixhouse = House('Дом на пр. Ужей, 17', 14)
print(House.houses_history)
viperhouse = House('Особняк на пл. Гадюк, 6', 10)
print(House.houses_history)

del natrixhouse
del viperhouse

print(House.houses_history)
