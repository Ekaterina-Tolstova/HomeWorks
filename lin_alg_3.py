import numpy as np

A = np.array([[0, 1, 2, 7], [2, 6, 3, 9], [5, 8, 0, 1]])
B = np.array([[3, 7, 9], [5, 4, 6], [3, 11, 10], [2, 5, 5]])


def func_mult_matrix(A, B):
    if len(A[1]) / len(B) != 1:
        return print('Количество столбцов в А не равно количеству строк в В. Операция невозможна.')
    else:
        c = []
        d = []
        el_c = 0
        for i in range(0, len(A)):
            for j in range(0, len(B[i])):
                for p in range(0, len(A[1])):
                    el_c += A[i][p] * B[p][j]
                c.append(el_c)
                el_c = 0
            d.append(c)
            c = []
    d1 = np.array(d)
    d2 = np.dot(A, B)
    return print(f'{d1}\n Проверка:\n {d2}')


func_mult_matrix(A, B)
