import numpy as np
'''
Задания 2, 3, 5.
Сначала сделано задание 5 - алгоритм LU-разложения.
Функции:
def LU_decomp - собственно разложение
def get_L - получение матрицы L
def get_U - получение матрицы U
def solve_LU - решение СЛАУ методом LU-разложения.
'''

'''
Задание 5.
'''


def LU_decomp(A):
    LU_matrix = np.array(np.zeros([len(A), len(A[1])]))
    n = len(A)
    for k in range(n):
        for j in range(k, n):
            LU_matrix[k, j] = A[k, j] - LU_matrix[k, :k] @ LU_matrix[:k, j]
        for i in range(k + 1, n):
            LU_matrix[i, k] = (A[i, k] - LU_matrix[i, :k] @ LU_matrix[:k, k]) / LU_matrix[k, k]
    return LU_matrix


def get_L(M):
    L = M.copy()
    for i in range(len(L)):
        L[i, i] = 1
        L[i, i + 1:] = 0
    return L


def get_U(M):
    U = M.copy()
    for i in range(1, len(U)):
        U[i, :i] = 0
    return U


def solve_LU(L, U, b):
    y = np.zeros(len(L))
    for i in range(0, len(y)):
        y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]
    x = np.zeros(len(U))
    for i in range(1, len(x) + 1):
        x[-i] = (y[-i] - U[-i, -i:] @ x[-i:]) / U[-i, -i]
    return x


'''
Задание 2.
А - матрица к заданию 2а), В - матрица к заданию 2б).
'''
A = np.array([[1, 2, 4], [2, 9, 12], [3, 26, 30]])
M = LU_decomp(A)
L = get_L(M)
print(f'2а) Матрица L: \n {L}')
U = get_U(M)
print(f'2а) Матрица U: \n {U}')
B = np.array([[1, 1, 2, 4], [2, 5, 8, 9], [3, 18, 29, 18], [4, 22, 53, 33]])
M = LU_decomp(B)
L = get_L(M)
print(f'2б) Матрица L: \n {L}')
U = get_U(M)
print(f'2б) Матрица U: \n {U}')

'''
Задание 3.
'''
A_koef = np.array([[2, 1, 3], [11, 7, 5], [9, 8, 4]])
B_vector = np.array([1, -6, -5])
Y = LU_decomp(A_koef)
L = get_L(Y)
U = get_U(Y)
X = solve_LU(L, U, B_vector)
print(f'3. Вектор ответа: \n {X}')
