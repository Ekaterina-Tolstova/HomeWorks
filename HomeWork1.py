
# задание 1

# a = 3
# b = 'text'
# c = 2.85
# print(a, b, c)
# num_1 = int(input('Введите целое число: '))
# print('Вы ввели ', num_1)
# num_2 = float(input('Введите десятичное число: '))
# print('Вы ввели ', num_2)
# text = input('Введите текст: ')
# print('Вы ввели ', text)

# задание 2

# t = int(input('Введите время в секундах: '))
# num_h = t // 3600
# t -= num_h * 3600
# num_m = t // 60
# num_s = t - num_m * 60
# print(f'Время {num_h:02d}:{num_m:02d}:{num_s:02d}')

# задание 3

# num = input('Введите число n ')
# num_1 = int(num)
# num_2 = int(num * 2)
# num_3 = int(num * 3)
# print(f'Сумма n+nn+nnn равна {num_1 + num_2 + num_3}')

# задание 4

# num = int(input('Введите целое положительное число '))
# max_num = 0
# while num > 0:
#     a = num // 10
#     num_1 = num - a * 10
#     if num_1 > max_num:
#         max_num = num_1
#     num = a
# print('Самая большая цифра в числе ', max_num)

# задание 5

# profit = int(input('Введите выручку '))
# cost = int(input('Введите издержки '))
# if profit > cost:
#     print(f'Ваша фирма работает с прибылью, рентабельность составляет {((profit / cost - 1) * 100):.2f}%')
#     staff_num = int(input('Введите численность сотрудников '))
#     print(f'Прибыль на одного сотрудника составляет {(profit - cost) / staff_num}')
# else:
#     print('Ваша фирма работает с убытком')

# задание 6

# a = float(input('Введите результат первого дня в км.: '))
# b = float(input('Введите желаемый результат в км.: '))
# i = 0
# while a < b:
#     a += a * 0.1
#     i += 1
# print(f'Желаемый результат будет достигнут на {i} день')
