#№1
test = 1
#№2
time = int(input("Введите время в секундах: "))
hour = time // 3600
min = (time - hour*3600)//60
sec = (time - hour*3600)%60
print(f"{'%02d' % hour}:{'%02d' %min}:{'%02d' %sec}")
#№3
data = input("Введите число: ")
print(int(chislo)+int(2*chislo)+int(3*chislo))
#№4
bigdata = input("Введите целое положительное число: ")
the_biggest_numeral=0
n=0 #счетчик, необходимый для передвижения по символам введенного пользоватеелм числа в формате str
while n<=len(bigdata)-1: # запустим цикл на количество итераций, равное количеству цифр введенных пользователем
    if int(bigdata[n]) > the_biggest_numeral: #сверяем текущую цифру введенного пользователем числа с наибольшей (в первой итерации с нулем)
        the_biggest_numeral = int(bigdata[n]) #если текущее число больше найденных ранее, записываем его в переменную
        n+=1 #увеличиваем счетчик
    elif int(bigdata[n]) <= the_biggest_numeral:
        n+=1
print(the_biggest_numeral)
#№5
income = int(input("Введите выручку: "))
costs = int(input('Введите расход: '))
if income > costs:
    print(f'Ваш доход больше расхода на {income-costs}')
    print(f'Ваша рентабельность: {(income-costs)/income*100}%')
    countpeople = int(input("Введите количество сотрудников: "))
    print(f'Прибыль фирмы на одного сотрудника равна {(income-costs)/countpeople}')
if income < costs:
    print(f"Ваш доход меньше расхода на {costs-income}")
if income == costs:
    print('Ваши доходы и расходы совпадают')
#№6
a=int(input('Введите стартовую дистанцию: '))
b=int(input('Введите конечную дистанцию: '))
d=0 #счетчик дней
while a <= b:
    a*=1.1
    d+=1
print(d+1)



