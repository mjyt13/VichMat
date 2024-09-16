""" Интерполяция """
import numpy as np
import matplotlib.pyplot as plt
""" Программа содержит описание построение (2 функции) интерполяционного многочлена Лагранжа на равномерной и
 чебышевской сетках, а также задание концов отрезка аппроксимации, интерполируемую функцию """

# Концы отрезка, на котором интерполируется функция
xStart = 0
xEnd = 2*np.pi


# Функция для интерполяции
def f(x):
    return np.abs(np.sin(x))


# Непосредственно интерполяция(равномерная сетка)
def Interpolation(number_of_nodes, start_point, end_point):
    # Чтобы равномерно заполнить массив узлов на отрезке, необходимо к начальной точке прибавить n-1 раз шаг,
    # определяемый из расстояния между концами отрезка и количества узлов
    n = number_of_nodes - 1
    h = abs(end_point - start_point) / n
    # Инициализировать список узлов - корней строимого полинома
    nodes = []

    # Заполнить список узлов от начальной до конечной точек
    i = float(start_point)
    while i <= end_point:
        # Занести в список аргумент
        nodes.append(i)
        i = i + h

    """создать  нулей для начального полинома, а потом прибавлять временный полином"""
    # Создание полинома с нулевыми коэффициентами, так представиться возможным технически складывать многочлены
    poly_nodes = []
    for ii in range(0, len(nodes)):
        poly_nodes.append(0)
    # Многочлены имеют вид a0 + a1 * x ** 1 + ... + an * x ** n, с числом их сложить не получится
    poly = np.polynomial.Polynomial(poly_nodes)

    # Проход по узлам
    for i in range(0, len(nodes)):
        # Сохранить (выписать) настоящее значение x(j)
        j = nodes[i]
        # Создать список оставшихся корней
        temp_nodes = nodes.copy()
        temp_nodes.pop(i)

        # Считать нормировочный коэффициент
        lbm = 1
        for k in temp_nodes:
            lbm = lbm / (j - k)
        # Так как значение функции в узле возможно определить,
        # то можно переходить ко множителю перед слагаемым-полиномом
        lbm = lbm * f(j)

        # Создать слагаемое-полином при помощи списка корней
        temp_poly = np.polynomial.Polynomial.fromroots(temp_nodes)
        # и домножить этот полином на ранее найденную константу
        temp_poly = temp_poly * lbm
        # В NumPy полиномы приводятся сразу к виду a0 * x**n + ... an, минуя (x-x1)(x-x2)(x-x3)*k,
        # поэтому здесь сразу построения промежуточного многочлена осуществляется суммирование найденных слагаемых
        poly = poly + temp_poly

    # Можно вывести найденный полином
    print(poly)

    # Наполнение списков для графиков

    # Создать пустые списки
    arguments = []
    interpolated = []
    analytic = []
    # Наполнить списки аргументов, значений изначальной функции и значений найденного полинома
    i = start_point
    while i <= end_point:
        arguments.append(i)
        interpolated.append(poly(i))
        analytic.append(f(i))
        i += 0.01
    return arguments, interpolated, analytic


# Непосредственно интерполяция(чебышёвская сетка)
def Interpolation2(number_of_nodes, start_point, end_point):
    # Здесь единственным существенным отличием является наполнение списка (формирование сетки)
    nodes = []

    for i in range(0, number_of_nodes):
        product = np.cos(((2 * i + 1) * np.pi) / (2 * (number_of_nodes + 1)))
        t1 = (end_point + start_point) / 2
        t2 = (end_point - start_point) / 2

        nodes.append(t1 + t2 * product)

    poly_nodes = []
    for ii in range(0, len(nodes)):
        poly_nodes.append(0)

    poly = np.polynomial.Polynomial(poly_nodes)

    for i in range(0, len(nodes)):
        # isklychaem isklychaem sohranyaem sohranyaem
        j = nodes[i]
        temp_nodes = nodes.copy()
        # a eto ostavshiesya korni
        temp_nodes.pop(i)

        lbm = 1
        for k in temp_nodes:
            lbm = lbm / (j - k)

        lbm = lbm * f(j)

        # VOT!! Sozdat polynom-slagaemoe
        temp_poly = np.polynomial.Polynomial.fromroots(temp_nodes)
        temp_poly = temp_poly * lbm
        # a teper sdelat NASH polynom
        poly = poly + temp_poly

    # ahahahaha
    print(poly)

    # eto dlya graphicov
    i = start_point
    arguments = []
    interpolated = []
    analytic = []
    while i <= end_point:
        arguments.append(i)
        interpolated.append(poly(i))
        analytic.append(f(i))
        i += 0.01
    return arguments, interpolated, analytic


# graphics+
# Функции построения графиков


def graphics(args, fargs, gargs, hargs):
    plt.title("Интерполяция функции ")
    plt.grid(True)
    plt.plot(args, fargs, args, gargs, args, hargs)
    plt.legend("ARC")
    plt.show()

# Создать 
res1 = Interpolation(13, xStart, xEnd)
res2 = Interpolation2(13, xStart, xEnd)

graphics(res1[0], res1[2], res1[1], res2[1])
