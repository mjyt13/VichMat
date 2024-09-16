"""Сортировки"""
"""Представлены реализации трёх алгоритмов сортировки для трех разных создаваемых массивов ЦЕЛЫХ чисел.
Сначала представлена функция создания массива псевдослучайных чисел. Затем идут три функции:
пузырьковая сортировка с поиском минимума и максимума, рекурсивная сортировка с разделением на 2
меньших массива и сортировка подсчётом"""



from sympy import *  # symbols, diff
import numpy as np
import random


# Создание массивов
def f(kolvo):
    massive = []
    for i in range(0, kolvo):
        # Непосредственно заполнение массива
        massive.append(random.randint(2, 67))
    return massive


# Пузырьковая сортировка
def bubble_EX(mass):
    # Отображение начального массива
    print(mass)
    # Для двух сортировок вводятся переменные сравнений и перемещений элементов
    compares = 0
    swaps = 0

    # Надо пройти только половину массива, так как внутри одной итерации находятся минимум и максимум
    for i in range(0, len(mass) // 2):
        # поиск локальных максимумов и минимумов
        mass_min = mass[i]
        mass_max = mass[i]
        # для перестановок также понадобятся индексы
        index_min = i
        index_max = i
        for j in range(i, len(mass) - i):
            # нахождение min
            compares += 1
            if (mass[j] < mass_min):
                mass_min = mass[j]
                index_min = j
            compares += 1
            # нахождение max
            if (mass[j] > mass_max):
                mass_max = mass[j]
                index_max = j
        # После нахождения максимумов и минимумов необходимо поменять их местами с первыми и последними элементами
        if (mass[i] > mass_min):
            # Вынести первый элемент
            mass_temp = mass[i]
            # Присвоить первому элементу значение минимума
            mass[i] = mass_min
            swaps += 1
            # Присвоить элементу с ранее минимальным значением значение первого элемента
            mass[index_min] = mass_temp
        # Аналогично
        compares += 1
        if (mass[j] < mass_max):
            mass_temp = mass[j]
            mass[j] = mass_max
            swaps += 1
            mass[index_max] = mass_temp
    print("{0} comparisons {1} swaps".format(compares, swaps))
    return mass


# Быстрая сортировка
def quickie(massive):
    # print(massive)

    mass = massive.copy()

    #compares += 1
    if len(mass) <= 1:
        return mass
    # Опорным элементом является первый, его и вынести
    sort_value = [mass[0]]
    mass.pop(0)
    # Создать 2 массива для больших, также меньших или равных значений
    mass_less = []
    mass_more = []
    # Наполнить массивы соответствующими значениями
    for i in range(0, len(mass)):
        #compares += 1
        if mass[i] > sort_value[0]:
            mass_more.append(mass[i])
        #compares += 1
        if mass[i] <= sort_value[0]:
            mass_less.append(mass[i])
    # Вызов функции сортировки

    mass_more_edit = quickie(mass_more)
    mass_less_edit = quickie(mass_less)
    # Соединение массивов
    #swaps += 1
    mass_final = mass_less_edit + sort_value + mass_more_edit
    # print(mass_final)

    return mass_final


# Сортировка подсчётом
def counter(massive):
    print(massive)
    mass = massive.copy()

    compares = 0
    swaps = 0
    #
    mass_min = mass[0]
    mass_max = mass[0]
    # Получение максимума и минимума для построения массива вхождений
    for i in range(1, len(mass)):
        if mass[i] > mass_max:
            mass_max = mass[i]
        if mass[i] < mass_min:
            mass_min = mass[i]

    # Создание массива вхождений каждого числа от минимума до максимума
    entries = []
    # И его наполнение нулями
    i = mass_min
    while i <= mass_max:
        entries.append(0)
        i = i + 1

    # Отметить вхождения чисел (от мин до макс)
    for i in mass:
        compares += 1
        entries[i-mass_min] = entries[i-mass_min] + 1

    # Начать перезаписывать изначальный массив
    i = mass_min
    berry = 0  # это индекс для массива
    while i <= mass_max:
        # Здесь происходит переписывание элемента массива столько раз, сколько входит число
        for j in range(0, entries[i-mass_min]):
            swaps += 1
            mass[berry] = i
            # Со смещением индекса
            berry = berry + 1
        i = i + 1
    print("{0} comparisons {1} swaps".format(compares,swaps))
    return mass


print(bubble_EX(f(random.randint(7, 11))))
print()
kirka = f(random.randint(7, 11))
print(kirka)
print(quickie(kirka))
print()
print(counter(f(random.randint(7,11))))