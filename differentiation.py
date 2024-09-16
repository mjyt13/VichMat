# Численное дифференцирование
# (1) В первом блоке реализовано нахождение функции её аналитически найденной первой и второй производных, а также
# обозначается точка и шаг для выяснения точности вычисленного разностного аналога
# (2) Во втором блоке реализовано нахождение производной с помощью разностного аналога и сравнение с аналитически
# найденной производной в точке
# (3) В третьем блоке строится график производной для уточнения погрешности
# Примечание: точность вычисления аналитически найденнойь производной в точке ограничивается машинной точностью
import numpy as np
import matplotlib.pyplot as plt

# (1) задание параметров

# Функция, от которой находится производная в точке
def f(x):
    # Здесь находится конструкция try-except для того, чтобы учесть невозможность вычисления функции в конкретной точке
    # и не остановить работу программы
    try:
        return np.sin(x)
    except:
        print("не существует функции в точке "+str(x))
        pass

# Аналитически найденная производная
def df(x):
    # Опять же, здесь конструкция try-except для учёта несуществования функции в некоторых точках но продолжения работы
    try:
        return np.cos(x)
    except:
        print("не существует производной точке "+str(x))
        pass

def d2f(x):
    try:
        return -np.sin(x)
    except:
        print("не существует второй производной в точке "+str(x))
        pass

# шаг, используемый для вычисления производной
h = 1e-6

# точка, в которой будет вычисляться производная, а также размер отрезка для построения графика
a = np.pi * 2


# (2) Дифференцирование

# Во всех трёх функциях реализовано вычисление,
# а также отклонение от аналитически найденной производной в конкретной точке

# Дифференцирование слева
def diffL(a):
    # Функция в настоящей точке и функция в предыдущей точке
    b = (f(a)-f(a-h))/h
    print("производная слева в точке "+str(a)+" равна "+str(b))
    print("погрешность равна "+str(abs(b-df(a))))

# Дмфференцирование справа
def diffR(a):
    # Функция в следующей точке и функция в настоящей точке
    b = (f(a+h)-f(a))/h
    print("производная справа в точке "+str(a)+" равна "+str(b))
    print("погрешность равна "+str(abs(b-df(a))))

# Дифференцирование с обеих сторон
def diffLR(a):
    # Функция в следующей точке и функция в предыдущей точке
    b = (f(a+h)-f(a-h))/(2*h)
    print("производная слева-справа в точке "+str(a)+" равна "+str(b))
    print("погрешность равна "+str(abs(b-df(a))))

# Дифференцирование второго порядка
def diff2(a):
    b = (f(a+h) - 2 * f(a) + f(a-h))/(h**2)
    print("вторая производная в точке " + str(a) + " равна " + str(b))
    print("погрешность равна " + str(abs(b - d2f(a))))


# Построение графиков производных

def diffL_graphics(a):
    # Здесь находится костыль - преобразование типов, необходимое для реализации цикла for
    b =int( a / h)
    # Создаётся три массива для построения графиков
    args = []
    fargs = []
    plt.title('Дифференцирование слева', fontsize=22)
    for i in range(-b, b):
        # Вносятся точки в списки
        args.append(i*h)
        fargs.append(((f((i+1)*h)-f(i*h))/h)-df(i*h))
        # Строится ноль
    plt.grid(True)
    # Создаётся грфик
    plt.plot(args, fargs)
    plt.show()
    pass

# Во всех остальных функциях ровно те же действиях за исключением метода нахождения производной
def diffR_graphics(a):
    b = int(a / h)
    args = []
    fargs = []
    plt.title('Дифференцирование справа', fontsize=22)
    for i in range(-b, b):
        args.append(i * h)
        fargs.append(((f(i * h) - f((i-1) * h)) / h) - df(i*h)) # Это относится к дифференцированию справа
    plt.grid(True)
    plt.plot(args, fargs)
    plt.show()
    pass

def diffLR_graphics(a):
    b = int(a / h)
    args = []
    fargs = []
    plt.title('Дифференцирование с обеих сторон', fontsize=22)
    for i in range(-b, b):
        args.append(i * h)
        fargs.append(((f(i * h + h) - f(i * h - h)) / (2*h))-df(i*h)) # Это относится к дифференцированию с обеих сторон
    plt.grid(True)
    plt.plot(args, fargs)
    plt.show()
    pass

diffL(a)
diffR(a)
diffLR(a)
diff2(a)
diffL_graphics(a)
diffR_graphics(a)
diffLR_graphics(a)