# задание 1

# class Data:
#
#     def __init__(self, day, month, year):
#         self.d = day
#         self.m = month
#         self.y = year
#
#     @classmethod
#     def magic_st(cls):
#         data = [int(el) for el in a.split('-')]
#         day, month, year = data[0], data[1], data[2]
#         print(f'Дата {day:02d}.{month:02d}.{year:04d} н.э.')
#         return cls(day, month, year)
#
#     def valid(self):
#         if self.d not in range(1, 31) or self.m not in range(1, 12) or self.y not in range(1, 2021):
#             return 'Нет такой даты'
#         else:
#             return 'Такая дата существует'
#
#     @staticmethod
#     def val():
#         return Data.magic_st().valid()
#
#
# a = input('Введите дату в формате "день-месяц-год": ')
# print(Data.val())


# задание 2

# class MyErr(Exception):
#
#     def __init__(self, txt):
#         self.txt = txt
#
#
# num1 = input('Введите делимое: ')
# num2 = input('Введите делитель: ')
# try:
#     a = int(num1) / int(num2)
#     if a < 0:
#         raise MyErr('Результат деления - отрицательное число')
# except (ValueError, ZeroDivisionError, MyErr) as err:
#     print(err)
# else:
#     print(f'Результат деления {a:.2f}')
# finally:
#     print('Программа завершена')


# задание 3

"""
Так и не поняла, куда пристроить созданную ошибку
"""


# class MyErr(Exception):
#
#     def __init__(self, txt):
#         self.txt = txt
#
#
# li = []
# while True:
#     a = input('Введите элемент списка. Для завершения списка введите stop: ')
#     if a == 'stop':
#         print('Список завершен')
#         print(li)
#         break
#     try:
#         a = int(a)
#     except ValueError:
#         print('Вы ввели не число')
#     else:
#         li.append(int(a))

# задание 4

# не выполнила (не смогла разобраться)
