# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# my_limit = int(input('Enter max number of factorial: '))
# fact = 1
# count = 1

# while count<= my_limit:
#     fact+= count
#     count+=1
    
# print(fact)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# n1 = 0
# n2 = 1
# i = 1

# num = int(input('Enter a namber: '))
# while n2 < num:
#     i += 1
#     n, n2 = n2, n1 + n2
# if n2 == num:
#     print(i)
# else:
#     print(-1)


# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.

# import random

# days = int(input("ведите количество рассматриваемых дней 1 ≤ N ≤ 100: "))

# max_thaw_durations_days = 0
# current_thaw_durations_days = 0

# for i in range(1, days+1):
#     # averageDailyTemperature = int(input(f"Введите среднесуточную температуру в день номер {i}: "))

#     average_daily_temperature = random.randint(-3, 3)

#     print(average_daily_temperature, end=" ")

#     if average_daily_temperature > 0:
#         current_thaw_durations_days += 1
#     else:
#         current_thaw_durations_days = 0

#     if current_thaw_durations_days > max_thaw_durations_days:
#         max_thaw_durations_days = current_thaw_durations_days

# print(f"\nДлительность максимальной оттепели за данный период составляет {max_thaw_durations_days} дней")


# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий 
# и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные 
# и не превышают 30000.

# import random

# MAX_WEIGHT = 5000
# MIN_WEIGHT = 100

# watermelon = int(input("Введите количество арбузов: "))
# weigth = 0
# max_weigth = MIN_WEIGHT
# min_weigth = MAX_WEIGHT

# for i in range(watermelon):
#     weigth = random.randint(MIN_WEIGHT, MAX_WEIGHT)
#     print(weigth, end=" ")
#     if weigth > max_weigth:
#         max_weigth = weigth
#     if weigth < min_weigth:
#         min_weigth = weigth
# print(f"\nАрбуз для себя получился на {max_weigth} г, а для тёщи {min_weigth} г. Как-то так")

# Задача *
# Валентина прогуляла лекцию по математике.Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения 
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью. Помогите ей
# Постарайтесь найти самое оптимальное решение.