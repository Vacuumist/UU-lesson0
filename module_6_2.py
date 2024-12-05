class Vehicle:
    __COLOR_VARIANTS = ['синий', 'красный', 'зелёный', 'чёрный', 'фисташковый']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = int(power)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзы сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'синий', 500)
vehicle1.print_info()
vehicle1.set_color('розовый')
vehicle1.set_color('ФИСТАШКОВЫЙ')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
