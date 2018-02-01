"""
Задача 8

Заполнить список из десяти элементов произвольными целочисленными значениями.
Затем четные элементы расположить в начале списка, нечетные - в конце.
"""

import random

lst = []
i = 0
while i < 10:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)
lst1 = lst[0:10:2]
lst2 = lst[1:10:2]
print(lst1)
print(lst2)
lst = lst1 + lst2
print(lst)
