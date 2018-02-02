"""
Задача 1

Заполнить список из шести элементов произвольными целочисленными значениями.
Вывести список на экран.
"""

import random

count = 6
"""
lst = []
i = 0
while i < 6:
    lst.append(random.randint(0, 100))
    i += 1
"""
lst = [random.randint(0, 100) for i in range(count)]
print(lst)
