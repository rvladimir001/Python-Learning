"""
Задача 5

Найдите количество четных цифр введёного натурального числа.
"""

num = int(input("Введите число ->"))
chetnye = 0
while num > 0:
    if num % 2 == 0:
        chetnye += 1
    num = num // 10
print("В числе {} чентых цифр".format(chetnye))
