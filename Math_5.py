import numpy as np
import matplotlib.pyplot as plt
import itertools
import math

# задание 1

# from random import randint
# for i in range(0, 5):
#     a = input('Нажмите ввод')
#     x = randint(0, 36)
#     print(f'Выпало {x}')


# задание 2.1
'''
Проверка теоремы сложения вероятностей.
Поскольку события А и В противоположные (в случае монетки), то Р(А) + Р(В) должно быть 1.
'''
# k, m = 0, 0
# n = 100
# for i in range(0, n):
#     x = randint(0, 1)
#     if x == 0:
#         k += 1
#     else:
#         m += 1
# p_k = k / n
# m_k = m / n
# print(f'Сумма вероятностей событий равна {p_k + m_k}')

# задание 2.2
'''
Здесь строится гистограмма значений
'''

# rng = np.random.RandomState(0)
# li = []
# for i in range(0, 10):
#     x = rng.rand(10)
#     li.append(x)
# x_s = sum(li)
# plt.bar(np.arange(len(x_s)), x_s)
# plt.xlabel('x')
# plt.ylabel('Значения')
# plt.title('Гистограмма значений')
# plt.show()

# задание 3

# rng = np.random.RandomState(0)
# k, n = 0, 10
# a = rng.randint(0, 2, n)
# b = rng.randint(0, 2, n)
# c = rng.randint(0, 2, n)
# d = rng.randint(0, 2, n)
# x = a + b + c + d
# for i in range(0, n):
#     if x[i] == 2:
#         k += 1
# print(a, b, c, d)
# print(x)
# print(f'Количество успешных испытаний {k}, '
#       f'Общее количество испытаний {n}, '
#       f'Вероятность успеха {k / n}')
# c_k_n = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))  # коэффициент
# p = c_k_n / 2 ** n  # частный случай для формулы Бернулли при равновероятных событиях
# print(f'Вероятность того, что орел выпадет ровно 5 раз из 10, составляет {p}')
# k, n = 3, 50
# c_k_n = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))  # коэффициент
# p_1 = c_k_n * (k / n) ** k * (1 - k / n) ** (n - k)  # формула Бернулли
# print(f'Вероятность того, что событие наступит ровно 3 раза из 50, составляет {p_1}')

# задание 4

# n = 'математика'
# k = 3
# j = 0
# for i in itertools.combinations(n, k):
#     print(''.join(i))
#     j += 1
# print(f'Всего {j} сочетаний')
# for i in itertools.permutations(n, k):
#     print(''.join(f for f in i))
#     j += 1
# print(f'Всего {j} размещений')

# задание 5

# rng = np.random.RandomState(0)
# n = 100
# r = 0.9
# x = rng.rand(n)
# m_x = np.sum(x) / n  # среднее квадр. отклонение х
# y = r * x + (1 - r) * rng.rand(n)
# m_y = np.sum(y) / n  # среднее квадр. отклонение у
# d_x = 0  # дисперсия х
# d_y = 0  # дисперсия у
# summ_mult_disp = 0  # сумма произведения дисперсий х и у
# summ_disp_x_sqr = 0  # сумма квадратов дисперсий х
# summ_disp_y_sqr = 0  # сумма квадратов дисперсий у
# for el in range(0, n):
#     summ_mult_disp += (x[el] - m_x) * (y[el] - m_y)
#     summ_disp_x_sqr += (x[el] - m_x) ** 2
#     summ_disp_y_sqr += (y[el] - m_y) ** 2
# plt.plot(x, y, 'o')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()
# a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
# b = (np.sum(y) - a * np.sum(x)) / n
# R = summ_mult_disp / np.sqrt(summ_disp_x_sqr * summ_disp_y_sqr)  # корреляция
# A = np.vstack([x, np.ones(len(x))]).T
# a1, b1 = np.linalg.lstsq(A, y)[0]
# print(a, b)
# print(a1, b1)
# print(R)
# plt.plot([0, 1], [b, a + b])
# plt.show()
