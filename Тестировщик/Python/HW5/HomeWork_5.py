# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# a = (int(input('Enter a namber A: ')))
# b = (int(input('Enter a namber B: ')))
#
# def power_num(a, b):
#     if b == 0:
#         return 1
#     return (a * power_num(a, b - 1))
#
#
# print(f'{a} to the power of {b} = {power_num(a, b)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# a = (int(input('Enter a namber A: ')))
# b = (int(input('Enter a namber B: ')))
#
# def sum_nums(a,b):
#     if b == 0:
#         return a
#     return(sum_nums(a+1, b-1))
#
# print((f'Sum of numder {a} and {b} = {sum_nums(a,b)}'))
