# 1. ПАЛИНДРОМЫ
# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов  
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
# level deified noon Racecar radar repaper

# Var 1
# word = input('Input a word: ')
# print(len(word))
# word = word.upper()
# i = 0
# j = -1
# t = 0
# while i < len(word)/2:
#     if word[i] == word[j]:
#         i+=1
#         j-=1
#         t+=1
#     else:
#         break
# print(t)
# print(len(word)/2)
# if t >= len(word)/2:
#     print('Yes')
# else:
#     print ('NO')

# Var 2
# word = input('Input a word: ')
# for i in range(len(word)//2):
#     if not word[i].lower() ==  word[-i-1].lower():
#         print('Это не палиндром')
#         break
# else:
#     print(f'{word} - палиндром')

# Var 3
# word = input('Input a word: ')
# print(word.lower() == word[::-1].lower())

# 1. ПАЛИНДРОМЫ
# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.

# Var 1
# import string
# text = input('Input a text: ')
# print(string.punctuation)
# for letter in string.punctuation:
#     text = text.replace(letter, '')
# text = text.replace(' ', '').lower()
# print(text.lower() == text[::-1].lower())

# Var 2
# text = "".join([symbol.lower() for symbol in input("Введите строку: ") if symbol.isalpha()])
# print(text == text[::-1])

# Напишите программу, которая будет выводить в консоль таблицу умножения от 1 до 10
# (как в вконце старых тетрадок, квадратная такая)
#
# Var 1
# for x in range(1,11):
#     for y in range(1,11):
#         print (f'{x*y:<5}', end='')
#     print()

# Var 2
# for i in range(1,11):
#     print('\t'.join([str(i*j) for j in range(1, 11)]))

# 3. ИСТИННОСТЬ ПРЕДИКАТ
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат
# (предикат - переменная, которая может иметь только два значения True или False)
# Напишите программу, которая докажет это.

# Var 1
# x = input('Input a namber x: ')
# y = input('Input a namber y: ')
# z = input('Input a namber z: ')
#
# if not(x or y or z) == (not x and not y and not z):
#     print(True)
# else: print(False)

# Var 2
# for x in[True, False]:
#     for y in [0,1]:
#         for z in ['1', None]:
#             if not(x and y and z) == (not(x) or not(y) or not(z)):
#                print("Yes")


# 4. СПОРТСМЕНЫ
# На вход подается возраст и вес спортсмена. Вывести группу по возрасту и весовую категорию,
# в которой он будет принимать участие согласно следующим правилам.
# Соревнования юношей младшей возрастной группы (14—15 лет) проводятся без деления участников на весовые категории.
# Соревнования для юношей старшего возраста (16—17 лет) проводятся в весовых категориях:
# легчайшая - до 52 кг
# легкая - до 57
# средняя - до 70
# тяжёлая - до 80
# вторая тяжелая свыше 80
# Соревнования для юниоров (18—19 лет) и взрослых (20 лет и старше)
# легчайшая - до 54 кг
# легкая - до 60
# средняя - до 75
# тяжелая свыше 81
# Лица младше 14 или весом ниже 44 кг до соревнований не допускаются

# a = int(input("Input age: "))
# w = int(input("input a weight: "))
#
# if a < 14 or w < 44:
#     print('Не допущен')
# elif a <= 15:
#     print('<ез деления участников на весовые категории')
# elif a <= 17:
#     if w <= 52:
#         print("Легчайшая")
#     elif  w <= 57:
#         print("Легкая")
#     elif w <= 70:
#         print('Cредняя')
#     elif w <= 80:
#         print("Тяжелая")
#     else:
#         print("вторая тяжелая")
# else:
#     if w <= 54:
#         print('Легчайшая')
#     elif w <= 60:
#         print('Легкая')
#     elif w <= 75:
#         print('Средняя')
#     elif w <= 81:
#         print('Тяжелая')
#     else:
#         print('Вторая тяжелая')


# 5. FIZZ BUZZ
# Напишите программу, которая выводит на экран числа от 1 до n.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# 7а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

# Var 1
# n = int(input('Input a number n: '))
#
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         i = "FizzBuzz"
#     elif i % 3 == 0:
#         i = "Fizz"
#     elif i % 5 == 0:
#         i = "Buzz"
#     print(i, end=" ")

# Var 2
# n = int(input('Input a number n: '))
# for i in range(1, n+1):
#     if not i%3 and not i%5:
#         i = "FizzBuzz"
#     elif not i%3:
#         i = "Fizz"
#     elif not i%5:
#         i = "Buzz"
#     print(i, end=" ")


# 6. ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР
# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций
# (сложение, вычитание, умножение или деление):
# вводим первое число,
# потом операцию
# и второе число
# выводится результат
#
# Программа должна завершаться только по желанию пользователя: можно ввести enter и программа закончится,
# или еще операцию и еще число. Ну и помним, что на ноль делить нельзя.

# Var 1
# x = float(input('Input a namber x: '))
# y = float(input('Input a namber y: '))
#
# while 1:
#     n = input('что делаем?(Enter: Выход)')
#     if n == "+":
#         print( x + y)
#     if n == "-":
#         print(x - y)
#     if n == "*":
#         print(x * y)
#     if n == "/":
#         if y != 0:
#             print(x / y)
#         else:
#             print("На 0 делить нельзя")
#     if n =="":
#         break

# Var 2

result = int(input("Введите первое число: "))
while True:
    while True:
        oper = input('Введите операцию: ')
        if oper == '':
            exit()
        if oper in '+-*/':
            break
    second = int(input('Введите второе число: '))
    if second =='':
        break
    match oper:
        case '+':
            result+= second
        case '-':
            result-= second
        case '*':
            result*= second
        case '/':
            if second:
                result/= second
            else:
                print("На 0 делить нельзя")

    print(result)
    if not isinstance(result, int | float):
        break
