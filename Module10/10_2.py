from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        enemy = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemy != 0:
            enemy = enemy - self.power
            if enemy < 0:
                print(f'{self.name} сражается {day+1} день (дня), осталось 0 воинов')
                print(f'{self.name} одержал победу спустя {day+1} дней(дня)!')
                break
            else:
                sleep(1)
                day += 1
                print(f'{self.name} сражается {day} день (дня), осталось {enemy} воинов')
                if enemy == 0:
                    print(f'{self.name} одержал победу спустя {day} дней(дня)!')
            # elif enemy < 0:
            #     break

first_knight = Knight('Sir Lancelot', 11)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')