from threading import Thread, Lock
from time import sleep
from random import randint

lock = Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self): #100
        for i in range(100):
            income = randint(50, 500)
            self.balance += income
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f'Пополнение: {income}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            consumption = randint(50, 500)
            print(f'Запрос на {consumption}')
            if consumption <= self.balance:
                self.balance -= consumption
                print(f'Снятие: {consumption}, Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()