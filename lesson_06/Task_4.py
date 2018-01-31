"""
Задача 4

Заполнить список из шести элементов произвольными целочисленными значениями.
Найти максимальный элемент в списке, вывести его и его номер на экран. Два
варианта вычисления максимального элемента: с приминением цикла и без него.
"""
#first variant
import random

lst = []
i = 0
while i < 6:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)
lst.sort(reverse=True)
print(lst)
print(lst[0])


#second variant
