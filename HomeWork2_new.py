
# задание 1

# li = [2, 5, 'day', True, ['a, b, c'], 47.259, {'a': 1, 'b': 2, 'c': 3}, ('a, b, c', 245), None]
# for el in li:
#     print(type(el))

# задание 2. Пыталась решить через "range", и не поняла, как это работает.
# Объясните, пожалуйста, или подскажите, где почитать.

# li = []
# elem = input('Введите элемент списка. Для окончания списка введите stop. ')
# while elem != 'stop':
#     li.append(elem)
#     elem = input('Введите элемент списка. Для окончания списка введите stop. ')
# i = 0
# for el in li:
#     while i < int(len(li) - 1):
#         li[i], li[i + 1] = li[i + 1], li[i]
#         i += 2
# print(li)

# задание 3
# решение через list

# li = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
# num = int(input('Введите номер месяца: '))
# for el in li:
#     if num in el:
#         print(el[0])


# задание 3
# решение через dir

# di = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
# num = int(input('Введите номер месяца: '))
# for key, val in di.items():
#     if num in val:
#         print(key)

# задание 4

# st = input('Введите строку, разделяя слова пробелами: ')
# for i, v in enumerate(st.split(' '), 1):
#     if len(v) < 10:
#         print(i, v)
#     else:
#         print(i, v[:10])

# задание 5

# li = [3, 2, 1]
# a = int(input('Введите новый элемент рейтинга: '))
# while a != 100:
#     li.append(a)
#     li.sort()
#     li.reverse()
#     print(li)
#     a = int(input('Введите новый элемент рейтинга. Чтобы закончить, введите 100: '))
# print('end')

# задание 6

# goods_num = int(input('Введите кол-во товаров: '))
# goods_list = []
# names = []
# prices = []
# ql = []
# unit = []
# n = 1
# while goods_num >= n:
#     goods_dict = {'Название': input('Название '), 'цена': input('цена '), 'кол-во': input('кол-во '), 'ед': input('ед ')}
#     names.append(goods_dict.get('Название'))
#     prices.append(goods_dict.get('цена'))
#     ql.append(goods_dict.get('кол-во'))
#     unit.append(goods_dict.get('ед'))
#     goods_tuple = (n, goods_dict)
#     goods_list.append(goods_tuple)
#     n += 1
#
# print(goods_list)
# analytics = {'название': names, 'цена': prices, 'кол-во': ql, 'ед': unit}
# print(f'Аналитика: {analytics}')
