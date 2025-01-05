import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = int()

    def deposit(self):
        for _ in range(100):
            dep = randint(50, 500)
            self.balance += dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {dep}. \tБаланс: {self.balance}\n', end='')
            sleep(0.001)

    def withdraw(self):
        for _ in range(100):
            wdr = randint(50, 500)
            print(f'Запрос на: {wdr}.\n', end='')
            if wdr <= self.balance:
                self.balance -= wdr
                print(f'Снятие: {wdr}. \t\tБаланс: {self.balance}\n', end='')
            else:
                print('Запрос отклонён, недостаточно средств.\n', end='')
                self.lock.acquire()
            sleep(0.001)


urbank = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(urbank,))
th2 = threading.Thread(target=Bank.withdraw, args=(urbank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {urbank.balance}')
