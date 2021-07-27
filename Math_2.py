
# задание 1

# def func(x, y, z):
#     return f'Длина вектора равна {((x ** 2 + y ** 2 + z ** 2) ** 0.5):.2f}'
#
#
# a = float(input('Введите координату вектора: '))
# b = float(input('Введите следующую координату вектора: '))
# c = float(input('Введите следующую координату вектора или 0: '))
# print(func(a, b, c))


# задание 3

# окружность

from matplotlib import numpy as np
from matplotlib import pyplot as plt
# r = 5
# x = np.arange(0, 5.01, 0.01)
# y = (abs(r ** 2 - x ** 2)) ** 0.5
# plt.plot(x, y)
# plt.plot(-x, y)
# plt.plot(-x, -y)
# plt.plot(x, -y)
# plt.show()

# эллипс

# a = 10
# b = 5
# x = np.arange(-10, 5.1, 0.1)
# y = ((b ** 2) * (1 - (x ** 2) / a ** 2)) ** 0.5
# plt.plot(x, y)
# plt.plot(-x, y)
# plt.plot(-x, -y)
# plt.plot(x, -y)
# plt.show()

# гипербола

# k = 0.5
# x = np.arange(0, 5.1, 0.1)
# y = k / x
# plt.plot(x, y)
# plt.plot(-x, -y)
# plt.show()

# задание 5
# две параллельные плоскости

from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import Axes3D
# fig = figure()
# ax = Axes3D(fig)
# X = np.arange(-5, 5, 0.05)
# Y = np.arange(-5, 5, 0.05)
# X, Y = np.meshgrid(X, Y)
# Z1 = 1 - 2 * X - 3 * Y
# Z2 = -12 - 2 * X - 3 * Y
# ax.plot_surface(X, Y, Z1)
# ax.plot_surface(X, Y, Z2)
# plt.show()

# две поверхности второго порядка

# fig = figure()
# ax = Axes3D(fig)
# X = np.arange(-5, 5, 0.05)
# Y = np.arange(-5, 5, 0.05)
# X, Y = np.meshgrid(X, Y)
# Z1 = (100 - (X - 2) ** 2 - (Y - 1) ** 2) ** 0.5
# Z2 = X ** 2 / 4 + Y ** 2 / 9
# ax.plot_surface(X, Y, Z1)
# ax.plot_surface(X, Y, Z2)
# plt.show()
