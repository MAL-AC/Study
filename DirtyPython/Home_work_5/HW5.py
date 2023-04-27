# # Шифратор Цезаря
# text = input('Enter a text for encode: ').upper()
# offset = int(input('Offset letters by: '))
#
# def encoder(text, offset):
#     dict_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     dict_eng = 'ABCD0EFGHIJKLMNOPQRSTUVWXYZ'
#     encode = ''
#     for i in text:
#         if i in dict_rus:
#             encode += dict_rus[(dict_rus.find(i) + offset) % len(dict_rus)]
#         elif i in dict_eng:
#             encode += dict_eng[(dict_eng.find(i) + offset) % len(dict_eng)]
#         else:
#             encode += i
#     return encode
#
# print(encoder(text, offset).capitalize())
#
#
# # Дешифратор Цезаря
# text = input('Enter a text for decode: ').upper()
# offset = int(input('Offset letters by: '))
# def decoder(text, offset):
#     dict_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     dict_eng = 'ABCD0EFGHIJKLMNOPQRSTUVWXYZ'
#     decode = ''
#     for i in text:
#         if i in dict_rus:
#             decode += dict_rus[(dict_rus.find(i) - offset) % len(dict_rus)]
#         elif i in dict_eng:
#             decode += dict_eng[(dict_eng.find(i) - offset) % len(dict_eng)]
#         else:
#             decode += i
#     return decode
#
# print(decoder(text, offset).capitalize())