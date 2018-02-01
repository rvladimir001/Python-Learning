"""
Задача 4

Заполнить список из шести элементов произвольными целочисленными значениями.
Найти максимальный элемент в списке, вывести его и его номер на экран. Два
варианта вычисления максимального элемента: с приминением цикла и без него.
"""
#first variant
#наполняем список рандомными числами
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

print("~" * 50)

#second variant
#наполняем список рандомными числами
import random

lst = []
i = 0
while i < 6:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)

print(max(lst))

print("~" * 50)

#
#наполняем список рандомными числами
import random

lst = []
i = 0
while i < 6:
    lst.append(random.randint(0, 100))
    i += 1
print(lst)

num = lst[0]
for i in lst:
    if i > num:
        num = i
        i +=1
print(num)
