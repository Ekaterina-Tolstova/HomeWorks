
# задание 1


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
#         return '\n'.join(str(i) for i in self.li)
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
# print(m1.__str__())
# print(' ')  # чтобы отделить визуально одну матрицу от другой
# m2 = Matrix(gen_li())
# print(m2.__str__())
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
#
#
#    def __init__(self):
#         self.li = []
#
#     def add_func(self, *args):
#         for arg in args:
#             self.li.append(arg)
#         s = 0
#         for el in self.li:
#             s += el.count
#         print(f'ОБщий расход ткани {s:.2f} м')
#
#
# suit1 = Suit(180)
# suit1.count_tex()
# suit2 = Suit(220)
# suit2.count_tex()
# coat1 = Coat(54)
# coat1.count_tex()
# com1 = Container()
# com1.add_func(suit1, suit2, coat1)


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
