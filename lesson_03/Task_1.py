"""
Вычислить модуль числа без использования библиотечных функций.
"""
x=float(input("Введите число ->\n"))
if x >= 0:
    y = x
    print("Модуль числа равен {}".format(y))
else:
    y = -x
    print("Модуль числа равен {}".format(y))
