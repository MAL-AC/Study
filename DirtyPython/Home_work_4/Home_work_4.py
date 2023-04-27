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
import string

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

text = input('Input a text: ')
def count_letters(text: str) -> tuple:
    for c in string.punctuation +' ':
        text = text.replace(c, '')

    dict_count ={}
    for c in text:
        dict_count[c] = dict_count.get(c, 0) + 1
    max_c = max(dict_count.keys(), key=lambda x: dict_count.get(x))
    return max_c, str(round(dict_count.get(max_c)/len(text)*100, 2)) + '%'

print(count_letters(text), sep=', ')

