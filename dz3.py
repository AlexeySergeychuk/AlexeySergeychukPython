#--------------------------1------------------------
#
# def delenie(num1, num2):
#     """Маленькая примитавная функция из первого задания"""
#     try:
#         fin = num1/num2
#         print(fin)
#     except:
#         ZeroDivisionError = print("Don't try divide by 0")

# delenie(int(input('First number: ')), int(input('Second number: ')))

#--------------------------2--------------------------
#
# def char(**kwargs):
#     """Функция выводит данные по пользователю в одну строку"""
#     for i in kwargs.values():
#         print(i, end=',')

# char(Имя="Алексей", Фамилия="Васильев", date='04.05.1977', City='Moscow', email='example@examples.ed')
#

# ---------------------------2.1-------------------------

# def char1(**kwargs):
#     return '/'.join(kwargs.values())
#
#
# print(char1(gg='2',    sdg ='334'))
#



# --------------------------3---------------------------

# def sumtwomax(num_1, num_2, num_3):
#     l=[num_1, num_2, num_3]
#     try:
#         l.remove(min(l))
#         return (sum(l))
#     except TypeError:
#         return 'Введите числа!_'
#
#
#
# print(sumtwomax(2,5,9))

# ----------------------------4.1-----------------------------

# def my_func():
#     """Функция возводит положительное число в отрицательную степень"""
#     while True:
#         x = int(input('First number +: '))
#         y = int(input('Second number -: '))
#         if x > 0 and y < 0:
#             print(x ** y)
#             break
#         else:
#             print("Enter true numbers!")
#
# my_func()

# -----------------------------4.2------------------------------

# def my_func1():
#     """Функция возводит положительное число в отрицательную степень"""
#     while 1:
#         x = int(input('First number: '))
#         y = int(input('Second number: '))
#         if x > 0 and y < 0:
#             j=1
#             for _ in range(abs(y)):
#                 j *= x
#             print(1/j)
#             break
#         else:
#             print("Enter true numbers!")
#
# my_func1()

#-------------------------------5-------------------------------

# final = 0 # переменная будет хранить сумму чисел
# while True:
#     num = input('Введите числа через пробел. Для завершения введите маленькую "q": ').split()
#     find = num.count('q') # ловим введенное "q" что бы вовремя завершить цикл
#     if find == 0: #попадаем в основную ветку если пользователь ввел только числа и суммируем их циклом
#         for i in range(len(num)):
#             num[i] = int(num[i])
#         final+=sum(num)
#         print(final)
#     else:
#         num.remove('q') #если пользователь ввел q, удаляем ее из пеерменной и циклом последний раз суммируем числа
#         for j in range(len(num)):
#             num[j] = int(num[j])
#         final+=sum(num)
#         print(final)
#         break

#-------------------------------6---------------------------------

# def inf_func(word):
#     """Функция возвращает слово с большой буквы"""
#     counter = 0
#     for i in range(len(word)):
#         m = ord(word[i])
#         if m >= 97 and m <= 122: #проверка на маленькие латинские
#             counter += 1 #счетчик для отлова слов, полностью состоящих из латиницы
#         else:
#             print('НЕПРАВИЛЬНОЕ_СЛОВО', end=' ') #если в слове есть символы, отличные от строчных латинских
#             break
#     if counter == len(word): #если слово полностью латинское, то печатаем
#         print(word[0].upper() + word[1:], end=' ') #склеиваем первую большую букву с остальными малыми
#
#
# sentence = input('Введите предложение из маленьких латинских букв: ').split() #запишем предложение в список
# for i in range(len(sentence)):
#     inf_func(sentence[i]) #отработаем функцию на каждом слове отдельно


