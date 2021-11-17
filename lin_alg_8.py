import numpy as np
from numpy.linalg import norm

'''
Задание 1.
'''
A = np.array([[1, 2, 0], [0, 0, 5], [3, -4, 2], [1, 6, 5], [0, 1, 0]])
np.set_printoptions(precision=2, suppress=True)
U, s, W = np.linalg.svd(A)
V = W.T
D = np.zeros_like(A, dtype=float)
D[np.diag_indices(min(A.shape))] = s
print(f'Матрица D: \n {D}')
print(f'Матрица U:\n {U}')
print(f'Матрица V:\n {V}')
print(f'Проверка: \n {np.dot(np.dot(U, D), V.T)}')

'''
Задание 2.
'''
print(f'Евклидова норма матрицы А: \n {norm(A, ord=2):.2f}')

'''
Задание 3.
'''
print(f'Норма Фробениуса матрицы А: \n {norm(A, ord=None):.2f}')
