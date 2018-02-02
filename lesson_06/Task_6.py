"""
Задача 6

Заполнить список из шести элементов квадратными корнями произвольныз
целочисленныз значений. Вывести список на экран через запятую.
"""
#********************************************************
import random

count = 6

lst = [random.randint(0, 100) for i in range(count)]
print("lst=", lst)

print("~" * 50)

for j in lst:
    j = j ** 0.5
    print(j, end=", ")
#********************************************************

print("*" * 50)

import random
import math

count = 6
"""randoms = [str(math.sqrt(random.randint(1, 101))) for _ in range(count)]
print('Исходный список ', randoms)
"""

lst = [random.randint(0, 100) for i in range(count)]
print("lst=", lst)
lst1 = [str(math.sqrt(lst))]
#********************************************************
print("~" * 50)

#lst1 = str(math.sqrt(lst))
