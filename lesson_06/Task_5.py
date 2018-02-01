"""
Задача 5

Заполнить список из десяти элементов произвольными целочисленными значениями.
Получить список из элементов певрого списка, стоящих на четных местах.
"""

import random

lst = []
i = 0
while i < 10:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)
print("dlina lst", len(lst))

print("~" * 50)

lst1 = []
j = 0
while j < 10:
    lst1.append(lst[j])
    j += 2
print(lst1)

print("~" * 50)
