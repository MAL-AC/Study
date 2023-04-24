# Задача No31. Общее обсуждение
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

# def f(a):
#     if a == 0 or a == 1:
#         return 1
#     return f(a-1)+f(a-2)

# print(f(7))

# Факториал
# n = int(input('n: '))

# def factor(n):
#     if n <= 1:
#         return 1
#     return n * factor(n-1)

# print(factor(n))


# Задача No35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# def check_num(n, i = 2):
#     if n == i:
#         return True
#     elif n%i ==0:
#         return False
#     elif i*i >n:
#         return True
#     return check_num(n, i+1)

# print(check_num(8))

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

def revers(n):
    if n ==0:
        return ''
    i = input('->')
    return revers(n-1) + i
print(revers(5))