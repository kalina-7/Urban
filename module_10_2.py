import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        enemies = 100
        counter = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            time.sleep(1)
            counter += 1
            print(f'{self.name} сражается {counter} день(дня)..., осталось {enemies - self.power} воинов')
            enemies -= self.power
        print(f'{self.name} одержал победу спустя  {counter} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')