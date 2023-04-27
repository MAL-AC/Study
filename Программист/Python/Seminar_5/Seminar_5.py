# Найти цисло фибоначи:
# def fibo(n):
#     if n == 0 or n ==1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(5))


# Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# Var 1
# import random
# list1 = [random.randint(1, 5) for _ in range(10)]
# print(list1)
# def change_maxnum(a):
#     max_num= max(a)
#     min_num = min(a)
#     for i in range(len(a)):
#         if a[i] == max_num:
#             a[i] = min_num
#     return a
#
# print(change_maxnum(list1))

# Var2
# import random
# list1 = [random.randint(1, 5) for _ in range(10)]
# print(list1)
# list1 = [min(list1) if i == max(list1) else i for i in list1]
# print(list1)

# Var 3 Best
# import random
# list1 = [random.randint(1, 5) for _ in range(10)]
# print(list1)
# max_ = max(list1)
# min_ = min(list1)
#
# list1 = [min_ if i == max_ else i for i in list1]
# print(list1)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# def prime(a):
#     i = 2
#     while i < -1 and a % i != 0:
#         i+=1
#     return i == a-1
#
# print(prime(6))
#  Var 2
# def prime(num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     elif not num % 2:
#         return False
#     for i in range(3, num // 2 + 1, 2):
#         if num % i == 0:
#             return False
#     return True
#
# print(prime(8))

# Var3
# def simple_numbers(n):
#     for i in range(2, n):
#         if n % i == 0:
#             result = 'Число составное'
#             break
#         else:
#             result = 'Число простое'
#     return (result)
#
# n = int(input('Введите число: '))
# print(simple_numbers(n))

# Дано натуральное числ N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.(Циклы не использовать)

# Var 1 (Not correct)
# def revers_num(n):
#     if n == 0 or n == 1:
#         print(n)
#     for i in range(1, n+1):
#         print(n+1-i, end=' ')
#
# revers_num(9)

# Var 2

# n = 'qwerty'
# print(n)
#
# my_str = " "
#
# def revers_str(a):
#     if len(a) == 1:
#         return a
#     return a[-1] + revers_str(a[:-1])
# print(revers_str(n))

# Var 3
# def revers(text: str):
#     if len(text) == 1:
#         return text
#     return text[-1] + revers(text[:-1])
#
# txt = input('Input str: ')
# print(revers(txt))

# Var 4

# def revers_list(n):
#     if n == 1:
#         return '1'
#     else:
#         return f'{n} -> {revers_list(n-1)}'
#
# num = int(input('Type your N:'))
# print(revers_list(num))

#     return('1' if n ==1 else f'{n}  {revers_list(n-1)}')