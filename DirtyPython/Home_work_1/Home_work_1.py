# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)

# n = input('Введите число: ')

# p = n.find('.')

# if p > 0:
#     n =float(n) * 10 **p
    
# n = int(n)

# if n < 0:
#     n*=(-1)
    
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10

# print('Сумма цифр числа:', sum)


# 2. На вход поступает вещественное число, найти первую цифру дробной части.

# n = input('Введите число: ')

# p = n.find('.')
# print(n[p+1])

# 3. На вход поступает десятичное число, вывести его в виде двоичного

# x = int(input('Введите число: '))
# n = ""
# while x > 0:
#     y = str(x % 2)
#     n = y + n
#     x = int(x / 2)
# print (n)

