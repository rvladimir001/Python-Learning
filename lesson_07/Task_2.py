"""
Задача 2
Написать функцию, возвращающую два введеных с клавиатуры числа.
"""
def Nums():
    global a
    global b
    a = int(input("Введите число А"))
    b = int(input("Введите число В"))
Nums()
print(a, b)
