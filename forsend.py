class Sklad:
    somelist = []

    # skladdict = {Printer: 0, Scaner: 0, Xerox: 0}
    @staticmethod
    def counts():
        print(Sklad.somelist)


class Equipment:
    def __init__(self, mark, name, year):
        self.mark = mark
        self.name = name
        self.year = year

class Printer(Equipment):
    def __init__(self, mark, name, year, color):
        super().__init__(mark, name, year)
        self.color = color


    def addsklad(self):
        Sklad.somelist.append(self)

lasers = Printer('lasers', 'l2', 1986, 'red')
lasers.addsklad()
Sklad.counts()
print(Sklad.counts())
