from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.__free_tables = len(self.tables)

    def guest_arrival(self, *guests):
        n = min(len(self.tables), len(guests))
        for i in range(n):
            self.tables[i].guest = guests[i]
            self.__free_tables -= 1
            guests[i].start()
            print(f'{guests[i].name} сел за стол №{self.tables[i].number}.')
        for i in range(n, len(guests)):
            self.queue.put(guests[i])
            print(f'{guests[i].name} в очереди.')

    def serve_guests(self):
        while not self.queue.empty() or self.__free_tables < len(self.tables):
            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    self.__free_tables -= 1
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол №{table.number}.')
                if table.guest is not None and not table.guest.is_alive():
                    self.__free_tables += 1
                    print(table.guest.name, 'покушал(-а) и ушёл(ушла).')
                    print(f'Стол №{table.number} свободен.')
                    table.guest = None
            sleep(0.5)
        print('Все посетители накормлены.')

tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe.guest_arrival(*guests)
cafe.serve_guests()
