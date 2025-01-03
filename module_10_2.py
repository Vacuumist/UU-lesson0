import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def __days_word(self, days):    # Дополнительная функция для корректного окончания слова при выводе дней.
        if days % 10 == 1 and days % 100 != 11:
            return 'день'
        elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
            return 'дня'
        else:
            return 'дней'

    def __enemies_word(self, enemies):  # Дополнительная функция для корректного окончания слова при выводе воинов.
        if enemies % 10 == 1 and enemies % 100 != 11:
            return 'воин'
        elif enemies % 10 in (2, 3, 4) and enemies % 100 not in (12, 13, 14):
            return 'воина'
        else:
            return 'воинов'

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            if enemies > self.power:
                enemies -= self.power
            else:
                enemies = 0
            days += 1
            print(f'{self.name} сражается {days} {self.__days_word(days)}, '
                  f'осталось {enemies} {self.__enemies_word(enemies)}.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} {self.__days_word(days)}!')


first_knight = Knight('Сэр Ланцелот', 9)
second_knight = Knight('Сэр Галахад', 17)

first_knight.start()
sleep(0.2)  # Небольшая задержка, чтобы потоки не пытались вывести информацию в консоль одновременно
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')