# --------------------------------1------------------------------
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        finallist = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                finallist += f"{self.matrix[i][j]} "
            finallist += '\n'
        return finallist


    def __add__(self, other):
        addmatrix = []
        halfmatrix = []

        '''Конструкция проверяет размерность двух матриц. Если одна больше другой, в меньшую записывается список из 
        нулей нужно размерности (проверка по размеру второго уровня вложенности).'''
        if len(self.matrix) > len(other.matrix):
            test = other.matrix
            lens = len(self.matrix[0])
            templist = []
            for i in range(lens):
                templist.append(0)
            test.append(templist)
        if len(other.matrix) > len(self.matrix):
            test = self.matrix
            lens = len(other.matrix[0])
            templist = []
            for i in range(lens):
                templist.append(0)
            test.append(templist)
        if len(self.matrix) == len(other.matrix):
            for i in range(len((self.matrix))):
                for j in range(len(self.matrix[i])):
                    halfmatrix.append(self.matrix[i][j]+other.matrix[i][j])
                addmatrix.append(halfmatrix)
                halfmatrix = []
            return addmatrix



matrix_1 = Matrix([[0,8,2],[2,1,2]])
matrix_2 = Matrix([[2,4,1],[3,1,2],[3,2,5]])

print(matrix_1)
print(matrix_1 + matrix_2)

# ---------------------------------2---------------------------------

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def rashod(self):
        pass
    def __add__(self, other):
        return self.rashod + other.rashod

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def rashod(self):
        return ((self.v / 6.5 + 0.5) * 50)
        '''Формула в методичке выдает значения расхода ткани на пальто и костюм разного порядка. 
        Добавил на глаз множитель 50 для пальто.'''

class Dress(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def rashod(self):
        return (self.h * 2 + 0.3)


palto_1 = Coat(50)
print(palto_1.rashod)

kostum_1 = Dress(185)
print(kostum_1.rashod)

print(palto_1 + kostum_1)

# --------------------------3----------------------------

class Cell:
    def __init__(self, amount, coun = 0):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __mul__(self, other):
        return self.amount * other.amount

    def __sub__(self, other):
        if self.amount >= other.amount:
            return self.amount - other.amount
        else:
            return other.amount - self.amount

    def __floordiv__(self, other):
        return self.amount // other.amount

    def makeorder(self, coun):
        a = self.amount // coun
        b = self.amount % coun
        somestr = ''
        for i in range(a):
            somestr+='*'*coun+'\n'
        somestr +='*'*b
        return somestr

cell_1 = Cell(22)
cell_2 = Cell(5)
cell_3 = Cell(7)

print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
print(cell_3.makeorder(6))

