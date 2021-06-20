
# задание 1

# def div(a, b):
#     try:
#         a / b
#     except ZeroDivisionError:
#         d = 'Деление на ноль. На ноль делить нельзя!'
#     else:
#         d = a / b
#     return d


# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# num_3 = div(num_1, num_2)
# print(f'Результат деления первого введенного Вами числа на второе: {num_3}')

# задание 2

# def my_f(name, surname, year_of_birth, town, email, tel):
#     st_my_f = name + ' ' + surname + ' ' + year_of_birth + ' ' + town + ' ' + email + ' ' + tel
#     return st_my_f
#
#
# v1 = input('Введите имя: ')
# v2 = input('Введите фамилию: ')
# v3 = input('Введите год рождения: ')
# v4 = input('Введите город: ')
# v5 = input('Введите адрес электронной почты: ')
# v6 = input('Введите телефон: ')
# my_str = my_f(name=v1, surname=v2, year_of_birth=v3, town=v4, email=v5, tel=v6)
# print(my_str)

# задание 3

# def my_funk(a, b, c):
#     li = [a, b, c]
#     li.remove(min(li))
#     s = li[0] + li[1]
#     return s
#
#
# print(my_funk(3, 4, 5))

# задание 4
# решение через **

# def my_funk(x, y):
#     res = x ** y  # работает и с отрицательными, и с положительными числами у
#     return res
#
#
# print(my_funk(2, -1))

# задание 4
# решение через цикл

# def my_funk(x, y):
#     i = 0
#     for el in range(abs(y) - 1):
#         x *= x
#         i += 1
#     res = 1 / x
#     return res
#
#
# print(my_funk(2.5, -1))


# задание 5

# li_1 = []
# st = input('Введите числа, разделяя их пробелом: ')
# while 's' not in st:
#     li = (st.split(' '))
#     for el in li:
#         el = int(el)
#         li_1.append(el)
#     print(f'Сумма чисел {sum(li_1)}')
#     st = input('Введите ещё числа. Для завершения введите stop: ')
# li = (st.split(' '))
# for el in li:
#     try:
#         el = int(el)
#     except ValueError:
#         continue
#     else:
#         li_1.append(el)
# print(f'Сумма чисел {sum(li_1)}. Программа завершена.')


# задание 6, 7 - не поняла разницу. "title" работает и с отдельными словами, и со строками.

# def int_funk(a):
#     return a.title()
#
#
# print(int_funk(input('Введите слово или строку слов с маленькой буквы: ')))
