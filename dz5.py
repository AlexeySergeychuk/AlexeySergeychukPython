# ---------------------1----------------------

# with open("test1.txt", 'w') as file:
#     list = input('Введите данные для записи в файл: ').split()
#     for i in range(len(list)):
#         list[i] = str(list[i]+'\n')
#     file.writelines(list)

# ----------------------1.1------------------------
#
# with open('text2.txt', 'w') as file1:
#     while 1:
#         '''Перевод строки ниже необходим по двум причинам: перевести строку согласно условиям, и как IF'''
#         someline = (input('Введите строку, для завершения ничего не вводите: ')+'\n')
#         if len(someline) == 1: #если пользователь ничего не введет, то добавится наш символ "\n" и сработает условие
#             break
#         file1.writelines(someline)

# ----------------------2----------------------------

# with open('text2.txt', 'r') as file3:
#     try:
#         list=file3.readlines()
#         print(f'Количество строк в файле {file3.name}: {len(list)}')
#         counter = 1
#         for i in range(len(list)):
#             list[i] = list[i].split(' ')
#             print(f'Количество слов в строке {counter} : {len(list[i])}')
#             counter+=1
#     except SyntaxError:
#         print('Ошибка!')

# ------------------------3----------------------------

# from typing import Any, Tuple
#
# somedict = {}
# with open('test3.txt', 'r', encoding='utf-8') as file2:
#     for line in file2: #приводим данные к словарю с помощью цикла
#         key, value = line.split()
#         somedict[key] = float(value)
#
# list = []
# listsolary = []
#
# for keys, values in somedict.items(): #записываем в один список все доходы,а в другой по условию фамилии с низкой зп
#     listsolary.append(values)
#     if values < 20000:
#         list.append(keys)
#
# print(f'Cписок тех, кому давно пора поднять ЗП: {list}')
# print(f'Средняя ЗП среди работников: {sum(listsolary)/len(listsolary)}')

# ----------------------------4----------------------------

# with open('text4.txt', 'r', encoding='utf-8') as file3:
#     text = file3.readlines()
#     translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'} #создаем словарь
#     for i in range(len(text)): #преобразуем строку в список
#         text[i] = text[i].split()
#     for j in range(len(text)): #преобразуем нулевой объект в малые буквы что бы считать со словаря и меняем 'en' на 'ru'
#         text[j][0] = translate.get(text[j][0].lower()).capitalize() #capitalize делает первые буквы заглавными
#     for l in range(len(text)):
#         text[l].append('\n') # добавляем '/n' что бы записать каждый элемент списка в отдельную строку
#     for k in range(len(text)): #объединяем подэлементы в один элемент
#         text[k] = ' '.join(text[k])
#
#
# with open('text5.txt', 'w', encoding='utf-8') as file4: #записываем в файл
#     file4.writelines(text)

# # --------------------------5--------------------------------
#
# from random import randint
# with open('text6.txt', 'r+') as file5:
#     numbers = [randint(10, 20) for el in range(int(input('Введите число: ')))] #создаем спичок размера 'n'
#     for el in numbers:
#         file5.writelines(str(el)) #Цикл записывает числа в файл разделяя их пробелами
#         file5.writelines(' ')
#     file5.seek(0) #устанавливаем курсор в начало файла
#     counter = file5.read().split() #считываем числа из файла в лист
#     for i in range(len(counter)):
#         counter[i] = int(counter[i]) #приводим значения в списке к формату int
#     finalsum = sum(counter) #суммируем
#     print(f'Вот список чисел: {counter}')
#     print(f'Сумма чисел {finalsum}')
#
# ----------------------------6-------------------------------

# with open('test6.txt', 'r', encoding='utf-8') as file6:
#     firstlist = file6.readlines()
#
# for i in range(len(firstlist)):
#     '''заменяем ':' на '(' и делаем первичный сплит по этому символу'''
#     firstlist[i] = firstlist[i].replace(':', '(').split('(')
# '''этот принт не нужен и оставлен для того что бы показать наглядно как после первого сплита выглядит список'''
# print(firstlist)
# '''создаем пустой словарь'''
# findict = dict()
# for i in range(len(firstlist)):
#     '''добавляем в словарь ключи с названиями предметов, значения пока пустые'''
#     findict.update({firstlist[i][0]: None})
#
# '''далее цикл в цикле перебирают оба уровня вложенности в словаре, и делают дополнительный сплит что бы все цифры стали
# отдельными значениями'''
# for i in range(len(firstlist)):
#     for j in range(len(firstlist[i])):
#         firstlist[i][j] = firstlist[i][j].split()
# '''этот принт тоже не нужен и оставлен для того что бы показать наглядно как после второго сплита выглядит список'''
# print(firstlist)
# '''cоздаем счетчик для сложеия чисел по каждому предмету'''
# c = 0
# ''' запускаем тройной цикл что бы охватить три уровня вложенности, образовавшихся после второго сплита'''
# for i in range(len(firstlist)):
#     for j in range(len(firstlist[i])):
#         for k in range(len(firstlist[i][j])):
#             '''через условие пропускаем только те строковые значения, которые на самом деле числа'''
#             if (firstlist[i][j][k].isdigit()):
#                 '''суммируем в переменную "c" все числа из первой вложенности, то есть из одного предмета'''
#                 c += int(firstlist[i][j][k])
#     '''присваиваем ключу значение, подсчитанное в переменную "c". Ключ определяется как название предмета [i][0][0],
#      то есть первый объект на первом уровне вложенности'''
#     findict[firstlist[i][0][0]] = c
#     '''обнуляем пеерменную 'c' что бы в новом предмете начать подсчет сначала'''
#     c=0
# print(findict)
#
# --------------------------7--------------------------------

# import json
#
# with open('text7.txt', 'r', encoding='utf-8') as file7:
#     array = file7.readlines()
# array = [el.replace('\n', '') for el in array] #убираем '\n'
# array = [el.split() for el in array] #разбиваем строку по сплиту
# lastlist = [] #create final list
# somedict = dict() #create dict for company's structures
# allincome = 0 # var for sum income
# incomedict = dict() #create dict for sum inpomes
# for i in range(len(array)):
#     check = int(array[i][2])-int(array[i][3]) #вычисляем прибыль компаниии
#     somedict.update({array[i][0] : check}) #в словарь заносим компанию и ее фин результат
#     if check >= 0: #проверка на то что компания прибыльна
#         allincome += check #увеличиваем общую прибыль на прибыль текущей компании
# lastlist.append(somedict)
# incomedict.update({'Прибыль без учета аутсайдеров:' : allincome})
# lastlist.append(incomedict)
#
# with open('firstfile.json', 'w', encoding='utf-8') as jsonfile:
#     json.dump(lastlist, jsonfile, ensure_ascii=False)



