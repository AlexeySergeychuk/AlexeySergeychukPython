# --------------------------------1---------------------------------
import time
class TrafficLight():

    __color = 'Цвет'

    def running(self):
        c = 0
        while c < 10:
            __color = 'Красный'
            print(f'\033[41m{__color}')
            time.sleep(7)
            __color = 'Желтый'
            print(f'\033[43m{__color}')
            time.sleep(2)
            __color = 'Зеленый'
            print(f'\033[42m{__color}')
            time.sleep(4)
            c += 1

sometraffic = TrafficLight()
sometraffic.running()

# --------------------------------2---------------------------------
class Road():

    def __init__(self, _length, _width, mass = 25, depth = 5):
        self._length = _length
        self._width = _width
        self.mass = mass
        self.depth = depth

    def countvalue(self):
        print(f' Масса асфальта, необходимая для покрытия полотна: '
              f'{int((self._length * self._width * self.mass * self.depth) / 1000)} т')

someroad = Road(20, 5000)
someroad.countvalue()

# -----------------------------------3--------------------------------

class Worker():

    moneydict = {"wage": 100, "bonus": 200}

    def __init__(self, name, surname, position, _income = None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = Worker.moneydict.values()

class Position(Worker):

    def getfullname(self):
        fullname = self.name + " " + self.surname
        return fullname

    def get_total_income(self):
        total_income = sum(Worker.moneydict.values())
        return total_income


Someman = Position('Piter', 'Parker', 'Bankir')
print(Someman.getfullname())
print(Someman.get_total_income())

# ----------------------4----------------------------

import random

class Car:

    def __init__(self, speed, color, name, is_polise = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f'{self.name} moving')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self):
        destiny = random.randrange(1,4)
        if destiny == 1:
            print(f'{self.name} turn left')
        if destiny == 2:
            print(f'{self.name} turn right')
        if destiny == 3:
            print(f'{self.name} goes forward')
        if destiny == 4:
            print(f'{self.name} turn around')

    def show_speed(self):
        somespeed = random.randrange(5, self.speed)
        print(f'Текущая скорость {self.name} : {somespeed}')


class SportCar(Car):

    def somemethod(self):
        pass

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise = True)
        self.is_polise = True

class TownCar(Car):

    def __init__(self, speed, color, name, is_polise = False):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        somespeed = random.randrange(5, self.speed)
        if somespeed <= 60:
            print(f'Текущая скорость автомобиля: {somespeed}')
        else:
            print(f'Текущая скорость автомобиля: {somespeed}. ВНИМАНИЕ! Вы нарушаете скоростной режим!')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_polise = False):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        somespeed = random.randrange(5, self.speed)
        if somespeed <= 40:
            print(f'Текущая скорость автомобиля: {somespeed}')
        else:
            print(f'Текущая скорость автомобиля: {somespeed}. ВНИМАНИЕ! Вы нарушаете скоростной режим!')


Porshe = SportCar(300, 'white', 'Panamera')
Porshe.go()
Porshe.stop()
Porshe.turn()
Porshe.show_speed()

Reno = PoliceCar(130, 'blue', 'Logan', True)
Reno.go()
Reno.stop()
Reno.turn()
Reno.show_speed()

Niva = TownCar(120, 'red', '4x4')
Niva.go()
Niva.stop()
Niva.turn()
Niva.show_speed()

Kamaz = WorkCar(100, 'grey', 'D')
Kamaz.go()
Kamaz.stop()
Kamaz.turn()
Kamaz.show_speed()

# -----------------------------5-----------------------------

class Stationery:

    def __init__(self, title):
        self.title = title

    def drow(self):
        print('Запуск отрисовки')


class Pencil(Stationery):

    def drow(self):
        print(f'Отрисовка карандашом {self.title}')


class Pen(Stationery):

    def drow(self):
        print(f'Отрисовка ручкой {self.title}')


class Handle(Stationery):

    def drow(self):
        print(f'Отрисовка маркером {self.title}')


somepen = Pen('Parker')
somepen.drow()

somepensil = Pencil('Дружба')
somepensil.drow()

somehandle = Handle('SuperHandle')
somehandle.drow()
