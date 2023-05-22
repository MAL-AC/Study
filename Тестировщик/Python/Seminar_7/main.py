# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) if values == transformed_values:
# print(‘ok’) else:
# print(‘fail’)
# Вывод:
# ok


# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте:
# вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде
#
# 13:36
# Задача No49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(list1):
#     max_elips = max(list1, key = lambda x: (x[0] * x[1]) * (x[0] != x[1]))
#     return max_elips
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Написать функцию, которая принимает список строк и возвращает список строк,
# содержащих только одно слово, с использованием лямбда-функции:
# python
# Copy code
#
#
# strings = ["Hello, world!", "This is a sentence.", "Another sentence", "Other"]
#
# def list_(string):
#     return list(filter(lambda x: not " " in x, string))
#
# print(list_(strings))


# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.
#
# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
#
# n = 4
# lst = [[0 for y in range(n)] for i in range(n)]
#
# # for i in range(n):
# #     lst[i][i] = 1
#
# print(*lst, sep='\n')

# 1.Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#
#
#  пример  - 8 11 0 -23 140 1 => 11 -23


# lst = [1,2,34,-56,7,8]
# print(*filter(lambda x: 9<abs(x)<100,lst))

# Создать список, который одинаково читается как слева направо, так и справа налево.
# import random

# list1 = [random.randint(1, 10) for _ in range(10)]
# print(list1)
# for i in range(len(list1)):
#     list1.insert(10,list1[i])
# print(list1)

# Заполните список случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.

# Найти количество чисел в списке, которые делятся на 3, но не делятся на 7.
# list1 = [random.randint(1, 100) for _ in range(20)]
# count=0
# for i in list1:
#     if i%3==0 and i%7!=0:
#         count+=1
# print(list1)
# print(count)
# Напишите программу, которая будет запрашивать у пользователя строку из различных значений
# (числа, символы, слова), разделенных запятыми.
# На основе введенных данных создавать из него словарь, в который будут включены только числа.
# Ключами словаря будут являться числа, а значениями - их квадраты.
# list1 = 'asd, 2, we, 3, 5, 5'
# list1 = list1.split(', ')
# print(list1)
# dict_ = dict()
# for i in list1:
#     print(i.isdigit())
#     if i.isdigit():
#         print(i)
#         dict_[i] = int(i)**2

# print(dict_)


# Создайте функцию, которая будет получать на вход два списка, один из ключей,
# другой из значений, и возвращать словарь, созданный из этих списков.

# list_1 = [random.randint(1, 10) for _ in range(5)]
# list_2 = [random.randint(1, 10) for _ in range(5)]
# print(list_1, list_2)


# def d(a, b):
#     list_3 = list(zip(a, b))
#     print(list_3)
#     dicter = {}
#     for i in list_3:
#         dicter[i[0]] = i[1]
#     return dicter
#
# print(d(list_1, list_2))

# Создайте функцию, которая будет получать на вход строку и возвращать словарь,
# содержащий количество вхождений каждой буквы в эту строку.

# def d(a):
#     dicter = {}
#     for i in a:
#         dicter[i] = a.count(i)
#     return dicter
#
# string = 'abcabcf'
# print(d(string))

# Сформировать строку из 10 символов. На четных позициях должны находится четные цифры, на нечетных позициях - буквы.

# import random
# string = ''
# for i in range(10):
#     if i%2==0:
#         string+= str(random.randint(0,10))
#     else:
#         string+= str(random.choice('abc'))
#
# print(string)

#
# Дана строка. Если ее длина больше 10,
# то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12

# string = 'ab'
# print(len(string))
# if len(string) >= 10:
#     print(string[0:6])
# elif len(string) < 10:
#     while len(string) <12:
#         string+='o'
#
# print(len(string), string)


# Дана строка. Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ, не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.
import random

list_1 = '912766123456'

# list1 = list[list_1]
print(list_1)
for i in range(0, len(list_1), 3):
    print(list_1[i+1])
    list(list_1[i]) = 55
    # print(list_1[i + 1])
    # while i+1 == i:
    #     i = '5'
    # print(list_1[i])
    # print(sorted(list_1[i:i + 3]))
print(list_1)
# i = 0
# print(len(list_2))
# for i in range(0, len(list_1), 3):
# while i < range(0,len(list_2)):
#     print(i)
#     print(sorted(list_2[i:3]))
#     i+=1
#     while i[1] == i[0] or i[1] == i[2]:
#         i[1] = f'{random.randint(1,10)}'
# print(list_2)
#
# for i in list_2:
#     print(i)
#     print(sorted(list(i)))
# print(sorted(str(list_1)))
