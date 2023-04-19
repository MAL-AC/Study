# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# text = list(input('Введите строку: '))
# count_dict = {}
#
# for letter in text:
#     count_dict[letter] = count_dict.get(letter, 0) + 1
#     if count_dict.get(letter) == 1:
#         print(f'{letter}', end=' ')
#     else:
#         print(f'{letter}_{count_dict.get(letter) - 1}', end=' ')


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