"""
Задача 7

Заполнить список из десяти элементов произвольными целочисленными значениями
(без использования цикла). Удалить те элементы, значения которых не кратны 3.
"""

import random

lst = list(range(0, 70, 7))

print(lst)

j = 0
for i in lst:
    if i % 3 != 0:
        lst.remove(i)
        print(lst)

print(lst)
