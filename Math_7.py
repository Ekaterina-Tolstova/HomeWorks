import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# задание 1

# A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
# B = np.array([12, 2, 1])
# print(np.linalg.solve(A, B))

# задание 2

# A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, -5, 0], [11, 4, -7]])
# B = np.array([1, 7, 12, 7, 15])
# print(np.linalg.lstsq(A, B))

# задание 3
import scipy.linalg

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B = np.array([[12, 2, 1]])
# C = np.concatenate((A, B.T), axis=1)
# print(np.linalg.matrix_rank(A, 0.00001))
# print(np.linalg.matrix_rank(C, 0.00001))
'''
Здесь ранг расширенной матрицы больше, чем ранг исходной матрицы,
поэтому система в исходном виде решений не имеет.
Переприсвоим В.
'''
# B = np.array([[0, 0, 0]])
# C = np.concatenate((A, B.T), axis=1)
# print(np.linalg.matrix_rank(A, 0.00001))
# print(np.linalg.matrix_rank(C, 0.00001))
# print(np.linalg.det(A))
'''
Теперь ранги равны, и определитель равен 0,
значит, система имеет бесконечное множество решений.
'''


# задание 4

# A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
# P, L, U = scipy.linalg.lu(A)
# print(L)
# print(U)


# задание 5

# def Q(x, y, z):
#     return x ** 2 + y ** 2 + z ** 2
#
#
# x = np.linspace(-5, 7, 50)
# plt.plot(x, Q(x, 10 * x - 13, 21 * x - 27))  # здесь y и z выражены через х
# plt.grid(True)
# plt.show()
#
# # дальше находим минимум функции
#
#
# def f(x):
#     return x ** 2 + (10 * x - 13) ** 2 + (21 * x - 27) ** 2
#
#
# print(optimize.minimize(f, [1]))
#
# # псевдорешение
#
# A = np.array([[1, 2, -1], [8, -5, 2]])
# B = np.array([1, 12])
# print(np.linalg.lstsq(A, B))

# задание 6
'''
Здесь я не поняла, как найти нормальное псевдорешение. 
'''

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B = np.array([2, 5, 11])
# Q, R = np.linalg.qr(A)
# print(R)
# R1 = R[:2, :2]
# print(R1)
# B1 = np.dot(np.transpose(Q), B)[:2]
# X1 = np.linalg.solve(R1, B1)
# print(X1)
# X = np.append(X1, 0)
# print(X)


