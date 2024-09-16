from sympy import * #symbols, diff
import numpy as np
import myrandom
import time
import math as m
x = symbols('x')

increment = 1
def rand(a,b):
    global increment
    increment += 2

    start_value = m.ceil(time.time()) - time.time() + increment
    mid_value = m.ceil(start_value * 1e9)
    values = []
    for i in range(0,abs(b-a)+1):
        values.append(mid_value % abs(b-a) + a)

    finish_value = values[m.ceil(time.time()//increment)%len(values)]
    return finish_value

# Вики(eng/rus) Списки структур данных
# Вики(eng/rus) стандарт числа IEEE754
# Wiki красно-черные деревья, Ассоциативный массив, АВЛ-Деревья, В-Деревья
# Поиск в длину, ширину
# Новиков - Дискретная математика(деревня)
# Кнут, Кормен
# квантик, квант - задачи про дороги

nums=[]
for i in range(0,1000):
    nums.append(rand(1,183))
print(nums)

examples = []
for i in range(0,5): examples.append(nums[i])

j=0
indexes=[]
for i in range(len(nums)-4):
    if nums[i]==examples[0] :
        if nums[i+1] == examples[1]:
            if nums[i+2] == examples[2]:
                if nums[i+3] == examples[3]:
                    if nums[i+4]== examples[4]:
                        j+=1
                        indexes.append(i)
print(f"{j} повторений, индексы повторений: {indexes}")