# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# Var 1
# text = input('Введите предложение').split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))

# Var 2
# str1 = print('Введите текст')
# a = str.upper().split()
# print(len(set(a)))



# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Var 1
# text = list(input('Введите строку: '))
# count_dict = {}

# for letter in text:
#     count_dict[letter] = count_dict.get(letter, 0) + 1
#     if count_dict.get(letter) == 1:
#         print(f'{letter}', end=' ')
#     else:
#         print(f'{letter}_{count_dict.get(letter) - 1}', end=' ')
        
# Var 2
# string = "a a a b c a a d c d d".split()

# for i in range(len(string)):
#     print(f"{string[i]}_{string[0:i].count(string[i])}" if string[0:i].count(string[i]) != 0 else string[i], end=" ")

# Var 3

# stroka = input("Введите строку: ").split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран:
# +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п.,
# а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами.
# Полученный словарь вывести командой:

# print(*sorted(d.items()))

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

# a = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"

# a = a.split()

# b = []


# for i in a:
#     b.append(i[0:2])
# c = dict().fromkeys(b, [])

# for i in a:
#     c[i[0:2]].append(i)



# print(c)