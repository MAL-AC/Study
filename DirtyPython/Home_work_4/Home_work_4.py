# 1. Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
#   - строку только из букв
#   - строку только из цифр
#   - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее
# #
# def sravnit(a,b):
#     print(len(a))
#     print(len(b))
#     if len(a) > len(b):
#         print('num more')
#     elif len(a) < len(b):
#         print('alfa more')
#     else:
#         print('num = alfa')
#
# num = [1,2,3]
# alfa = ['a','b','c','d']
# sravnit(num,alfa)

# 2. Написать функцию, которая будет возвращать список созданный по заданным критериям:
# размер, минимальное и максимальное значение, наличие повторяющихся элементов
#
# import random
# def list(a,b,c,):
#     list1 = [random.randint(b, c) for _ in range(a)]
#     repeat = [i for i in list1 if list1.count(i) != 1]
#     return list1, repeat
#
# print(list(10,1,10))

# 3. функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - *принимает число и выдает его только простые делители

# def check_num(a):
#     if a % 2 == 0:
#         print('Even')
#     else:
#         print('Not even')
#
#     for i in range(2, a//2+1):
#         print(i)
#         if a % i == 0:
#             print('Complex')
#             break
#         else:
#             print('Prime')
#     if a == 2 or a == 3:
#         print('Prime')
#
#
# check_num(3)


# 4. Функция принимает предложение, вычислzет какой буквы в этом предложении больше и возdращает эту букву и процент ее вхождения предложение