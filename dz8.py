# -------------------------1------------------------------

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def number(cls, data):
        datalist = (data.split('-'))
        for i in range(len(datalist)):
            datalist[i] = int(datalist[i])
        return type(datalist[0]), datalist

    @staticmethod
    def valid(data):
        datalist1 = (data.split('-'))
        for i in range(len(datalist1)):
            datalist1[i] = int(datalist1[i])
        for i in range(3):
            d = 0
            if 32 < datalist1[0] > 0:
                d += 1
            elif datalist1[0] < 1 or datalist1[0] > 31:
                return 'Некорректная дата'
            elif 13 < datalist1[1] > 0:
                d+=1
            elif datalist1[1] > 12:
                return "Некорректный месяц"
            elif 2021 < datalist1[2] > 1900:
                d+=1
            elif d != 3:
                return 'Некорректный год'
            else: return 'Валидация пройдена успешно!'


print(Data.number('06-05-1989'))
mc = Data('02-14-1976')
print(mc.number('33-12-1976'))
print(Data.valid('03-13-1985'))
print(Data.valid('03-12-1888'))

# ---------------------------------2-----------------------------

class SecondDevizionByZero(Exception):
    def __init(self, txt):
        self.txt = txt

delvar = int(input('Введите делитель: '))

try:
    if delvar == 0:
        raise SecondDevizionByZero('Вы пытаетесь поделить на ноль!')
except ValueError:
    print('Вы ввели не число')
except SecondDevizionByZero:
    print('Не пытайтесь поделить на 0!')
else:
    print(10/delvar)


# -----------------------------------3-----------------------------------

class JustInt(Exception):
    def __init(self, txt):
        self.txt = txt

somelist = []
while 1:
    a = input('Введите число. Для выхода из программы введите "Stop": ')
    if 'Stop' in a or 'stop' in a:
        print(somelist)
        break
    try:
        if a.isdigit() == False:
            raise JustInt('Вы пытаетесь ввести НЕ число')
    except JustInt:
        print('ВВОДИТЕ ТОЛЬКО ЧИСЛА!')
    else:
        somelist.append(a)

# ----------------------------------7-----------------------------------------

'''Пощадите, двусторонняя пневмония не оставляет сил честно решить эту задачу.'''
class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

a = complex(3, 0.04)
b = complex(5, 3)

acom = ComplexNumbers(a)
acom1 = ComplexNumbers(b)

print(acom + acom1)
print(acom * acom1)

# ------------------------------4,5,6----------------------------------------
'''Запустался с конструкцией setter. Прошу помочь!.'''
class Sklad:
    list = []

    @staticmethod
    def counts():
        print(f'На складе содержится следующая продукция: {Sklad.list}')


class Equipment:
    def __init__(self, mark, name, year):
        self.mark = mark
        self.name = name
        self.year = year

    def addsklad(self):
        return Sklad.list.append([self.mark, self.name, self.year])

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        if self.year > 2021:
            self.year = 2021
        else:
            self.year = year

class Printer(Equipment):
    def __init__(self, mark, name, year, color):
        super().__init__(mark, name, year)
        self.color = color

class Scaner(Equipment):
    def __init__(self, mark, name, year, ip):
        super().__init__(mark, name, year)
        self.ip = ip

class Xerox(Equipment):
    def __init__(self, mark, name, year, someperk):
        super().__init__(mark, name, year)
        self.someperk = someperk

lasers = Printer('lasers', 'l2', 2025, 'red')
lasers.addsklad()
somexerox = Xerox('Xerox', 'R300', 2019, 'best Xerox')
somexerox.addsklad()
Sklad.counts()
