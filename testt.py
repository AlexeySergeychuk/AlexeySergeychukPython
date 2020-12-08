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


