# sw-4-5.py
from sw import calc_truangle_square_gerone_calc

a = int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

print('S =', calc_truangle_square_gerone_calc(a, b, c))