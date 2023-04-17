# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)
# Var1
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


# Var2 "THE BEST"
# num = input('Введите число: ')
# sum_ = 0
# for item in num:
#     if item.isdigit():
#         sum_ += int(item)
# print(sum_)

# Var3
# num = input('Введите число: ')
# num = num.replace('.', '').replace('-', '')
# sum_= 0
# for item in num:
#     sum_ += int(item)
# print(sum_)
    

# 2. На вход поступает вещественное число, найти первую цифру дробной части.

# Var 1
# n = input('Введите число: ')
# p = n.find('.')
# print(n[p+1])

# Var 2
# num = float(input('Введите число: '))
# print(int(num * 10 % 10))

# Var 3
# num = input('Введите число: ')
# num = num.split('.')[1][0]
# print(num)

# 3. На вход поступает десятичное число, вывести его в виде двоичного

# Var 1
# x = int(input('Введите число: '))
# n = ""
# while x > 0:
#     y = str(x % 2)
#     n = y + n
#     x = int(x / 2)
# print (n)

# Var 2

# num = 16
# bi_num = ''
# while num:
#     bi_num = str(num % 2) + bi_num
#     num //=2
# print(bi_num)