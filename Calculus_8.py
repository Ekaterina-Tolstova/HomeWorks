"""
задание 3, 4
"""
#
# import matplotlib_inline
# import numpy as np
# from scipy.optimize import fsolve
#
#
# def equations(p):
#     x, y = p
#     return x ** 2 - y ** 2 + 3 * x * y ** 3 - 2 * x ** 2 * y ** 2 + 2 * x - 3 * y - 5, 3 * y ** 3 - 2 * x ** 2 + 2 * x ** 3 * y - 5 * x ** 2 * y ** 2 + 5
#
#
# solv = list()
# for j in np.arange(-5, 5, 1):
#     for i in np.arange(-5, 5, 1):
#         (x, y), info, ier, mesg = fsolve(equations, (j, i), full_output=True)
#         if ier == 1:
#             solv.append([int(x * 10 ** 7) / 10 ** 7, int(y * 10 ** 7) / 10 ** 7])
# solv_orig = list()
# for el in solv:
#     try:
#         solv_orig.index(el)
#     except:
#         solv_orig.append(el)
# solv.clear()
# print(solv_orig) # список пар корней

"""
задание 5
"""

# import numpy as np
# from scipy.interpolate import splev, splrep
# from matplotlib import pylab as plt
#
# """
# восстановление функций методом сплайнов
# """
#
# n = 10000
# h = 20 / n
# x = np.arange(0, 20, h)
# x = np.append(x, 20)
# f_d = np.array([0])
# g_d = np.array([1])
#
# while n != 0:
#     f_d = np.append(f_d, f_d[-1] + 0.5 * g_d[-1] * h)
#     g_d = np.append(g_d, g_d[-1] + (2 - 2 * f_d[-1]) * h)
#     n -= 1
#
# spl_f = splrep(x, f_d)
# spl_g = splrep(x, g_d)
#
#
# def f_f(k):
#     return splev(k, spl_f)
#
#
# def f_g(k):
#     return splev(k, spl_g)
#
# """
# график
# """
#
# plt.figure(figsize=(10, 7))
# plt.axis([0, 20, -3, 3])
#
# x = np.linspace(0, 20, 200)
# y1 = f_f(x)
# y2 = f_g(x)
#
# plt.plot(x, y1, c='b')
# plt.plot(x, y2, c='r')
# plt.show()

"""
задание 6
"""

# def equations(p):
#     x = p
#     return f_f(x) - f_g(x)
#
#
# solv = list()
# for j in np.arange(1, 20, 1):
#     (x), info, ier, mesg = fsolve(equations, j, full_output=True)
#     if ier == 1:
#         solv.append([int(x * 10 ** 7) / 10 ** 7])
# solv_orig = list()
# for el in solv:
#     try:
#         solv_orig.index(el)
#     except:
#         solv_orig.append(el)
# solv.clear()
# print(solv_orig)  # список корней
