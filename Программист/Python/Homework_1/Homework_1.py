# Задача 2: Найдите сумму цифр трехзначного числа.

# n = int(input('Введите трехзначное число: '))

# if 99<n<1000:
#     a = int(n/100)
#     b = int(n/10%10)
#     c = int(n%10)
#     print(a+b+c)
# else:
#     print('Число не трехзначное!')



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


# n = int(input('Сколько журавлей '))

# k = int(-1*n//1.5*-1)
# p = int((n//6))
# s = p

# if p+k+s == n:
#     print(f'Петя сделал: {p}, Катя сделала: {k}, Сережа сделал: {s}')
# else:
#     k = int(n//1.5)
#     p = int(-1*n//6*-1)
#     s = p
#     if p+k+s == n:
#         print(f'Петя сделал: {p}, Катя сделала: {k}, Сережа сделал: {s}')
#     else:
#         k = int(n//1.5+1)
#         p = int(n//6)
#         s = p
#         if p+k+s == n:
#             print(f'Петя сделал: {p}, Катя сделала: {k}, Сережа сделал: {s}')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# n = int(input('Введите 6 значное число: '))
# a = n//100000
# b = n//10000%10
# c = n//1000%10
# d = n%1000//100
# e = n%100//10
# f = n%10 

# if a+b+c == d+e+f:
#     print('Yes')
# else:
#     print('No')
 

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите размер n: '))
# m = int(input('Введите размер m: '))
# k = int(input('Сколько долек ломаем: '))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')

# Вариант 2
# if int(num[0])+int(num[1])+int(num[2]) == int(num[3])+int(num[4])+int(num[5]):
#     print("yes")
# else:
#     print("no")