import math

dict_sin = {0.0: 0.0}
delta_x_rad = 0.01 * math.pi / 180
sin_prev = 0
li_grad = [n * 0.01 for n in range(1, 3001)]
for el in li_grad:
    sin_x = sin_prev + ((1 - sin_prev ** 2) ** 0.5) * delta_x_rad
    new_dict_sin = {el: sin_x}
    dict_sin.update(new_dict_sin)
    sin_prev = sin_x
for el in dict_sin.items():
    print(f'{el[0]:.2f} \t {el[1]:.7f}')
