# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте:
# вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна

import random
from math import pi


# def find_farthest_orbit(list_of_orbits: list) -> dict:
#     dict_ = {round(pi * orbit[0] / 2 * orbit[1] / 2, 2): orbit for orbit in
#              filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}
#
#     return dict_
#
#
# num = int(input("Введите список планет:"))
# orbits = [(random.randint(1, 10), random.randint(1, 10)) for i in range(num)]
# print(orbits)
# dict_p = find_farthest_orbit(orbits)
# print(max(dict_p), dict_p[max(dict_p)])


# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))
    return len(my_set) < 2

my_list = [random.randint(2,10) for i in range (5)]

print(same_by(lambda x: x%2, my_list), my_list)