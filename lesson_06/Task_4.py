"""
Задача 4

Заполнить список из шести элементов произвольными целочисленными значениями.
Найти максимальный элемент в списке, вывести его и его номер на экран. Два
варианта вычисления максимального элемента: с приминением цикла и без него.
"""
#first variant
#наполняем список рандомными числами
print("1" * 50)
import random

count = 6

lst = [random.randint(0, 100) for i in range(count)]
print(lst)

lst.sort(reverse=True)
print(lst)

print(lst[0])

print("2" * 50)

#second variant
#наполняем список рандомными числами
import random

count = 6

lst = [random.randint(0, 100) for i in range(count)]
print(lst)

print(max(lst))
print(lst.index(max(lst)))

print("3" * 50)

#
#наполняем список рандомными числами
import random

count = 6

lst = [random.randint(0, 100) for i in range(count)]
print(lst)

num = lst[0]
for i in lst:
    if i > num:
        num = i
        i +=1
print(num)
print(lst.index(num))
