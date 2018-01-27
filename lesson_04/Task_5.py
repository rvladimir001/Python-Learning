"""
Задача 5

Найдите количество четных цифр введёного натурального числа.
"""

num = int(input("Введите число ->"))
KakZnayuTakPishu = 0
while num > 0:
    if num % 2 == 0:
        KakZnayuTakPishu += 1
    num = num // 10
print("В числе {} чентых цифр".format(KakZnayuTakPishu))
