# while True:
#     a = int (input('input a number '))
#     if 0 < a < 11:
#         print(a**2)
#         break
#     else:
#         print('input again')


# fname = input('Your firstname ')
# sname = input('Your secondname ')
# a = int (input('Your age '))
# w = int (input('Your weight '))


# if a <= 30 and w >= 50 and w <= 120:
#     print (f'{fname} {sname} Good') 
# elif a > 30 and a <= 40 and (w < 50 or w > 120):   
#     print ('You need Traing') 
# if a >= 40 and (50 >= w or w >= 120):   
#     print (f'{fname} {sname} You need a Doctor') 

# friend = 'MAKSIM; Leonid'
# print(friend.split(';'))

# top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. petrov 3. cidorov 4. petrov 5. sokolov'
# start = top5.find('1')
# end = top5.find('4')
# top3 = top5[start: end]
# result = (f'Поздравляем {top3.upper()} c успехом!')
# print(result)

# friends = ['Max', 'Leo', 'Kate']
# print(friends)
# print(len(friends))
# friends.append('Ron')
# print(friends)
# print(len(friends))
# del friends[0]
# print(friends)

# print('COMPETITION OF PYTHON')
# count = int(input('How many participants: '))
# i = count
# participants = []
# while i > 0:
#     name = input('Who took {} place: '.format(i))
#     participants.append(name)
#     i-=1
# # Кто участвовал в соревновании по алфавиту
# print('The competition was attended by: ', sorted(participants))
# # Мы записали людей с конца?
# participants.reverse()
# # Нам нужно взять первые 3 места
# result = participants[:3]

# result = 'Winners {}!'.format(result)
# print(result)


# friend_name = 'Max'
# friends = ['Max', 'Leo', 'Kate']
# roles = ('admin', 'guest', 'user')
# # цикл While
# # i = 0
# # while i < len(friends):
# #     friend = friends[i]
# #     print(friend)
# #     i+=1
# # Цикл for
# for friend in friends:
#     print(friend)
    
# for letter in friend_name:
#     print(letter)
    
# for role in roles:
#     print(role)
# print()
# print ('end')


# numbers = range(10)
# print(numbers)
# print(type(numbers))
# print(list(numbers))


# winners = ['Max', 'Leo', 'Kate']
# # Простой способ
# # for winner in winners:
# #     print(winner)
# # Используем range
# for i in range(len(winners)):
#     # print(i+1)
#     print(i+1, '|', winners[i])

# numbers = [1, 2, 5]
# for number in numbers:
#     print(number)

# print(list(range(1, 1000, 2)))

# for number in range(1, 1000, 2):
#     print (number)
    
    
# friends = ['Max', 'Leo', 'Kate']
# print(friends)
# print(type(friends))
# friend = friends[0]
# print(friend)
# friend = {
#     'name': 'Max',
#     'age' : 23 
# }
# print(friend)
# print(type(friend))


# friend = {
#     'name': 'Max',
#     'age': 23,
#     'has_car': True
# }

# # По ключам
# for key in friend.keys():
#     print(key)
#     print(friend[key])
# # Тоже самое
# for key in friend:
#     print(key)
#     print(friend[key])
# # По значению
# for val in friend.values():
#     print(val)
# Пары ключ значение
# for item in friend.items():
#     print(item)
    
# for key, val in friend.items():
#     print(key,':', val)
 
 
#  Множество

# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
# print(type(cities))
# print(cities)

# cities = set(cities)
# print(cities)
# print(type(cities))

# cities = {'Las Vegas', 'Paris', 'Moscow'}
# print(cities)
# cities.add('Buzma')
# print(cities)
# cities.add('Moscow')
# print(cities)
# cities.remove('Moscow')
# print(cities)
# print(len(cities))
# print('Paris' in cities)

# for city in cities:
#     print(city)


# # Один взял эти вещи
# max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# # Другой эти
# kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
# # Какие вещи взяли
# print(max_things | kate_things)
# # Какие повторяются
# print(max_things & kate_things)
# # Какие взял Мах и не взяла Kate
# print(max_things - kate_things)
# # Какие взяла Kate и не взял Max
# print(kate_things - max_things)


# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие 
# во втором списке.
#     Примечание. Списки создайте вручную, например так:
# a = [2, 5, 5, 5, 8, 2, 12, 12, 4]
# b = [2, 7, 12, 3]
#
# for number in a[:]:
#     if number in b:
#         a.remove(number)
# print(a)

# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)
# date ='02.11.2013'
# d, m, y = date.split('.')
# print(d, m, y)
# month = {
#     '11': 'ноября'
# }
# days = {
#     '02': 'второе'
# }
# result = f'{days[d]} {month[m]} {y} года'
# print (result)

# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:

# numbers = [2, 2, 5, 12, 8, 2, 12]
# result = []
# for number in numbers:
#     if numbers.count(number) == 1:
#         result.append(number)
# print(result)

# Угадай число
# Вариант 1 (простой)
# import random
# number = random.randint(1, 100)
#
# while True:
#     user_number = int(input('Введите число: '))
#     if number == user_number:
#         print('Победа')
#         break
#     elif number < user_number:
#         print('Число больше загаданного')
#     else:
#         print('Число меньше загаданного')

# Вариант 2
# import random
# number = random.randint(1, 100)
# user_number = None
# while number != user_number:
#     user_number = int(input('Введите число: '))
#     if number < user_number:
#         print('Число больше загаданного')
#     elif number > user_number:
#         print('Число меньше загаданного')
# print('Победа')

# Вариант 3
# import random
# number = random.randint(1, 10)
# user_number = None
# count = 0
# max_count = 3
# while number != user_number:
#     count +=1
#     if count > max_count:
#         print('Game END!')
#         break
#     print(f'Попытка № {count}')
#     user_number = int(input('Введите число: '))
#     if number < user_number:
#         print('Число больше загаданного')
#     elif number > user_number:
#         print('Число меньше загаданного')
# else:
#     print('Победа')

# Вариант 4 (Уровни сложности)
# import random
# number = random.randint(1, 100)
# user_number = None
# count = 0
# levels = {1: 10, 2: 5, 3: 3}
# level = int(input('Введите уровень сложности из трех: '))
# max_count = levels[level]
# while number != user_number:
#     count +=1
#     if count > max_count:
#         print('Game END!')
#         break
#     print(f'Попытка № {count}')
#     user_number = int(input('Введите число: '))
#     if number < user_number:
#         print('Число больше загаданного')
#     elif number > user_number:
#         print('Число меньше загаданного')
# else:
#     print('Победа')

# Вариант 5 (Несколько игроков)

# import random
# number = random.randint(1, 100)
# user_number = None
# count = 0
# levels = {1: 10, 2: 5, 3: 3}
# level = int(input('Введите уровень сложности из трех: '))
# max_count = levels[level]
# user_count = int(input('Введите количество пользователей: '))
# users = []
# for i in range(user_count):
#     user_name = input(f'Введите имя пользователя {i+1}: ')
#     users.append(user_name)
# print(users)
# is_winner = False
# winner_name =None
# while not is_winner:
#     count +=1
#     if count > max_count:
#         print('Game OVER!')
#         break
#     print(f'Попытка № {count}')
#     for user in users:
#         print(f'Ход игрока {user} ')
#         user_number = int(input('Введите число: '))
#         if user_number == number:
#             is_winner = True
#             winner_name = user
#             break
#         elif number < user_number:
#             print('Ваше число больше загаданного')
#         else:
#             print('Ваше число меньше загаданного')
# else:
#     print(F'Победитель: {winner_name}')

