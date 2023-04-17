# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# import random
# size = int(input('Input quantity of numbers: '))
# min_num = int(input('Input a min number: '))
# max_num = int(input('Input a max number: '))

# list_1 = [(random.randint(min_num, max_num)) for i in range(size)]

# print(list_1)

# x = int(input('Input a number to search for: '))
# count = 0

# for i in range(len(list_1)):
#     if list_1[i] == x:
#         count+= 1

# print(f'The number {x} occurs {count} times')


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# import random
# size = int(input('Input quantity of numbers: '))
# min_num = int(input('Input a min number: '))
# max_num = int(input('Input a max number: '))

# list_1 = [(random.randint(min_num, max_num)) for i in range(size)]

# print(list_1)

# x = int(input('Input a number to search for: '))
# min_ = list_1[0]

# for i in range(len(list_1)):
#     if (abs(list_1[i] - x) < abs(min_ - x)) and list_1[i] != x :
#         min_ = list_1[i]

# print(f'the nearest number {x} is {min_}')


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
#

# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}
#
# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in list_letters.items():
#         if i in v:
#             summ += k
# print(f"Цена слова: {summ}")