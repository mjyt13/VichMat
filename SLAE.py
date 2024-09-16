# Создадим матрицу коэффициентов при переменных и числовых значений
# Матрица будет представлять собой массив массивов, где первые числа - коэффициенты, а последнее - число

# Здесь будет рассмотрена система уравнений с 3 неизвестными, так что строк в матрице 3, а элементов в каждой строке 4
# Для удобства восприятия будут использоваться переносы на новую строку

# Counter - счетчик для строк, Subcounter - счетчик для элементов

Numbers = [[3,4,6,7],
           [2,3,8,1],
           [5,4,2,6]]
# Проверка матрицы
def Sort(Matr):
    # Цикл проходит через строки и проверяет на наличие строк с нулями, а также столбцов с нулями
    amount_string = 0
    for counter in range (0,len(Matr)):
        # подсчёт нулей в строке
        amount_column = 0
        for subcounter in range(0,len(Matr[counter])-1):
            if Matr[counter][subcounter] == 0:
                amount_column+=1
        # Проверка на строку из нулей и выдача
        if amount_column == len(Matr[counter])-1:
            print("Система решений не имеет")
            break
        if Matr[counter][0] == 0:
            amount_string+=1
    # Если столбец состоит из нулей, то его можно отбросить и преобразовывать матрицу с меньшей размерностью
    if amount_string == len(Matr)-1:
        NewMatr=[]
        # Для работы создаётся промежуточный список
        InMatr=[]
        for counter in range(0,len(Matr)-1):
            # Происходит копирование элементов
            for subcounter in range(1,len(Matr[counter])):
                InMatr.append(Matr[counter][subcounter])
                # Само наполнение, а таакже очищение промежуточного списка
            NewMatr.append(InMatr)
            InMatr.clear()
        return NewMatr

    if Matr[0][0] == 0:
        # koryavaya perestanovka
        for counter in range (0,len(Matr[0])):
            var = Matr[0][counter]
            Matr[0][counter] = Matr[1][counter]
            Matr[1][counter] = var

def Gauss (Matr):
    PrintString(Matr)
    print()
    # Создать список решений
    Solutions = []
    # обозначить номер рабочей строки
    num_str = 0
    # Работа будет просиходить до предпоследней строки
    while num_str < len(Matr):
        # Сначала происходит деление всех чисел строки на значение в первом столбце
        for counter in range(num_str, len(Matr)):
            # Дополнение-исправление: если потенциальный делитель равен 0, то один из шагов уже выполнен,
            # поэтому дальнейший цикл не вызывается
            if Matr[counter][num_str]!=0:
                # Чтобы делить на это число, его нужно записать отдельно от остальных
                divider = Matr[counter][num_str]
                # Само деление чисел строки
                for subcounter in range(0, len(Matr[counter])):
                    Matr[counter][subcounter] = Matr[counter][subcounter] / divider
        # Отобразить изменения
        PrintString(Matr)
        print()
        # Вычитание из элементов следующей строки значений предыдущей
        for counter in range(num_str+1,len(Matr)):
            for subcounter in range(0,len(Matr[counter])):
                Matr[counter][subcounter] = Matr[counter][subcounter] - Matr[num_str][subcounter]
        PrintString(Matr)
        print()
        num_str+=1

    # Далее представлена старая часть кода, которая оставлена для понимания создания цикла нахождения решений

    # Внесем значение третьей переменной
    # Сейчас происходит работа с последней строкой, переменная осталась после цикла
    # Вообще, из-за того, что здесь происходит работа с матрицами, второй индекс можно указать равным количеству строк
    # матрицы (она квадратная, но добавляется столбец решений), однако здесь используется длина списка минус 1 как
    # нормер последнего элемента строки
    # Внесем значение этой переменной в список решений
    #Solutions.append(Matr[num_str][len(Matr[num_str])-1]/Matr[num_str][num_str])
    # Далее будем искать значение второй переменной
    num_str-=1
    #Equal = Solutions[0]*Matr[num_str][len(Matr[num_str])-2]
    #Solutions.append(Matr[num_str][len(Matr[num_str])-1]-Equal)
    # Можно попытаться расширить эту функцию на большее количество строк и столбцов в матрице

    # Работа будет продолжаться до тех пор, пок не закончатся обрабатываемые строки
    while num_str >=0:
        # Создаётся переменная для вычитания
        subtrahead = 0
        for n in range (0,len(Solutions)):
            # Перемножение элементов строки на решения и суммирование произведений
            summand = Matr[num_str][len(Matr[num_str])-2-n] * Solutions[n]
            subtrahead = subtrahead + summand
        # Внесем в список решений значение, получаемое посредством вычитания из свободного члена полученого вычитаемого
        Solutions.append((Matr[num_str][len(Matr[num_str])-1])-subtrahead)
        # Перейдём к строке выше
        num_str = num_str - 1
    # Изменить порядок решений
    Solutions.reverse()
    PrintString(Solutions)

# Вывод матрицы
def PrintString (Mass):
    for counter in range(0,len(Mass)):
        print(Mass[counter])
Sort(Numbers)
Gauss(Numbers)