"""
Пользователь вводит два целых числа x и y  > 1 (проверки на числа, целые, > 1).
Нужно создать матрицу размером (x, y). Т.е. один список размером x, состоящий из списков размером y.
Заполнить матрицу случайными числами в диапазоне от 0 до 1000.
Найти номера столбцов, в которых содержатся числа в интервале от 90 до 100.

Для начала можно матрицу ввести прямо в коде и сделать часть с нахождением номеров столбцов.

пример матрицы
m = [
    [1, 2, 7],
    [5, 4, 5],
    [5, 6, 8]
    ]
"""
import random as rnd

kolvX = int(input("Введите Х\n"))
kolvY = int(input("Введите Y\n"))


#lst1 = [rnd.randint(0, 10) for i in range(kolvX)]
#lst2 = [rnd.randint(0, 10) for i in range(kolvY)]
matrix = [[rnd.randint(0, 10) for y in range(kolvX)] for x in range(kolvY)]

print(matrix)

for im in range(kolvY):
    print(matrix[im])
