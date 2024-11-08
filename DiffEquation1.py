# Линейные дифференциальные уравнения 2 порядка

# Здесь дифференциальное уравнение 2 порядка с помощью замены искомой функции и её производной становится системой
# дифференциальных уравнений 1 порядка, которые решаются методом Рунге-Кутты 4 порядка

import numpy as np
import matplotlib.pyplot as plt

# начальные условия
h = 1e-4
x0 = 0
y0 = 0
dy0 = 1
# коэффициенты при y' и y, а также конец нахождения функции
xn = np.pi * 4
b = 0
c = 1

# правая часть, явно зависящая от аргумента x
def z(x):
    return x

# здесь производится замена u1 = y', u2 = y

"""
u2' = u1
u1' = f(x) - b * u1 - c * u2
"""

# функция, стоящая в правой части 1 уравнения (u1' = u2)
def g(x, y):
    return y

# функция, стоящая в правой части 2 уравнения (u2' = f(x) - b * u1 - c * u2), f(x) здесь есть z(x), b=0, ибо
# нет понимания, как работать с тремя функциями (типа брать настоящее значение u1k)
def f(x,y,c):
    return z(x) - c * y

# Непосредственно решение системы уравнений с помощью метода Рунге-Кутты 4 порядка
def RungeKutt4(x0, y0, dy0, xn, h):
    # задать массивы для создания функций
    xi = []
    yi = []
    # занести начальные условия в первые значения (для вычисления методом Рунге-Кутты)
    xk = x0 #это аргумент
    u1k = dy0 # это значение функции
    u2k = y0 # это значение производной
    while xk <= xn:
        # внести в массив значения аргумента и искомой функции для составления графиков
        xi.append(xk)
        yi.append(u2k)
        # сохранить предыдущее значение u1 для вычисления u2
        u1k_t = u1k
        # применение метода Рунге-Кутты для u1
        K1 = f(xk, u2k, c)
        K2 = f(xk + (h / 2), u2k + (h / 2) * K1, c)
        K3 = f(xk + (h / 2), u2k + (h / 2) * K2, c)
        K4 = f(xk + h, u2k + h * K3, c)
        u1k = u1k + (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
        # применение метода Рунге-Кутты для u2
        K1 = g(xk,u1k_t)
        K2 = g(xk + (h / 2), u1k_t + (h / 2) * K1)
        K3 = g(xk + (h / 2), u1k_t + (h / 2) * K2)
        K4 = g(xk + h, u1k_t + h * K3)
        u2k = u2k + (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4)

        xk = xk + h
    return xi,yi

# Построение графиков: сетка, занесение массивов и вывод
def graphics(args,fargs):
    plt.title("Решение дифференциального ураавнения y'' + y = x")
    plt.grid(True)
    plt.plot(args, fargs)
    plt.show()

graphics(RungeKutt4(x0,y0,dy0,xn,h)[0],RungeKutt4(x0,y0,dy0,xn,h)[1])