# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут 
# длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

n = int(input('км за день '))
m = int(input('км нужно '))

s = (m + n - 1) // n
print(s)




# В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# a = int(input('класс а '))
# b = int(input('класс b '))
# c = int(input('класс c '))

# c = int(input())
# a1 = (a + 1) // 2
# b1 = (b + 1) // 2
# c1 = (c + 1) // 2
# s = a1 + b1 + c1
# print(s)

# a = int(input('Введите количество учеников в первом классе: '))
# b = int(input('Введите количество учеников во втором классе: '))
# c = int(input('Введите количество учеников в третьем классе: '))

# result = a//2 + b//2 + c//2 + a%2 + b%2 + c%2

# print(f'{result}')

# Задача No5. Решение в группах
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016 Output: YES

# Напишите программу, которая принимает на вход координаты точки х и Y). # причем х * О и Y о и выдает номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).