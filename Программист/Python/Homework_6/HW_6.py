# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a = int(input('Input a first number: '))
# list1 = [a]
# d = int(input('Input a difference: '))
# n = int(input('Quantity of elements: '))
#
# for i in range(n-1):
#     an = a + (i - 1) * d
#     list1.append(an)
#
# print(list1)

# Определить индексы элементов массива(списка), значения которых принадлежат заданному диапазону(т.е.не
# меньше заданного минимума и не больше заданного максимума)

# import random
# list1 = [random.randint(1,10) for _ in range(10)]
# print(list1)
# min_ = int(input('Input min: '))
# max_ = int(input('Input max: '))
#
# for i in range(len(list1)):
#     if min_ <= list1[i] <= max_:
#         print(i, end=', ')