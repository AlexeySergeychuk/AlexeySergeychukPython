# -------------------------1---------------------------
# from sys import argv
#
# name, time, pricetime, salary = argv
#
# print((float(time) * int(pricetime))+int(salary))

# ---------------------------2---------------------------

# somelist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#
#
# newlist = [somelist[el] for el in range(1, len(somelist)) if somelist[el] > somelist[el-1]]
# print(newlist)
#
# -----------------------------3---------------------------
#
# somelist = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
# print(somelist)
#
# # ---------------------------4------------------------------------

# somelist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# newlist = [somelist[el] for el in range(len(somelist)) if somelist.count(somelist[el]) == 1]
# print(newlist)
#
# -------------------------------5----------------------------------
#
# from functools import reduce
#
# def my_func(prev_el, el):
#     return prev_el * el
#
# somelist = [el for el in range(100, 1001, 2)]
#
# print(reduce(my_func, somelist))

# -------------------------------6.1----------------------------------
#
# from itertools import count
#
# for el in count(4):
#     if el >12:
#         break
#     else:
#         print(el)

# ---------------------------------6.2-----------------------------------

# from itertools import cycle
#
# somelist = [1, 'some', True]
#
# counter = 0
# for el in cycle(somelist):
#     if counter > 10:
#         break
#     else:
#         print(el)
#         counter += 1
#
# ----------------------------------7-----------------------------------

# from math import factorial
#
# somelist = [1,3,5,7]
# def factfun(someint):
#     for i in someint:
#         yield factorial(i)
#
# a = factfun(somelist)
# for i in a:
#     print(i)

