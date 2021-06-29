# задание 1

# with open('my_file.txt', 'w') as f:
#     a = input('Введите данные: ')
#     while a != '':
#         f.writelines([a, '\n'])
#         a = input('Введите данные: ')


# задание 2

# with open('my_text.txt', 'r', encoding='utf-8') as file:
#     i = 1 # счетчик строк
#     for line in file:
#         a = len(line.split())
#         print(f'Количество слов в {i}-й строке {a}')
#         i += 1
#     print(f'Количество строк {i - 1}')


# задание 3

# with open('salary_file.txt', 'r', encoding='utf-8') as file:
#     li_com = []
#     i = 0
#     print('Сотрудники с зарплатой менее 20.000:')
#     for line in file:
#         li = line.split()
#         if float(li[1]) < 20000:
#             print(li[0])
#         li_com.append(float(li[1]))
#         i += 1
#     print(f'Средняя зарплата сотрудников {round((sum(li_com) / i), 2)}')


# задание 4

# di = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# with open('number.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         li = line.split()
#         for el in li:
#             if el in di.keys():
#                 i = li.index(el)
#                 a = di.setdefault(el)
#                 li.remove(el)
#                 li.insert(i, a)
#                 my_str = ''
#                 for num in range(0, len(li)):
#                     my_str = my_str + str(li[num] + ' ')
#                 with open('num_rus.txt', 'a', encoding='utf-8') as new_file:
#                     new_file.write(my_str + '\n')


# задание 5

# from random import randint
#
# li_num = []
# li_str = []
# for el in range(0, 10):
#     num = randint(0, 100)
#     li_num.append(num)
#     my_str = str(num)
#     with open('sum_num.txt', 'a') as file:
#         file.write(my_str + ' ')
# print(f'Сумма чисел в файле: {sum(li_num)}')


# задание 6

# with open('subjects.txt', 'r', encoding='utf-8') as f:
#     di = {}
#     for line in f:
#         li = line.split(':') # делит строку на 2 элемента, где первый - ключ словаря, второй - всё остальное
#         li_val = list(li[1]) # из второго элемента делает список для значений словаря
#         li_1 = [] # список элементов цифра + пробел
#         for el in li_val:
#             try:
#                 int(el)
#                 li_1.append(el)
#             except ValueError:
#                 li_1.append(' ')
#         my_str = ''.join(li_1).split(' ')
#         li_2 = [] # список элементов-чисел
#         for elem in my_str:
#             try:
#                 li_2.append(int(elem))
#             except ValueError:
#                 continue
#         new_di = {li[0]: sum(li_2)}
#         di.update(new_di)
#     print(di)


# задание 7

# with open('company.txt', 'r', encoding='utf-8') as f:
#     li_common = [] # общий итоговый список
#     di_profit = {}
#     i = 0  # счетчик количества прибыльных фирм
#     li_profit = []  # список прибыли
#     for line in f:
#         li = line.split()
#         new_di_profit = {li[0]: (int(li[2]) - int(li[3]))}
#         di_profit.update(new_di_profit)
#         if int(li[2]) > int(li[3]):
#             li_profit.append(int(li[2]) - int(li[3]))
#             i += 1
#     li_common.append(di_profit)
#     li_common.append({'average_profit': sum(li_profit) / i})
#
#
# import json
#
# with open('my_file.json', 'w') as write_f:
#     json.dump(li_common, write_f)
