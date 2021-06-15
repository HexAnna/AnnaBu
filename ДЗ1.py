# Булдакова Анна Евгеньевна ДЗ 1
#Home Work 1
#Task 1
name = input('Введите ваше имя:')
age = int(input('Введите ваш возраст:'))
a = (age-18)
print(name, 'на', a, 'года/лет больше 18')
#Task 2
q = int(input('Введите число 1:'))
w = int(input('Введите число 2:'))
e = q+0
r = w+0
print('Число 1:', r, 'Число 2:', e)
#Task 3
import math
print('Введите коэфиценты для уравнения')
print('ax^2 + bx + c = 0')
a = float(input('Коэффициент a:'))
b = float(input('Коэффициент b:'))
c = float(input('Коэффициент c:'))
D = b ** 2 - 4 * a * c
print('Дискриминант', round(D, 2))
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print('x1=', round(x1, 2), 'x2= ', round(x2, 2))
elif D == 0:
    x = -b / (2*a)
    print('x =', round(x, 2))
else:
    print('Нет корней')
