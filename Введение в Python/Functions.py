# # enumerate
# # winners = ['Leo', 'Max', 'Kate']
# # for number, winner in enumerate(winners,1):
# #     print(number, winner)
#
# # def greeting(say,*args):
# #     print(say, args)
# #
# # greeting('Hello', 'Leo')
# # greeting('Hello', 'Leo', 'Max')
# # greeting('Hello', 'Leo', 'Max', 'Kate')
#
# # def get_person(**kwargs):
# #     for k, v in kwargs.items():
# #         print(k, v)
# #
# # get_person(name='Leo', age=20, has_car=True)
#
# # def f():
# #     print('Hello from other f')
# #
# # def to(f_param):
# #     f_param()
# #
# # to(f)
#
# '''
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
# numbers = [i for i in range(1, 9)]
# print(numbers)
#
# def is_even(number):
#     return number % 2 == 0
#
# print(my_filter(numbers, is_even))
#
# def is_not_even(number):
#     return number % 2 != 0
#
# print(my_filter(numbers, is_not_even))
#
# def big_4(number):
#     return number >4
#
# print(my_filter(numbers, big_4))
# '''
# import random
#
# '''
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
# numbers = [i for i in range(1, 9)]
# print(numbers)
#
#
# print(my_filter(numbers, lambda x: x % 2 == 0))
# print(my_filter(numbers, lambda x: x % 2 != 0))
# print(my_filter(numbers, lambda x: x > 4))
# '''
#
# # import random
# # numbers = [random.randint(1,10) for i in range(10)]
# # print(numbers)
# # print(sorted(numbers))
# # print(sorted(numbers, reverse=True))
#
# # names = ['Max', 'Alex', 'Kate']
# # print(sorted(names))
#
# # # Картежи
# # cities = [('Moscow', 1000), ('Las-Vegas', 500), ('Izmir', 2000)]
# # # Сортировка по алфавиту
# # print(sorted(cities))
# #
# # def by_count(city):
# #     return city[1]
# # # Сортировка по числу
# # print(sorted(cities, key=by_count))
# #
# # print(sorted(cities, key=lambda city: city[1]))
#
# '''
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#
# def is_even(number):
#     return number % 2 ==0
#
# result = filter(is_even, numbers)
# print(result)
# result = list(result)
# print(result)
# '''
#
# # names = ['Max', 'Leo', 'Kate']
# # # Получить строку больше 3-х символов
# # print(list(filter(lambda x: len(x)>3, names)))
#
# # import random
# #
# # numbers = [random.randint(1,10) for i in range(10)]
# # print(numbers)
# #
# # print(list(map(lambda x: x**2, numbers)))
# # print(list(map(lambda x: str(x), numbers)))
#
# # 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# # Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
#
# # name = input('Enter your name: ').title()
# # age = input('Enter your age: ')
# # city = input('Enter your city: ').title()
# #
# # def res(name, age, city):
# #     result = (f'«{name} , {age} год(а), проживает в городе {city}»')
# #     return result
# #
# # print(res(name, age, city))
#
#
# # 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# # a = int(input('Enter a number a: '))
# # b = int(input('Enter a number b: '))
# # c = int(input('Enter a number c: '))
# #
# # def max_number(a,b,c):
# #     return max(a,b,c)
# #
# # print(f'Max number is {max_number(a,b,c)}')
#
#
# # import random
#
# player_1 = {'Name': input('Enter first person: '),
#             'health': 100,
#             'damage': random.randint(1, 50),
#             'armor': 1.2
#             }
#
# player_2 = {'Name': input('Enter second person: '),
#             'health': 100,
#             'damage': random.randint(1, 50),
#             'armor': 1.2
#             }
#
#
# def attack(person1, person2):
#     leg = ''
#     while leg == '':
#         damage = random.randint(1, 50)
#         print(f'{player_1["Name"]} beet {player_2["Name"]} damage of {damage}')
#         def attack(damage, armor):
#             return damage/armor
#         player_2['health'] -= attack(damage, player_2['armor'])
#         print(f'{player_2["Name"]} have {round(player_2["health"],2)}')
#         if player_2['health'] <= 0:
#             print(f'{player_1["Name"]} Winner!')
#             break
#         damage = random.randint(1, 50)
#         print(f'{player_2["Name"]} beet {player_1["Name"]} damage of {damage}')
#         player_1['health'] -= attack(damage, player_1['armor'])
#         print(f'{player_1["Name"]} have {round(player_1["health"], 2)}')
#         if player_1['health'] <= 0:
#             print(f'{player_2["Name"]} Winner!')
#             break
#         leg = input('Input on the Enter')
#
#
# attack(player_1, player_2)
#
