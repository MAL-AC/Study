# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

import random
list1 ={random.randint(1,10) for _ in range(10)}
print(list1)
list2 ={random.randint(1,10) for _ in range(10)}
print(list2)

print(list1 & list2)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# import random
# list1 =[random.randint(1,10) for _ in range(5)]
# print(list1)
# max_ = 0
# for i in range(len(list1)-1):
#     if max_ < list1[i] + list1[i-1] + list1[i+1]:
#         max_ = list1[i] + list1[i - 1] + list1[i + 1]
# if max_ < list1[0] + list1[-1] + list1[-2]:
#     max_ = list1[0] + list1[-1] + list1[-2]
# print(max_)


