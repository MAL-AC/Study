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


# print(int('Enter a number: '))

min_ = 1
max_ = 100

answer = (max_ + min_) // 2
attemps = 3
while answer != '=':
    print(f'Steel attemp # {(attemps)}')
    print(answer)
    attemps -= 1
    if attemps == 0:
        print('PC LOSER!')
        break
    num = input('Your number is =, < or > ?:  ')
    if num == '=':
        print('PC Winner!!!')
        answer = num
    if num == '<':
        max_ = answer - 1
        answer = (min_ + answer) // 2
    if num == '>':
        min_ = answer + 1
        answer = (answer + max_) // 2

