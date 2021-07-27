# задание 1

from matplotlib import numpy as np
from matplotlib import pyplot as plt

# x = np.arange(0, 5.01, 0.01)
# k = 1
# k1 = 2
# k2 = 3
# a = 4
# a1 = 5
# a2 = 6
# b = 7
# b1 = 8
# b2 = 9
# y = k * x ** 2 + a * x + b
# y1 = k1 * x ** 2 + a1 * x + b1
# y2 = k2 * x ** 2 + a2 * x + b2
# plt.plot(x, y)
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()

# задание 3.1 (полярные координаты в декартовы)

# r = float(input('Введите значение вектора: '))
# ang = float(input('Введите значение угла в градусах: '))
# ang_ = ang * np.pi / 180
# x = r * np.cos(ang_)
# y = r * np.sin(ang_)
# print(f'Декартовы координаты: {x}, {y}')

# задание 3.2 (график окружности в полярных координатах)

# theta = np.arange(0, np.pi, np.pi / 254)
# y = 5 * np.sqrt(1 - np.cos(theta) ** 2)
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, y)
# ax.set_rmax(5.1)
# ax.set_rticks([1, 2, 3, 4])
# ax.grid(True)
# ax.set_title('График окружности в полярных координатах', va='bottom')
# plt.show()

# задание 3.3 (график отрезка прямой в полярных координатах)

# theta = np.arange(20 * np.pi / 180, 38 * np.pi / 180, np.pi / 254)
# r = 0.5 / (np.cos(theta) - np.pi / 4)
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, r)
# ax.set_rmax(25)
# ax.set_rticks([5, 10, 15, 20])
# ax.grid(True)
# ax.set_title('График отрезка прямой в полярных координатах', va='bottom')
# plt.show()

# задание 4.
'''
Сначала графики, там видно, что есть 3 корня у системы уравнений.
Решением системы уравнение + неравенство будет объединение областей 
от бесконечности до -1 и от 1 до плюс бесконечности 
т.к. функция параболы на отрезке от -1 до 1 отрицательная,
а функция экспоненты всегда положительная.
'''

# import math
# from scipy.optimize import fsolve
#
# x = np.arange(-12, 5, 0.01)
# y = (math.e ** x + x - 1) / x
# y1 = x ** 2 - 1
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.grid()
# plt.plot(x, y)
# plt.plot(x, y1)
# ax.hlines(0, -12, 5)
# plt.show()
#
#
# def equations(p):
#     x_, y_ = p
#     return [math.e ** x_ + x_ * (1 - y_) - 1, x_ ** 2 - y_ - 1]
#
#
# root1 = fsolve(equations, (5, 5))
# print(root1)
# root2 = fsolve(equations, (3, 3))
# print(root2)
# root3 = fsolve(equations, (-2, 0))
# print(root3)
