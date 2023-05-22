# # VAR 1 (my)
#
# # # Шифратор Цезаря
# # text = input('Enter a text for encode: ').upper()
# # offset = int(input('Offset letters by: '))
#
# # def encoder(text, offset):
# #     dict_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# #     dict_eng = 'ABCD0EFGHIJKLMNOPQRSTUVWXYZ'
# #     encode = ''
# #     for i in text:
# #         if i in dict_rus:
# #             encode += dict_rus[(dict_rus.find(i) + offset) % len(dict_rus)]
# #         elif i in dict_eng:
# #             encode += dict_eng[(dict_eng.find(i) + offset) % len(dict_eng)]
# #         else:
# #             encode += i
# #     return encode
# #
# # print(encoder(text, offset).capitalize())
# # #
# #
# # # Дешифратор Цезаря
# # text = input('Enter a text for decode: ').upper()
# # offset = int(input('Offset letters by: '))
# # def decoder(text, offset):
# #     dict_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# #     dict_eng = 'ABCD0EFGHIJKLMNOPQRSTUVWXYZ'
# #     decode = ''
# #     for i in text:
# #         if i in dict_rus:
# #             decode += dict_rus[(dict_rus.find(i) - offset) % len(dict_rus)]
# #         elif i in dict_eng:
# #             decode += dict_eng[(dict_eng.find(i) - offset) % len(dict_eng)]
# #         else:
# #             decode += i
# #     return decode
# #
# # print(decoder(text, offset).capitalize())
#
# # VAR 2
#
# import string
#
# en_letters_low = string.ascii_lowercase
# en_letters_up = string.ascii_uppercase
# ru_letters_low = ''.join([chr(x) for x in range(ord('а'), ord('я') + 1)])
# ru_letters_up = ''.join([chr(x) for x in range(ord('А'), ord('Я') + 1)])
# ru_letters_low = ru_letters_low[:6] + 'ё' + ru_letters_low[6:]
# ru_letters_up = ru_letters_up[:6] + 'Ё' + ru_letters_up[6:]
# all_alphabet = [en_letters_low, en_letters_up, ru_letters_low, ru_letters_up]
#
#
# def cript(letter: str, alphabet: str, shift: int, decrypt: bool = True) -> str:
#     return alphabet[(alphabet.find(letter) + (shift if decrypt else -shift)) % len(alphabet)]
#
#
# def cipher_cesser(word: str, all_letters: list[str], shift: int, decode: bool) -> str:
#     crypt_word = ''
#     for letter in word:
#         for alpha in all_letters:
#             if letter in alpha:
#                 crypt_word += cript(letter, alpha, shift, decode)
#                 break
#
#         else:
#              crypt_word += letter
#     return crypt_word
#
#
# word = input('Input a word: ')
# shift = int(input('Input a shift: '))
#
# print(word)
# print(cip_word := cipher_cesser(word, all_alphabet, shift, True))
# print(cipher_cesser(cip_word, all_alphabet, shift, False))
