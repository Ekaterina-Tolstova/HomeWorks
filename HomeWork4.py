# задание 1

# from sys import argv
#
# work_hour, rate, bonus = map(int, argv[1:])
# print(f'Зарплата сотрудника {work_hour * rate + bonus}')

# задание 2.

# from random import randint
#
# li = []
# for el in range(randint(2, 20)):
#     li.append(randint(1, 100))
# print(li)
# n = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
# print(n)

# задание 3

# n = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
# print(n)

# задание 4

# li = [47, 10, 2, 5, 47, 23, 2, 50, 10, 10, 89, 1]
# n = [el for el in li if li.count(el) == 1]
# print(n)

# задание 5

# from functools import reduce
#
#
# li = [el for el in range(100, 1001, 2)]
# print(li)
# print(reduce(lambda a, b: a * b, li))

# задание 6

# from itertools import count, cycle


# start_num = 3
# for el in count(start_num):
#     if el > 10:
#         break
#     else:
#         print(el)


# li = [1, 2, 3]
# end = 10
# i = 0
# for el in cycle(li):
#     if i > end:
#         break
#     else:
#         print(el)
#         i += 1


# задание 7

# def fact(n):
#     i = 1
#     for el in range(1, n + 1):
#         i = el * i
#         yield i
#
#
# num = int(input('Введите число для расчета факториала: '))
# for el in fact(num):
#     print(el)
