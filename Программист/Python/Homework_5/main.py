# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
a = (int(input('Enter a namber A: ')))
b = (int(input('Enter a namber B: ')))

def raise(a**b):
    if a <= 1:
        return 1
    return a + raise(a**b)




# def factor(n):
#     if n <= 1:
#         return 1
#     return n * factor(n-1)