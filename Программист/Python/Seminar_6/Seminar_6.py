# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве

import random

list1 = [random.randint(0, 10) for _ in range(5)]

list2 = [random.randint(0, 10) for _ in range(5)]
print(list1, list2)

for i in list1:
    if i not in list2:
        print(i, end=" ")

new_list = (i for i in list1 if i not in list2)
print(new_list)


# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

# import random

# list1 = [random.randint(0, 10) for _ in range(5)]
# print(list1)
# count_ = 0
# for i in range(1, len(list1)-1):
#     if list1[i-1] < list1[i]  > list1[i+1]:
#         count_+=1
# print(count_)
    
# Var 2
# new_list = (i for i in list1 if i not in list_2) 

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, 
# которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# for el in set(list1):
#     counter += list1.count(el) //

# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, 
# каждое из которых не превосходит k.

# k = 10000
# print(my_list := [i for i in range(k)])
# for item in my_list:
#     if item == summarize(summarize(item)) and item != summarize(item):
#         print(item, summarize(item))




# def summarize(number, sum=0):
#     for item in range(1, number//2+1):
#         if number % item == 0:
#             sum += item
#     return sum


# k = 10000
# print(my_list := [i for i in range(k)])
# lst = list()

# i = 0
# while i < len(my_list):
#     item = my_list[i]
#     sum1 = summarize(item)
#     sum2 = summarize(sum1)
#     if (sum2 == item) and (item != sum1):
#         print(item, sum1)
#         lst.append((item, sum1))
#         i = sum1
#     i += 1
# print(lst)

# || def find_sum_delitel(num: int) -> int: 
#     summ = 0 
#     for i in range(1, num // 2 +1): 
#         summ += 1 
#     return summ 
 
# k = int(input('Введите число: ')) 
 
# for num_1 in range(2, k): 
#     num_2 = find_sum_delitel(num_1) 
 
#     if (find_sum_delitel(num_2) == num_1) and (num_1 < num_2): 
#         print (num_1, num_2) ||