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
"""
нихрена не понял: для и в последовательности длины т.е 10
если остаток деления 0 то запихиваем дальше
но последовательность 10 это же [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] так?
если так то почему когда запихиваем остатки от деления то туда нормальные числа
падают?
"""
for i in range(len(lst)):
    if i % 2 == 0:
        lst2.append(lst[i])
print("lst2=",lst2)

print("*" * 50)
