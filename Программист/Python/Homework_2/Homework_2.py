# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# import random

# n = int(input('Quantity coins: '))
# res = 0
# ger = 0

# for i in range(n):
#     p = random.randint(0, 1)
#     print(p , end=" ")
#     if p == 0:
#         res+=1
#     else:
#         ger+=1
# if res < ger:
#     print(f'Решки {res}')
# elif ger < res:
#     print(f'Орёл {ger}')
# else:
#     print('Одинаково')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# # Вариант 1: Отгадываем
# import random
# a = random.randint(0,10)
# b = random.randint(0,10)
# # print(a, b)
# print(a+b)
# print(a*b)

# if int(input('number a: ')) == a and int(input('number b: ')) == b or int(input('number a: ')) == b and int(input('number b: ')) == a:
#     print('Winner')
# else:
#     print('Loser')

# Вариант 2: Загадываем

# x = int(input('Sum: '))
# y = int(input('Composition: '))
# for i in range(0,1000):
#     for j in range(0,1000):
#         if x == i + j and y == i * j:
#             print(i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Enter a number'))
# count = 0

# while count<= N:
#     if count%2 == 0:
#         print(count, end=" ")
#     count+=1
