# Численное интегрирование
# (1) в первой части записана функция, от которой находится интеграл и его аналитически надйенное значение
# Примечание: в данной программе интеграл имеет переменный верхний предел
# (2) во второй части реализованы численные методы нахождения интеграла
# метод прямоугольников (слева, посередине и справа), метод трапеций и метод парабол
import numpy as np
import matplotlib.pyplot as plt

# Часть 1

# Обозначение шага разностной сетки
h = 1e-2

# Подынтегральная функция
def f(x):
    return np.exp(-x)

# Аналитически вычисленный неопределенный интеграл
def Ia_f(x):
    return (-np.exp(-x))

# Аналитически найденный определенный интеграл
def I_f(x):
    return (1 - np.exp(-x))


# Часть 2

# Все реализации имеют одинаковую структуру записи, поэтому подробное описание даётся в первой функции,
# после чего будут закомментированы только строчки с нижним переменным пределом, а также строка перед непосредственно
# формулой для вычисления шага

def integr_rectangle_M(t):
    # Используется костыль для создания более точного отрезка интегрирования
    # S = int(s/h)
    T = int(t / h)
    # Инициализируются основные переменные для хранения результатов (переменная для числового значения,
    # массивы для построения графиков отклонения от аналитически надйенного интеграла)
    I = 0
    args = []
    fargs = []
    vargs = []
    # for i in range(S,T)
    for i in range(0, T):
        # Вносится в первый массив само значение из отрезка
        args.append(i * h)
        # Вносится слагаемое в числовую переменную
        # Прямоугольники по середине, здесь используется f(i+1/2)*h
        I = I + f((i + 0.5) * h) * h
        # Вносится в массив найденное численным методом значение части интеграла
        fargs.append(I)
        # Вносится в массив разность между найденным значением(прямоугольником) и аналитически найденным интегралом в
        # этой же точке
        vargs.append(f((i + 0.5) * h) * h - (Ia_f((i+1) * h) - Ia_f(i * h)))
    # Стандартные процедуры: нанесение сетки, обозначение названия и вывод на экран
    plt.figure().set_figheight(11)
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Интегрирование методом прямоугольников (середина)")
    plt.plot(args, fargs)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.title("Отклонение численного метода от аналитического решения")
    plt.plot(args, vargs)
    plt.show()
    return I

# Метод прямоугольников (слева)
def integr_rectangle_L(t):
    # S = int(s/h)
    T = int(t / h)
    I = 0
    args = []
    fargs = []
    vargs = []
    # for i in range(S,T)
    for i in range(0, T):
        args.append(i * h)
        # прямоугольники слева, используется значение f(i)
        I = I + f(i * h) * h
        fargs.append(I)
        vargs.append(f(i * h) * h - (Ia_f((i+1) * h) - Ia_f(i * h)))
    plt.figure().set_figheight(11)
    plt.subplot(2,1,1)
    plt.grid(True)
    plt.title("Интегрирование методом прямоугольников (слева)")
    plt.plot(args, fargs)
    plt.subplot(2,1,2)
    plt.grid(True)
    plt.title("Отклонение численного метода от аналитического решения")
    plt.plot(args,vargs)
    plt.show()
    return I

# Метод прямоугольников (справа)
def integr_rectangle_R(t):
    # S = int(s/h)
    T = int(t / h)
    I = 0
    args = []
    fargs = []
    vargs = []
    # for i in range(S,T)
    for i in range(0, T):
        args.append(i * h)
        # Прямоугольники справа, используется значение f(i+1)
        I = I + f((i + 1) * h) * h
        fargs.append(I)
        vargs.append(f((i + 1) * h) * h - (Ia_f((i+1) * h) - Ia_f(i * h)))
    plt.figure().set_figheight(11)
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Интегрирование методом прямоугольников (справа)")
    plt.plot(args, fargs)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.title("Отклонение численного метода от аналитического решения")
    plt.plot(args, vargs)
    plt.show()
    return I

# Метод трапеций
def integr_trapezoid(t):
    # S = int(s/h)
    T = int(t / h)
    I = 0
    args = []
    fargs = []
    vargs = []
    # for i in range(S,T)
    for i in range(0, T):
        args.append(i * h)
        # Трапеции, используется найденное по формуле ( f(i)+f(i+1) ) * (h/2)
        I = I + (f(i * h) / 2 + f((i + 1) * h) / 2) * h
        fargs.append(I)
        vargs.append((f(i * h) / 2 + f((i + 1) * h) / 2) * h - (Ia_f((i+1) * h) - Ia_f(i * h)))
    plt.figure().set_figheight(11)
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Интегрирование методом трапеций")
    plt.plot(args, fargs)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.title("Отклонение численного метода от аналитического решения")
    plt.plot(args, vargs)
    plt.show()
    return I

# Метод Симпсона (парабол)
def integr_Simpson(t):
    # S = int(s/h)
    T = int(t / h)
    I = 0
    args = []
    fargs = []
    vargs = []
    # for i in range(S,T)
    for i in range(0, T):
        args.append(i * h)
        # Приближение к параболам, используется формула (f(i * h) + 4 * f((i + 0.5) * h) + f((i + 1) * h)) * (h / 6)
        I = I + (f(i * h) + 4 * f((i + 0.5) * h) + f((i + 1) * h)) * (h / 6)
        fargs.append(I)
        vargs.append((f(i * h) + 4 * f((i + 0.5) * h) + f((i + 1) * h)) * (h / 6) - (Ia_f((i+1) * h) - Ia_f(i * h)))
    """plt.figure().set_figheight(11)
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Интегрирование методом парабол")
    plt.plot(args, fargs)
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.title("Отклонение численного метода от аналитического решения")
    plt.plot(args, vargs)
    plt.show()"""
    return round(float(I),2)

# джим корбетт ясон бернадзе дина санычанг
