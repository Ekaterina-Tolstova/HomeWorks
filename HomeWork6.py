# задание 1

# from time import sleep
#
#
# class TrafficLight:
#     def __init__(self, color):
#         self.__c = color
#
#     def running(self):
#         print('красный')
#         sleep(7)
#         print('желтый')
#         sleep(2)
#         print('зеленый')
#         sleep(5)
#
#
# red = TrafficLight('')
# red.running()


# задание 2

# class Road:
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#
#     def mass_count(self):
#         print(f'Масса асфальта {self._l * self._w * 25 * 0.05}')
#
#
# a = Road(2000, 5)
# a.mass_count()


# задание 3

# class Worker:
#     def __init__(self, name, surname, position, income):
#         self.n = name
#         self.s = surname
#         self.p = position
#         self.i = income
#
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Полное имя: {self.n} {self.s}')
#
#     def get_total_income(self):
#         print(f'Доход с учетом премии: {sum(self.i.values())}')
#
#
# a = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите должность: '),
#              {'wage': float(input('Введите оклад: ')), 'bonus': float(input('Введите бонус: '))})
# a.get_full_name()
# a.get_total_income()


# задание 4

# class Car:
#     def __init__(self, speed, color, name, is_police=None):
#         self.s = speed
#         self.c = color
#         self.n = name
#         self.p = is_police
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn_right(self):
#         print('Машина повернула направо')
#
#     def turn_left(self):
#         print('Машина повернула налево')
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.s} км/ч')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.s > 60:
#             print('Превышение скорости!')
#         else:
#             print(f'Текущая скорость {self.s} км/ч')
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.s > 40:
#             print('Превышение скорости!')
#         else:
#             print(f'Текущая скорость {self.s} км/ч')
#
# class PoliceCar(Car):
#     def police(self): # добавила от себя
#         if self.p is not None:
#             print('Это полицейская машина')
#
#
# car = Car(80, 'grey', 'Auto')
# print(car.c, car.n)
# car.show_speed()
# car_1 = TownCar(65, 'black', 'Mazda')
# print(car_1.c, car_1.n)
# car_1.show_speed()
# car_2 = SportCar(100, 'red', 'FF')
# print(car_2.c, car_2.n)
# car_2.go()
# car_3 = WorkCar(39, 'white', 'KIA')
# print(car_3.c, car_3.n)
# car_3.show_speed()
# car_3.turn_left()
# car_4 = PoliceCar(50, 'blue', 'Ford', 1)
# print(car_4.c, car_4.n)
# car_4.stop()
# car_4.police()


# задание 5

# class Stationery:
#     def __init__(self, title):
#         self.t = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print('Запуск отрисовки ручкой')
#
#
# class Penсil(Stationery):
#     def draw(self):
#         print('Запуск отрисовки карандашом')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print('Запуск отрисовки маркером')
#
#
# st = Stationery('Пишушая принадлежность')
# st.draw()
# st_1 = Pen('Ручка')
# st_1.draw()
# st_2 = Penсil('Карандаш')
# st_2.draw()
# st_3 = Handle('Маркер')
# st_3.draw()
