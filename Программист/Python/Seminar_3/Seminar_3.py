# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Var 1
# a = {1, 2, 3, 2, 1, 3, 4}
# print(len(a))

# Var 2
# n = list(input('Enter numbers'))
# uniq_list = []
# for item in n:
#     if not item in uniq_list:
#         uniq_list.append(item)
# print(n)
# print(uniq_list)
# print(len(uniq_list))

# Var 3
# n = list(input('Enter numbers'))
# print(n)
# print(len(set(n)))

# Var 4
# print(set_num := input('Enter nambers: '), len(set(set_num)))

# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.



# Дан список, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов списка, больших предыдущего 
# (элемента с предыдущим номером)

# list1 = list(input('Enter numbers'))
# print(list1)
# count = 0
# max_ = int(list1[0])
# for i in range(max_):
#     if i < i+1:
#         count+= 1
# print(count)

# Напишите программу для печати всех уникальных значений в словаре.

my_list = [{"V": "S001"}, {"V": "S002"},
           {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {" V ": "S009"},
           {" VIII ": "S007"}]

uniq = set()

for item in my_list:
    for value in item.values():
        uniq.add(value)
print(uniq)