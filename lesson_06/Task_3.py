"""
Задача 3

Заполнить список из шести элементов произвольными целочисленными значениями.
Вывести список на экран в обратной последовательности. Два варианта получения
обратной последовательности: с приминением цикла и без него.
"""
#first variant
import random as rnd

count = 6
lst = [rnd.randrange(0, 100) for i in range(count)]
"""
предвзятое отношение к данному циклу
i = 0
while i < 7:
    lst.append(rnd.randint(0, 100))
    i += 1
"""
print(lst)
lst.reverse()
print(lst)
print("~" * 50)
#second variant
count = 6
lst = [rnd.randrange(0, 100) for i in range(count)]
print(lst)
lst_r = []
for i in lst:
    lst_r.insert(0, i)
print(lst_r)
