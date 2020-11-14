#1
x = [1, 2.3, 'fg', None, [1,2], {1,3}]
for i in range(len(x)):
    print(type(x[i]), end=',')
#2
y=input('Введите что-нибудь: ').split()
for i in range(len(y) - 1):
    if i%2 == 0 or i == 0:
        j = y[i]
        y[i]= y[i +1]
        y[i + 1]=j
print(y)
#3.1
m = int(input('Введите номер месяца: '))
monthlist = ['Зима', 'Весна', 'Лето', 'Осень']
if m in (12, 1, 2):
    print(monthlist[0])
elif m in (3, 4, 5):
    print(monthlist[1])
elif m in (6, 7, 8):
    print(monthlist[2])
elif m in (9, 10, 11):
    print(monthlist[3])
else:
    print('Вы ввели не номер месяца: ')
#3.2
m = int(input('Еще раз введите номер месяца: '))
monthdict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето',
             8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(monthdict.get(m))
#4
text=input('Введите текст через пробелы: ').split()
for i in range(len(text)):
    print(text[i][:10])
#5
my_list = [9, 9, 8, 6, 3, 2, 2, 1]
l = int(input('Введите рейтинг от 1 до 10: '))
my_list.append(l)
my_list.sort()
my_list.reverse()
print(my_list)

#6
data = [[1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}],
[2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}],
[3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'}]]

item = input('Введите название: ')
price = input("Введите цену: ")
count1 = input("Введите количество: ")
ed = input("Введите единицу измерения: ")
datanew = {'название': item, 'цена': price, 'количество': count1, 'ед': ed}
x = len(data) + 1
data.append([x])
data[x-1].append(datanew)


bigdataname = {'название': []}
for i in range(len(data)):
    t = data[i][1].get('название')
    bigdataname['название'].append(t)
print(bigdataname)

bigdataprice = {'цена': []}
for i in range(len(data)):
    t = data[i][1].get('цена')
    bigdataprice['цена'].append(t)
print(bigdataprice)

bigdatacount = {'количество': []}
for i in range(len(data)):
    t = data[i][1].get('количество')
    bigdatacount['количество'].append(t)
print(bigdatacount)

bigdataed = {'ед': []}
for i in range(len(data)):
    t = data[i][1].get('ед')
    bigdataed['ед'].append(t)
print(bigdataed)
