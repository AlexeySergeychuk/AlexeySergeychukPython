with open('test6.txt', 'r', encoding='utf-8') as file6:
    firstlist = file6.readlines()

for i in range(len(firstlist)):
    '''заменяем ':' на '(' и делаем первичный сплит по этому символу'''
    firstlist[i] = firstlist[i].replace(':', '(').split('(')
'''этот принт не нужен и оставлен для того что бы показать наглядно как после первого сплита выглядит список'''
print(firstlist)
'''создаем пустой словарь'''
findict = dict()
for i in range(len(firstlist)):
    '''добавляем в словарь ключи с названиями предметов, значения пока пустые'''
    findict.update({firstlist[i][0]: None})

'''далее цикл в цикле перебирают оба уровня вложенности в словаре, и делают дополнительный сплит что бы все цифры стали
отдельными значениями'''
for i in range(len(firstlist)):
    for j in range(len(firstlist[i])):
        firstlist[i][j] = firstlist[i][j].split()
'''этот принт тоже не нужен и оставлен для того что бы показать наглядно как после второго сплита выглядит список'''
print(firstlist)
'''cоздаем счетчик для сложеия чисел по каждому предмету'''
c = 0
''' запускаем тройной цикл что бы охватить три уровня вложенности, образовавшихся после второго сплита'''
for i in range(len(firstlist)):
    for j in range(len(firstlist[i])):
        for k in range(len(firstlist[i][j])):
            '''через условие пропускаем только те строковые значения, которые на самом деле числа'''
            if (firstlist[i][j][k].isdigit()):
                '''суммируем в переменную "c" все числа из первой вложенности, то есть из одного предмета'''
                c += int(firstlist[i][j][k])
    '''присваиваем ключу значение, подсчитанное в переменную "c". Ключ определяется как название предмета [i][0][0],
     то есть первый объект на первом уровне вложенности'''
    findict[firstlist[i][0][0]] = c
    '''обнуляем пеерменную 'c' что бы в новом предмете начать подсчет сначала'''
    c=0
print(findict)