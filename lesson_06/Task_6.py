"""
Задача 6

Заполнить список из шести элементов квадратными корнями произвольныз
целочисленныз значений. Вывести список на экран через запятую.
"""
import random

lst = []
i = 0
while i < 6:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)
for j in lst:
    j = j ** 0.5
    print(j, end=", ")
