# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# fact = 1
# n = int(input ("Введите число N: "))
# while n>0:
#     fact = fact*n
#     n=n-1
# print (fact)

# Задача No11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6
# Вариант 1
# A = int(input("Ведите искомый номер числа фибоначчи "))     

# if A == 0:
#     print("0")

# elif A == 1:
#     print("1\nили")

# if (A < 0):
#     print("-1")
# else:
#     fib1 = 0
#     fib2 = 1
#     fib3 = 1
#     FibIndx = 2

#     while (fib2 < A):
#         fib3 = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib3
#         FibIndx += 1

#     result = FibIndx

# if fib2 == A:

#     print(result)

# else:
#     print("-1")

# Вариант 2

# n = int(input("Введите число Фибоначчи: "))
# print((round((5*n*n+4)**0.5, 0)) == (5*n*n+4)**0.5 or (round((5*n*n-4)**0.5, 0)) == (5*n*n-4)**0.5)

# y = 1
# z = 2
# count = 4

# # while (((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/(5**0.5) < n

# while z!=n:
#     temp = z
#     z = z+y
#     y = temp
#     count+=1

# print(count)

# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 Output: 2

# days = int(input("Количество дней: "))
# count = 0
# tempMax = 0
# for i in range(0, days):
#     temperature = int(input("Введите температуру дня: "))
#     if (temperature > 0):
#         count += 1
#         if (tempMax < count):
#             tempMax = count
#     elif (temperature <= 0):
#         count = 0

# print(tempMax)

# Задача No15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9

# melons = int(input("Количество арбузов: "))
# num_melon = int(input(f"Масса 1-го арбуза: "))
# min = num_melon
# max = num_melon
# for i in range(1, melons):
#     num_melon = int(input(f"Масса {i + 1}-го арбуза: "))
#     if (min > num_melon):
#         min = num_melon
#     if (max < num_melon):
#         max = num_melon
# print(f"Масса лёгкого арбуза = {min}")
# print(f"Масса тяжёлого арбуза = {max}")