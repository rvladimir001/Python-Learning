"""
Задача 5

Заполнить список из десяти элементов произвольными целочисленными значениями.
Получить список из элементов певрого списка, стоящих на четных местах.
"""

import random

count = 10

lst = [random.randint(0, 100) for i in range(count)]
print("lst=", lst)
print("dlina lst", len(lst))

print("~" * 50)

lst1 = []
j = 0
while j < 10:
    lst1.append(lst[j])
    #print(lst1)
    j += 2
print("lst1=", lst1)

print("*" * 50)
lst2 = []

"""выдаст только четные символы
for i in lst:
    if i % 2 == 0:
        lst2.append(i)
"""
for i in range(len(lst)):
    if i % 2 == 0:
        lst2.append(lst[i])
print("lst2=",lst2)

print("*" * 50)
