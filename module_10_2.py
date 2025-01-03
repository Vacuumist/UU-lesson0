import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def __days_word(self, days):    # Дополнительная функция для корректного окончания слова при выводе кол-ва дней.
        if days % 10 == 1 and days % 100 != 11:
            return 'день'
        elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
            return 'дня'
        else:
            return 'дней'

    def __enemies_word(self, enemies):  # Дополнительная функция для корректных окончаний слов при выводе воинов.
        if enemies % 10 == 1 and enemies % 100 != 11:
            return f'остался {enemies} воин'
        elif enemies % 10 in (2, 3, 4) and enemies % 100 not in (12, 13, 14):
            return f'осталось {enemies} воина'
        else:
            return f'осталось {enemies} воинов'

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
            print(f'{self.name} сражается {days} {self.__days_word(days)}, {self.__enemies_word(enemies)}.\n', end='')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} {self.__days_word(days)}!\n', end='')
        '''Здесь в конце f-строк добавлено <\n', end=''> для гарантированного вывода информации из параллельного 
        потока на новой строке. Без этого окончания строки иногда в консоль выводится на одной строке информация 
        из двух потоков, а только затем - два переноса на новую строку'''

first_knight = Knight('Сэр Ланцелот', 9)
second_knight = Knight('Сэр Галахад', 17)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')