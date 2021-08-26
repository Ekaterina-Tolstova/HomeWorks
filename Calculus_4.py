import math

import sympy
from sympy import *
init_printing()


n = sympy.Symbol('n')
a = math.e / ((2 * math.pi * n) ** (1 / (2 * n)))
print(f'Значение предела по упрощенной формуле: {sympy.limit(a, n, oo)}')


n = int(input('Введите номер члена последовательности для расчета по упрощенной формуле '))
a = math.e / ((2 * math.pi * n) ** (1 / (2 * n)))
print(a)

n = int(input('Введите номер члена последовательности для расчета по исходной формуле (не более 170) '))
#  ограничение до 170 - для моего компьютера
b = n / math.factorial(n) ** (1 / n)
print(b)
