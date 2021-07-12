# задание 1

"""
не поняла, почему выдает в ответ на print(m1 + m2)
TypeError: __str__ returned non-string (type NoneType),
хотя получается тоже список списков в конце функции __add__,
и тоже из цифр, как и исходные матрицы.
Там ведь всё получается, хотя тоже не строчные значения?
Еще пыталась перегрузить __str__ через изменение типа переменных на строчные и
print(' '.join(map(''.join, el))),
всё равно та же ошибка в итоге. Дальше поэтому не стала форматировать, чтоб красиво выводить.
"""

# from random import randrange
#
#
# def gen_li():  # генератор списка для матрицы, тут произвольные значения
#     li = []
#     for _ in range(10):
#         li.append([randrange(10) for _ in range(10)])
#     return li
#
#
# class Matrix:
#     def __init__(self, li):
#         self.li = li
#
#     def __str__(self):
#         for el in self.li:
#             print(*el)
#             #
#
#     def __add__(self, other):
#         li_new = []
#         for el in range(len(self.li)):
#             li_new_str = []
#             for j in range(len(self.li[0])):
#                 li_new_str.append(self.li[el][j] + other.li[el][j])
#             li_new.append(li_new_str)
#         return Matrix(li_new)
#
#
# m1 = Matrix(gen_li())
# m1.__str__()
# print(' ')  # чтобы отделить визуально одну матрицу от другой
# m2 = Matrix(gen_li())
# m2.__str__()
# print(' ')
# print(m1 + m2)


# задание 2

# from abc import ABC, abstractmethod
#
#
# class AbsClass(ABC):
#
#     @abstractmethod
#     def count_tex(self):
#         pass
#
#
# class Clothes:
#
#     def __init__(self, p):
#         self.p = p
#         self.li = []
#
#     def count_tex(self):
#         pass
#
#     @property
#     def param(self):
#         return self.p
#
#     @param.setter
#     def param(self, p):
#         if p > 200:
#             self.p = 200
#         elif p < 160:
#             self.p = 160
#         else:
#             pass
#
#
# class Suit(Clothes):
#
#     def __init__(self, p):
#         super().__init__(p)
#         self.count = 2 * (self.p / 100) + 0.3
#
#     def count_tex(self):
#         print(f'Расход ткани на костюм {self.count} м')
#
#
# class Coat(Clothes):
#
#     def __init__(self, p):
#         super().__init__(p)
#         self.count = self.p / 6.5 + 0.5
#
#     def count_tex(self):
#         print(f'Расход ткани на пальто {self.count:.2f} м')
#
#
# class Container:
"""
тут я пыталась сделать композицию, чтобы рассчитать суммарный расход ткани,
но получила AttributeError: type object 'Suit' has no attribute 'count'
"""

#     def __init__(self):
#         self.li = []
#
#     def add_func(self):
#         self.li.append(Suit)
#         self.li.append(Coat)
#         s = 0
#         for el in self.li:
#             s += el.count
#         print(f'ОБщий расход ткани {s} м')
#
#
# suit1 = Suit(180)
# suit1.count_tex()
# suit2 = Suit(220)
# suit2.count_tex()
# coat1 = Coat(54)
# coat1.count_tex()
# com1 = Container()
# com1.add_func()


# задание 3

# class Cell:
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         return f'Число ячеек общей клетки {self.n + other.n}'
#
#     def __sub__(self, other):
#         if self.n > other.n:
#             return f'Разность количества ячеек двух клеток {self.n - other.n}'
#         else:
#             return 'Результат вычитания меньше нуля'
#
#     def __mul__(self, other):
#         return f'Число ячеек общей клетки {self.n * other.n}'
#
#     def __truediv__(self, other):
#         return f'Число ячеек общей клетки {self.n // other.n}'
#
#     def make_order(self, num):
#         a = self.n // num
#         b = self.n % num
#         for el in range(a):
#             print('*' * num)
#         print('*' * b)
#
#
# c1 = Cell(18)
# c2 = Cell(5)
# print(c1 + c2)
# print(c1 - c2)
# print(c1 * c2)
# print(c1 / c2)
# c3 = Cell(12)
# c3.make_order(5)
