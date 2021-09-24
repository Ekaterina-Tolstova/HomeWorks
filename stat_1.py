import itertools
import math


def funk_c(n, k):
    c = math.factorial(n)/(math.factorial(k)*math.factorial(n - k))
    return c


p = funk_c(13, 4) / funk_c(52, 4)
print(f'1а). Вероятность того, что все карты - крести, равна {p:.4f}')

p = 1 - funk_c(48, 4) / funk_c(52, 4)
print(f'1б). Вероятность того, что среди 4-х карт окажется хотя бы один туз, равна {p:.4f}')

n = '0123456789'
k = 3
j = 0
for i in itertools.combinations(n, k):
    j += 1
print(f'2. Вероятность открыть дверь с первой попытки равна {1 / j:.4f}')

p = funk_c(9, 3) * funk_c(6, 0)/funk_c(15, 3)
print(f'3. Вероятность того, что все извлеченные детали окрашены, равна {p:.4f}')

p = funk_c(2, 2) * funk_c(98, 0) / funk_c(100, 2)
print(f'4. Вероятность того, что оба приобретенных билета выигрышные, равна {p:.4f}')
